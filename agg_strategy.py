class AggregateContext:
    """
    A context class that uses a aggreagation strategy to aggregate data.

    Attributes:
        strategy: the aggreagation strategy to use.
    """
    def __init__(self, strategy):
        """
        Initializes an instance of the AggregateContext class.
        
        Args:
            strategy: the initial aggreagation strategy to use.
        """
        self.strategy = strategy

    def set_strategy(self, strategy):
        """
        Sets the aggreagation strategy to use.
        
        Args:
            strategy: the initial aggreagation strategy to use.
        """
        self.strategy = strategy

    def aggregate(self, data):
        """
        Filters the data using  aggreagation strategy.
        
        Args:
            data(list):  data to be filtered.
            context:  information that required to aggregate data.
        
        """
        return self.strategy.aggregate(data)