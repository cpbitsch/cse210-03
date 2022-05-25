<<<<<<< HEAD:jumper/game/Parachutist.py
class Jumper:
    """Creates the jumper."""

    def __init__(self):
        self._lines_to_draw = [
            " ___ ",
            "/___\\",
            "\\   /",
            " \\ /",
            "  0 ",
            " /|\\",
            " / \\"]
        self.is_dead=False

    def __str__(self):
        results = ''
        for line in self._lines_to_draw:
            results += line + '\n'

        return results

    def break_chute(self):
        if len(self._lines_to_draw) >3:
            self._lines_to_draw.pop(0)
        else:
            self._lines_to_draw[0] = self._lines_to_draw[0].replace('0','X')
            self.is_dead=True
=======
import sys

def main():

	print('Please enter the password.')
	
	password = 'burger'
	user_input = input('Please Enter Password: ')
	
	if user_input != password:
		sys.exit('Incorrect Password, terminating... \n')
		
	print("User is logged in!")
if __name__ == "__main__":
	main()
#Has an example of a password protection that will limit access to only those who have the password.
#it can be changed depending on the preference of the team.
	main()
class Jumper:
    """Creates the jumper."""

    def __init__(self):
        self._lines_to_draw = [
            " ___ ",
            "/___\\",
            "\\   /",
            " \\ /",
            "  0 ",
            " /|\\",
            " / \\"]
        self.is_dead=False

    def __str__(self):
        results = ''
        for line in self._lines_to_draw:
            results += line + '\n'

        return results

    def break_chute(self):
        if len(self._lines_to_draw) >3:
            self._lines_to_draw.pop(0)
        else:
            self._lines_to_draw[0] = self._lines_to_draw[0].replace('0','X')
            self.is_dead=True
>>>>>>> 59047046b02da5fcf8cdf9dc660edc60d18ee72f:Parachutist.py
