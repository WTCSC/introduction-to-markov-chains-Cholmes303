import random
import re
import argparse

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""

# Opens file and makes it readable
corpus_file = open("corpus.txt", 'r')
# Sets x to user input, user chooses the word count
x = int(input('word count: '))
# Reads the file
read_corpus_file = corpus_file.read(x)
# Prints out requested amount of words from file 
print(read_corpus_file)

# Sets text variable
text = read_corpus_file
# Creates a dictionary for punctuation
transitions = {
    "comma":",",
    "period":".",
    "exclamation point":"!",
}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""

words = re.findall(r'[^\W_]+', text) 
#text.split()
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
print(transitions)

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""

def generate_text(start_word, num_words):
    current_word = start_word.upper([0])
    result = [current_word]
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    return " ".join(result.append("."))

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""

def main():

    # Description of the program
    parser = argparse.ArgumentParser(description='Sentence generator from a selected corpus')
    
    # Adds two arguments that can be used to compare two files to crack password
    parser.add_argument('num_words', help='The length of the output') 
    parser.add_argument('start_word', help='Choose starting word')

    args = parser.parse_args()

    # Adds the two arguments defined to the password cracking function
    arguments = generate_text(args.start_word, args.num_words)
    
    # Loops through the arguments in password cracking function and prints matching usernames and passwords
    for x in arguments:
        print(x)

if __name__ == "__main__":
    main()
