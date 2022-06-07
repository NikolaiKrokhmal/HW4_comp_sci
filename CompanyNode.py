from Company import Company
import copy


class CompanyNode(Company):

    _comparison_type = getattr(Company, "_comparison_type")

    def __init__(self, name, stocks_num, stock_price, comp_type):
        super().__init__(name, stocks_num, stock_price, comp_type)
        self.__children = []
        self.__parent = None

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def is_leaf(self):
        if len(self) == 0:
            return True
        else:
            return False

    def add_child(self, child: "CompanyNode"):
        if self.check_rule(child):
            self.__children.append(child)
            child._CompanyNode__parent = self
            return True
        else:
            return False

    def total_net_worth(self):
        return self.get_total_sum()

    def test_node_order_validity(self):
        for child in self.get_children():
            if not self.check_rule(child):
                return False
        while self.get_parent() is not None:
            if not self.get_parent().check_rule(self):
                return False
        return True

    def __len__(self):
        return len(self.__children)

    """def __repr__(self):
        text = "[{0}, [{1}]]"
        totalText = ""
        if len(self.__children) == 0:
            return text.format(self.representation(), "")
        for child in self.__children:
            totalText += child.__repr__()
        return text.format(self.representation(), totalText)"""
    def __repr__(self):
        return str(self.name)

    def is_ancestor(self, other: "CompanyNode"):
        while other.get_parent() is not None:
            if self == other.get_parent():
                return True
            else:
                other = other.get_parent()
        if self is other:
            return True
        return False

    def __add__(self, other: "CompanyNode"):
        if other.is_ancestor(self):
            raise ValueError("Error: Cant merge ancestor into self")
        mergedCompany = CompanyNode(self.name, self.stocks_num, self.stock_price, self.comp_type)
        mergedCompanyMarketCap = self.get_market_cap() + other.get_market_cap()
        mergedCompany.add_stocks(other.stocks_num)
        mergedCompany.stock_price = mergedCompanyMarketCap / mergedCompany.stocks_num
        other.detach_node()
        for child in self.__children:
            mergedCompany.add_child(copy.deepcopy(child))
        othersChildren = other.get_children()
        for child in othersChildren:
            mergedCompany.add_child(copy.deepcopy(child))
        mergedCompany._CompanyNode__parent = copy.deepcopy(self.__parent)
        if not mergedCompany.test_node_order_validity:
            raise ValueError("Error: cant merge nodes - new node doesnt obey rule")
        return mergedCompany

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type is not ("net value" or "stock num" or "stock price" or "total sum"):
            return False
        else:
            CompanyNode._comparison_type = comparison_type
            return True

    def check_rule(self, other: "CompanyNode"):
        if self._comparison_type == "net value":
            if self.get_market_cap() >= other.get_market_cap():
                return True
            else:
                return False
        elif self._comparison_type == "stock num":
            if self.stocks_num >= other.stocks_num:
                return True
            else:
                return False
        elif self._comparison_type == "stock price":
            if self.stock_price >= other.stock_price:
                return True
            else:
                return False
        elif self._comparison_type == "total sum":
            if self.get_total_sum() > other.get_total_sum():
                return True
            else:
                return False

    def get_total_sum(self):
        totalValue = self.get_market_cap()
        child_value = 0
        if len(self.__children) == 0:
            return totalValue
        for child in self.__children:
            child_value += child.get_total_sum()
        return totalValue + child_value

    def detach_node(self):
        parent = self.__parent
        parentsChildren = parent.get_children()
        selfIndex = parentsChildren.index(self)
        parent._CompanyNode__children = parentsChildren[:selfIndex] + parentsChildren[selfIndex+1:]

    def __lt__(self, other: "CompanyNode"):
        if type(other) is not CompanyNode:
            return False
        if self._comparison_type != "total sum":
            return super().lt_compare(other)
        else:
            return self.get_total_sum() < other.get_total_sum()

    def __eq__(self, other: "CompanyNode"):
        if type(other) is not CompanyNode:
            return False
        if self._comparison_type != "total sum":
            return super().eq_compare(other)
        else:
            return self.get_total_sum() == other.get_total_sum()

    def __gt__(self, other: "CompanyNode"):
        if type(other) is not CompanyNode:
            return False
        if self._comparison_type != "total sum":
            return super().__gt__(other)
        else:
            return other.get_total_sum() < self.get_total_sum()

    def __ne__(self, other: "CompanyNode"):
        if type(other) is not CompanyNode:
            return False
        if self._comparison_type != "total sum":
            return super().__ne__(other)
        else:
            return not self.get_total_sum() == other.get_total_sum()

    def __ge__(self, other: "CompanyNode"):
        if type(other) is not CompanyNode:
            return False
        if self._comparison_type != "total sum":
            return super().__ge__(other)
        else:
            return not self.get_total_sum() < other.get_total_sum()

    def __le__(self, other: "CompanyNode"):
        if type(other) is not CompanyNode:
            return False
        if self._comparison_type != "total sum":
            return super().__le__(other)
        else:
            return not other.get_total_sum() < self.get_total_sum()

    def set_stock_price(self, stock_price):
        previousPrice = self.stock_price
        super(CompanyNode, self).set_stock_price(stock_price)
        if self.test_node_order_validity():
            return True
        else:
            super(CompanyNode, self).set_stock_price(previousPrice)
            return False

    def set_stocks_num(self, stocks_num):
        previousNum = self.stocks_num
        super(CompanyNode, self).set_stocks_num(stocks_num)
        if self.test_node_order_validity():
            return True
        else:
            super(CompanyNode, self).set_stocks_num(previousNum)
            return False

    def update_net_worth(self, net_worth):
        previousNetWorth = self.net_worth()
        super(CompanyNode, self).update_net_worth(net_worth)
        if self.test_node_order_validity():
            return True
        else:
            super(CompanyNode, self).update_net_worth(previousNetWorth)
            return False

    def add_stocks(self, number):
        super(CompanyNode, self).add_stocks(number)
        if self.test_node_order_validity():
            return
        else:
            super(CompanyNode, self).add_stocks(-number)
            return False


