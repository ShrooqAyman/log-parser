class FilterContext:
    """
    A context class that uses a filtering strategy to filter data.

    Attributes:
        strategy: the filtering strategy to use.
    """
    def __init__(self, strategy):
        """
        Initializes an instance of the FilterContext class.
        
        Args:
            strategy: the initial filtering strategy to use.
        """
        self.strategy = strategy

    def set_strategy(self, strategy):
        """
        Sets the filtering strategy to use.
        
        Args:
            strategy: the initial filtering strategy to use.
        """
        self.strategy = strategy
        
    def filter(self, data, context):
        """
        Filters the data using  filtering strategy.
        
        Args:
            data(list):  data to be filtered.
            context:  information that required to filter data.
        
        """
        return self.strategy.filter(data, context)