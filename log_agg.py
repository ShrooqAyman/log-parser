from abc import ABC, abstractmethod
import datetime, re

class LogAggregator(ABC):
    """
    Abstract class representing an aggregator for log records.        
    """
    
    @abstractmethod
    def aggregate(self, data):
        """
        Abstract method that takes data and aggregate.  

        Args:
            data (list): list of LogEntry objects
        """
        pass

class LevelAggregator(LogAggregator):
    """
    Subclass of LogAggregator that aggregate log records by level. 
    """
    def aggregate(self, data):
        """
        Aggregates records by level.  

        Args:
            data (list): list of LogEntry objects
        """
        levels = dict()
        output = list()
        for entry in data:
            if entry.level not in levels.keys():
                levels[entry.level] = [entry]
            else:
                levels[entry.level].append(entry)

        for level, value in levels.items():
            length = 0
            count = len(value)
            for entry in value:
                length += len(entry.message)

            output.append({'level':level, 'Num messages':count, 'Avg length':length/count}) 

        return output
        

class DateAggregator(LogAggregator):
    """
    Subclass of LogAggregator that aggregate log records by date. 
    """
    def aggregate(self, data):
        """
        Aggregates records by Date.  

        Args:
            data (list): list of LogEntry objects
        """
        dates = dict()
        output = list()
        date_pattern = r'[0-9]{4}\-[0-9]{2}-[0-9]{2}'
        for entry in data:
            date = re.search(pattern=date_pattern, string=entry.timestamp).group(0)

            if date not in dates.keys():
                dates[date] = [entry]
            else:
                dates[date].append(entry)

        for date, value in dates.items():
            length = 0
            count = len(value)
            for entry in value:
                length += len(entry.message)

            output.append({'Date':date, 'Num messages':count, 'Avg length':length/count}) 

        return output


class ModuleAggregator(LogAggregator):
    """
    Subclass of LogAggregator that aggregate log records by Module. 
    """
    def aggregate(self, data):
        """
        Aggregates records by module.  

        Args:
            data (list): list of LogEntry objects
        """
        modules = dict()
        output = list()
        for entry in data:
            if entry.module not in modules.keys():
                modules[entry.module] = [entry]
            else:
                modules[entry.module].append(entry)

        for module, value in modules.items():
            length = 0
            count = len(value)
            for entry in value:
                length += len(entry.message)

            output.append({'Module':module, 'Num messages':count, 'Avg length':length/count}) 

        return output