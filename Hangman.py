#Step 5
import replit
from replit import clear
import random
import hangman_art
import hangman_words
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py done
#Delete this line: word_list = ["ardvark", "baboon", "camel"] done

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game. done

print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks done
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know. done
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            if guess == letter:
               print("Thats the right letter")
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word. done
        lives -= 1
        print("It is not the correct letter!")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.done
    print(f"{' '.join(display)}")

    #Check if user has got all letters.done
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.done
    print(stages[lives])
