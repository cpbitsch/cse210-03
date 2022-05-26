class guess_controller:

    """Creates the guess controller"""

    def __init__(self):

        self._user_input = ""
        self._correct_letters = ""



    def get_user_input(self):

        self.user_input = input("Enter a letter.\n")



    def __check_letter__(self,input_letter):

        if input_letter not in (self._letters):

            self._guess_count = self._guess_count + 1

            self._guess_output = False

        elif input_letter in (self._letters):

            self._guess_count = self._guess_count + 1

            self._guess_output = True



    def display_correct(self):

        if self._guess_output == True:

            return True

        elif self._guess_output == False:

            return False

        else:

            return "Error"

