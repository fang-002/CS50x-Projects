-- Keep a log of all SQL queries that you run on the database.

-- Find the crime scene report for the theft on Humphrey Street on July 28, 2025
SELECT description FROM crime_scene_reports WHERE year = 2025 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- Find the interviews of witnesses who were present at the bakery on the day of the theft
SELECT name, transcript FROM interviews WHERE year = 2025 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- Find the thief using security logs, ATM withdrawals, phone calls, and the earliest flight out on July 29, 2025
SELECT name FROM people
WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2025 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25 AND activity = 'exit'
)
AND id IN (
    SELECT person_id FROM bank_accounts
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
    WHERE year = 2025 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
)
AND phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2025 AND month = 7 AND day = 28 AND duration < 60
)
AND passport_number IN (
    SELECT passport_number FROM passengers
    WHERE flight_id = (
        SELECT id FROM flights
        WHERE year = 2025 AND month = 7 AND day = 29
        ORDER BY hour, minute LIMIT 1
    )
);

-- Find the destination city the thief escaped to
SELECT city FROM airports
WHERE id = (
    SELECT destination_airport_id FROM flights
    WHERE year = 2025 AND month = 7 AND day = 29
    ORDER BY hour, minute LIMIT 1
);

-- Find the accomplice who helped the thief
SELECT name FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls
    WHERE year = 2025 AND month = 7 AND day = 28 AND duration < 60
    AND caller = (SELECT phone_number FROM people WHERE name = 'Bruce')
);
