class LogEntry:
    """
    Class representing log Entry

    Attributes:
        timestamp (str): string representing the time and date when the log entry was created. 
        level (str) : string representing the log level (INFO, DEBUG, WARN or ERROR). 
        module (str) : string representing the module name. 
        message (str) : string representing the message.
    """

    def __init__(self, timestamp, level, module, message) -> None:
        """
        Initialize an instance from LogEntry class.

        Args:
            timestamp (str): string representing the time and date when the log entry was created. 
            level (str) : string representing the log level (INFO, DEBUG, WARN or ERROR). 
            module (str) : string representing the module name. 
            message (str) : string representing the message.
        
        Returns:
            None
        """
        self.timestamp = timestamp
        self.level = level 
        self.module = module
        self.message = message