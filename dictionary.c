// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table (larger size for better distribution)
const unsigned int N = 26 * 26 * 26;

// Global variable to keep track of word count
unsigned int word_count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Create a lowercase version of the word for case-insensitive comparison
    char lowercase_word[LENGTH + 1];
    int length = strlen(word);
    for (int i = 0; i < length; i++)
    {
        lowercase_word[i] = tolower(word[i]);
    }
    lowercase_word[length] = '\0';

    // Get the hash index for the word
    unsigned int index = hash(lowercase_word);

    // Set cursor to the head of the linked list at that index
    node *cursor = table[index];

    // Traverse the linked list
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, lowercase_word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number (Using djb2 hash function for great distribution)
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;
    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + c; // hash * 33 + c
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Read words from file one by one
    char buffer[LENGTH + 1];
    while (fscanf(file, "%s", buffer) != EOF)
    {
        // Allocate memory for a new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }

        // Copy word into the node
        strcpy(new_node->word, buffer);
        new_node->next = NULL;

        // Hash word to obtain a hash value
        unsigned int index = hash(buffer);

        // Insert node into hash table at that location
        new_node->next = table[index];
        table[index] = new_node;

        // Increment word count
        word_count++;
    }

    // Close dictionary file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Iterate through every bucket in the hash table
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
