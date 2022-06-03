class Company:

    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        if not check_string(name) or not check_stocks_num(stocks_num) or not check_stock_price(stock_price) or not check_string(comp_type):
            raise ValueError("One or more of the argument provided does not meet requirements")
        else:
            self.name = name
            self.stocks_num = stocks_num
            self.stock_price = stock_price
            self.comp_type = comp_type

    def net_worth(self):
        return self.stocks_num * self.stock_price

    def set_name(self, name):
        if not check_string(name):
            return False
        else:
            self.name = name
            return True

    def set_stocks_num(self, stocks_num):
        if not check_stocks_num(stocks_num):
            return False
        else:
            marketCap = self.get_market_cap()
            self.stocks_num = stocks_num
            self.stock_price = marketCap / self.stocks_num
            return True

    def set_stock_price(self, stock_price):
        if not check_stock_price(self.stock_price):
            return False
        else:
            marketCap = self.get_market_cap()
            if stock_price > marketCap:
                return False
            self.stock_price = stock_price
            self.stocks_num = marketCap // self.stock_price
            return True

    def set_comp_type(self, comp_type):
        if not check_string(comp_type):
            return False
        else:
            self.comp_type = comp_type
            return True

    def update_net_worth(self, net_worth):
        if not check_stock_price(net_worth):
            return False
        else:
            self.stock_price = net_worth / self.stocks_num
            return True

    def add_stocks(self, number):
        if self.stocks_num + number <= 0:
            return False
        else:
            self.stocks_num += number
            return True

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type is not ("net value" or "stock num" or "stock price"):
            return False
        else:
            Company._comparison_type = comparison_type
            return True

    def __str__(self):
        text = "({0} {1} stocks, Price: {2}, {3}, Net Worth: {4})"
        return text.format(self.name, self.stocks_num, self.stock_price, self.get_market_cap())

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if type(other) is not Company:
            return False
        if Company._comparison_type == "net value":
            return (self.stocks_num * self.stock_price) < other.stocks_num * other.stock_price
        elif Company._comparison_type == "stock num":
            return self.stocks_num < other.stocks_num
        elif Company._comparison_type == "stock price":
            return self.stock_price < other.stock_price

    def __gt__(self, other):
        if type(other) is not Company:
            return False
        return other < self

    def __eq__(self, other):
        if type(other) is not Company:
            return False
        if Company._comparison_type == "net value":
            return (self.stocks_num * self.stock_price) == other.stocks_num * other.stock_price
        elif Company._comparison_type == "stock num":
            return self.stocks_num == other.stocks_num
        elif Company._comparison_type == "stock price":
            return self.stock_price == other.stock_price

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        totalStockNum = self.stocks_num + other.stocks_num
        totalMarketCap = self.get_market_cap() + other.get_market_cap
        newStockPrice = totalMarketCap / totalStockNum
        return Company(self.name, totalStockNum, newStockPrice, self.comp_type)

    def get_market_cap(self):
        return self.stocks_num * self.stock_price


def check_string(myString: str):
    if type(myString) is not str:                                                   # check if string
        return False
    wordlist = myString.split()
    firstWord = wordlist[0]
    for word in wordlist:
        for myChar in word:
            if len(word) <= 1:                                                      # check if each word is at least 2 chars long
                return False
            if not (65 <= ord(myChar) <= 90) and not (97 <= ord(myChar) <= 122):    # check if words are english letters
                return False
    if firstWord[0] == firstWord[0].lower():                                        # check if first letter is upper case
        return False
    if len(wordlist) <= 1:                                                          # check if there are less then 2 words
        return False
    amountOf_ = 0                                                                   # check if there is only 1 space between words
    for myChar in myString:
        if myChar == " ":
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

