import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # جلب الأسهم اللي اليوزر معاه
    rows = db.execute("""
        SELECT symbol, SUM(shares) AS total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, session["user_id"])

    portfolio = []
    total_value = 0

    # جلب سعر كل سهم حالياً وحساب قيمته
    for row in rows:
        stock = lookup(row["symbol"])
        value = stock["price"] * row["total_shares"]
        portfolio.append({
            "symbol": stock["symbol"],
            "shares": row["total_shares"],
            "price": stock["price"],
            "value": value
        })
        total_value += value

    # جلب كاش اليوزر
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    grand_total = total_value + cash

    return render_template("index.html", portfolio=portfolio, cash=cash, grand_total=grand_total)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol", 400)

        stock = lookup(symbol)
        if stock is None:
            return apology("invalid symbol", 400)

        try:
            shares = int(shares)
        except (TypeError, ValueError):
            return apology("shares must be a positive integer", 400)

        if shares <= 0:
            return apology("shares must be a positive integer", 400)

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        cost = shares * stock["price"]

        if cost > cash:
            return apology("can't afford", 400)

        # خصم الفلوس وتسجيل العملية
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", cost, session["user_id"])
        db.execute("""
            INSERT INTO transactions (user_id, symbol, price, shares)
            VALUES (?, ?, ?, ?)
        """, session["user_id"], stock["symbol"], stock["price"], shares)

        return redirect("/")

    else:
        return render_template("buy.html")
