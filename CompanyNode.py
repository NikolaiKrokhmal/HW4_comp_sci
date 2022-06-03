from Company import Company


class CompanyNode(Company):

    _comparison_type = Company._comparison_type

    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company(name, stocks_num, stock_price, comp_type)
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

    def add_child(self, child):
        pass

    def total_net_worth(self):
        pass

    def test_node_order_validity(self):
        pass

    def __len__(self):
        return len(self.__children)

    def __repr__(self):
        pass

    def is_ancestor(self, other):
        pass

    def __add__(self, other):
        pass

    def check_rule(self, other):
        if self._comparison_type == "net value":
            if
        elif self._comparison_type == "stock num":
            pass
        elif self._comparison_type == "stock price":
            pass
        elif self._comparison_type == "total sum":
            pass

