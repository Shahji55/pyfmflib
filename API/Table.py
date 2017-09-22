class Table:

    def  __init__(
            self,
            name,
            symbol
    ):

        self.name = name
        self.symbol = symbol
        self.data_definitions = None
        self.no_columns = None
        self.no_rows = None
        self.data = None
        self.comments = None

    def initialize(*args):

        print (args)
        print (len(args))

#        if len(args) < 2:
#            raise Exception('Number of arguments specified is invalid')

        return Table(name=None, symbol=None, data_definitions=[], no_columns=None, no_rows=None, data=[], comments=None)


    def get_table(self,symbol):
        if self.s != symbol:
            raise Exception('Symbol does not exist')

