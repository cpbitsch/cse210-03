# cse210-03

Objects: Director, word, guess_controller, parachute 

class: Director (Chris, Ricky)
    Starts the game and manages other classes. Determines end conditions.
    Attributes:
        is_playing
        word
    Methods:
        start_game
        get_word
        get_user_input
        guess_vs_word

class: Word (Santiago)
    Choose a word from a word bank and store it
    Attributes:
        word
        word_bank
    Methods:
        choose_word
        get_word
        load_bank

class: guess_controller (Jacob)
    Gets user input and checks it against the word. Stores correct letters
    Attributes:
        user_input
        correct_letters
    Methods
        get_user_input
        check_letter
        display_correct

class: parachute (Joshua)
    Stores lives and person art
    Attributes:
        lives
    Methods:
        change_lives
        display_lives