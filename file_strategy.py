class SaveContext:
    """
    A context class that uses a saving strategy to save output data.

    Attributes:
        strategy: the saving strategy to use.
    """
    def __init__(self, strategy):
        """
        Initializes an instance of the SaveContext class.
        
        Args:
            strategy: the initial filtering strategy to use.
        """
        self.strategy = strategy

    def set_strategy(self, strategy):
        """
        Sets the saving strategy to use.
        
        Args:
            strategy: the initial filtering strategy to use.
        """
        self.strategy = strategy
        
    def save(self, data, filename):
        """
        Save the data using saving strategy.
        
        Args:
            data(list):  data to be saved.
            filename: output file name.
        
        """
        return self.strategy.save(data, filename)