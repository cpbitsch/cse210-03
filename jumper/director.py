from word.word import Word
from game.Parachutist import Jumper
from game.guess_controller import guess_controller

class Director():

    def __init__(self):
        self.word = Word()
        self.jumper = Jumper()
        self.game_over = False

    

    def game_loop(self):

        def check_input(full_word_str, full_word_list, game_word, letter):
            
            #checks if letter is in the original word
            if letter in full_word_str:
                #if found loops through the list to get the index where it matches
                #and replaces the interactible list with the letter
                for i in range(len(full_word_list)):
                    if full_word_list[i] == letter:
                        game_word[i] = letter
                
                #if correct guess returns True else returns False
                return True
            else:
                return False

        # -----------------------------------------------------------


        #calls Word class to get word from bank
        full_word_str = self.word.get_word()

        #converts word to list for iterations
        full_word_list = list(full_word_str)

        #creates a duplicate of the word for interacting with
        game_word = full_word_list.copy()

        #changes interactive word from letters to "-"
        for i in range(len(game_word)):
            game_word[i] = "-"
        
        #converts list to string for display
        game_word_str = " ".join(game_word)

        #creates list to store guessed letters
        guessed_letters = []

        while not self.game_over:

            #prints "-"'d word
            print(game_word_str)
        
            #draws person
            print(self.jumper.__str__())

            #letter = self.user.get_user_input()
            letter = input("guess a letter: ")

            #if guessed a letter already guess loops until one is not
            while letter in guessed_letters:
                letter = input("Already guessed. guess a new letter: ")
            else:
                #adds guessed letter to list
                guessed_letters.append(letter)


            check = check_input(full_word_str, full_word_list, game_word, letter)

            #converts list to string for display
            game_word_str = " ".join(game_word)

            if not check:
                self.jumper.break_chute()

                if self.jumper.is_dead:
                    self.game_over = True

                    print()
                    print(self.jumper.__str__())
                    print(f"The word was {full_word_str}")
                    print("Better luck next time")
                    print()
                    print("Game Over")
                    print()
            
            if game_word == full_word_list:
                self.game_over = True
                print()
                print("You won!")
                print("Congratulations!")
