from Company import Company


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
            child.__parent = self.name
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

    def __repr__(self):
        pass

    def is_ancestor(self, other: "CompanyNode"):
        while other.get_parent() is not None:
            if self.name == other.get_parent():
                return True
            else:
                other = other.get_parent()
        return False

    def __add__(self, other: "CompanyNode"):
        pass

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
