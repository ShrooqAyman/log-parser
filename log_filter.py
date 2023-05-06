from abc import ABC, abstractmethod
import re, datetime

class LogFilter(ABC):
    """
    Abstract class representing a filter for log records.        
    """
    @abstractmethod
    def filter(self, data, context):
        """
        Abstract method that takes data and filters it depends on criteria.        
        """
        pass

class LevelFilter(LogFilter):
    """
    Subclass of LogFilter that filters log records based on their level.    
    """

    def filter(self, data, context):
        """
        Filters log records based on their level.

        Args:
            data (list): list of LogEntry objects
            context (str): a string representing the log level to filter by.
        """
        filter_result = []
        for entry in data:
           if entry.level == context:
               filter_result.append(entry)
        return filter_result


class ModuleFilter(LogFilter):
    """
    Subclass of LogFilter that filters log records based on their Module.    
    """
    
    def filter(self, data, context):
        """
        Filters log records based on their Module.

        Args:
            data (list): list of LogEntry objects
            context (str): a string representing the log module to filter by.
        """
        filter_result = []
        for entry in data:
           if entry.module == context:
               filter_result.append(entry)
        return filter_result

class DataRangeFilter(LogFilter):
    """
    Subclass of LogFilter that filters log records based on Date range.    
    """
    
    def filter(self, data, context):
        """
        Filters log records based on date range.

        Args:
            data (list): list of LogEntry objects
            context (dict): a dictionary representing the log date range to filter by.
        """
        date1 = context['date1']
        date2 = context['date2']
        date_1 =  datetime.datetime(int(date1[0:4]),int( date1[5:7]), int(date1[8:10]))
        date_2 =  datetime.datetime(int(date2[0:4]),int( date2[5:7]), int(date2[8:10]))

        filter_result = []
        date_pattern = r'[0-9]{4}\-[0-9]{2}-[0-9]{2}'
        for entry in data: 
           date_str = re.search(pattern=date_pattern, string=entry.timestamp).group(0)
           date = datetime.datetime(int(date_str[0:4]),int( date_str[5:7]), int(date_str[8:10]))
           
           if date >= date_1 and date <= date_2:
               filter_result.append(entry)

        return filter_result