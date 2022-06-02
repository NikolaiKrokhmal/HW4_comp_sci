class Company:
    def __init__(self, name, stocks_num, stock_price, comp_type):
        pass

    def net_worth(self):
        pass

    def set_name(self, name):
        pass

    def set_stocks_num(self, stocks_num):
        pass

    def set_stock_price(self, stock_price):
        pass

    def set_comp_type(self, comp_type):
        pass

    def update_net_worth(self, net_worth):
        pass

    def add_stocks(self, number):
        pass

    @classmethod
    def change_comparison_type(cls, comparison_type):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __add__(self, other):
        pass


def check_string(myString: str):
    if type(myString) is not str:                                                   # check if string
        return False
    wordlist = myString.split()
    firstWord = wordlist[0]
    for word in wordlist:
        for char in word:
            if len(word) <= 1:                                                      # check if each word is at least 2 chars long
                return False
        uniCodeRep = ord(char)
        if not (65 <= uniCodeRep <= 90) and not (97 <= uniCodeRep <= 122):          # check if words are english latters
            return False
    if firstWord[0] == firstWord[0].lower():                                        # check if first letter is upper case
        return False
    if len(wordlist) <= 1:                                                          # check if there are less then 2 words
        return False
    amountOf_ = 0                                                                   # check if there is only 1 space between words
    for char in myString:
        if char == " ":
            amountOf_ += 1
    if amountOf_ != len(wordlist) - 1:
        return False
    return True


def check_stocks_num(stocks_num: int):
    if type(stocks_num) is not int:                                                 # check if int
        return False
    if stocks_num > 0:                                                              # check if positive
        return False


def check_stock_price(stock_price):
    if type(stock_price) is not int and stock_price is not float:                   # check if int or float
        return False
    if stock_price > 0:                                                             # check if positive
        return False

