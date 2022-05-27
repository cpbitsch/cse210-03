import csv, random



class Word:
    """Choose a word from a word bank and store it 
        Attributes: word word_bank 
        Methods: choose_word get_word load_bank"""
    
    def __init__(self):
        ## attribute for storing the relative path + name of the CSV file        
        self._word_bank = self.__load_bank__()        
        self._word = self.__choose_word__(self._word_bank)
    
    def get_word(self):
        return self._word

    def __choose_word__(self, bank_list):
        a_word = bank_list[random.randint(0, bank_list.__len__() - 1)]
        return a_word

    def __load_bank__(self):
        _csv_file = "jumper\word\persistent_word_bank.csv"
        word_bank = []        
        try:
            with open(_csv_file) as file:
                #print("Opened csv file...")
                csvreader = csv.reader(file, delimiter = ',')
                for line in csvreader:
                    word_bank.append(line[0])
            return word_bank
        except (FileNotFoundError, IOError):
            print("There was a problem loading the CSV file...") 