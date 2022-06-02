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
        pass

    def add_child(self, child):
        pass

    def total_net_worth(self):
        pass

    def test_node_order_validity(self):
        pass

    def __len__(self):
        pass

    def __repr__(self):
        pass

    def is_ancestor(self, other):
        pass

    def __add__(self, other):
        pass
