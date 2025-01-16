import random

# List of words for the game
word_list = ["python", "hangman", "developer", "computer", "programming", "challenge", "algorithm"]

# Function to select a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the Hangman game
def play_hangman():
   
    word = choose_word()
    guessed_letters = set()  
    incorrect_guesses = 0  
    max_incorrect_guesses = 6  
    guessed_word = ['_'] * len(word)  

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("You have 6 incorrect guesses to make.")
    
   
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
    
        guess = input("Enter a letter: ").lower()
        
       
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
      
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue
        
 
        guessed_letters.add(guess)
        
        
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, the letter '{guess}' is not in the word.")
        
       
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
     
        print(f"\nGame Over! The correct word was: {word}")

if __name__ == "__main__":
    play_hangman()
