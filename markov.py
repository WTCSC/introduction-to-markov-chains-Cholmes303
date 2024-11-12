import random
import argparse

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""

# Opens file and makes it readable.
corpus_file = open("corpus.txt", 'r', encoding='utf8')

# Reads the file.
read_corpus_file = corpus_file.read()
# Sets text variable.
text = read_corpus_file

# Creates a dictionary for punctuation and newline to remove newlines.
transitions = {
    "comma":",",
    "period":".",
    "exclamation point":"!",
    "question mark":"?",
    "semicolon":";",
    "new line": "\n",
    "apostrophy":"'",
}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""

# Sets words variable and splits text by spaces.
words = text.split()

# Loops through words to build the Markov chain, the word possibilities after each chosen word.
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

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

# Function to generate text at a chosen starting word and amount of words.
def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word]
    for _ in range(num_words):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    return f"{' '.join(result)}."

"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate

"""

def main():

    # Description of the program.
    parser = argparse.ArgumentParser(description='Sentence generator from a selected corpus')
    
    # Adds two arguments that can be used to choose the starting word that is used and the number of words that is used.
    parser.add_argument('start_word', help='Choose starting word', type=str)
    parser.add_argument('num_words', help='The length of the output', type=int) 

    args = parser.parse_args()

    # Adds the two arguments defined to the text generating function.
    arguments = generate_text(args.start_word, args.num_words)
    
    # Prints the generated text.
    print(arguments)

if __name__ == "__main__":
    main()
