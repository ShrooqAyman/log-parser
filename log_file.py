from log_entry import LogEntry
import re

class LogFile:
    """
    Class representing log file.

    Attributes:
        filename (str): string representing the name of log file. 
        entry_lst (list) : list of LogEntry objects.
    """
    def __init__(self, filename):
        """
        Initialize an instance from LogFile class.

        Args:
            filename (str): string representing the name of log file. 
            entry_lst (list) : list of LogEntry objects.
        
        Returns: 
            None.
        """
        self.filename = filename
        self.entry_lst = []

    def read_file(self):
        """
        Read logs from log file and save them as LogEntry objects in list.

        Returns:
            (list) : a list of LogEntry objects
        """
        with open(self.filename, 'r') as file:
            time_pattern = r"[0-9]{4}\-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}"
            module_pattern = r'([a-z]+)'
            level_pattern = r'\b[A-Z]{4,6}'
            message_pattern = r'[A-Z]{1}[a-z].+'

            for line in file:
                line = line.strip()
                try:
                    time = re.search(pattern=time_pattern, string=line).group(0)
                except AttributeError as e:
                    print(f'Error: {e}, timestamp missed')
                    continue
                try:
                    level = re.search(pattern=level_pattern, string=line).group(0)
                except AttributeError as e:
                    print(f'Error: {e}, level missed')
                    continue
                
                try:
                    module = re.search(pattern=module_pattern, string=line).group(0)
                except AttributeError as e:
                    print(f'Error: {e}, module missed')
                    continue

                try:
                    message = re.search(pattern=message_pattern, string=line).group(0)
                except AttributeError as e:
                    print(f'Error: {e}, message missed')
                    continue

                entry = LogEntry(timestamp=time, level=level, module=module, message=message)
                self.entry_lst.append(entry)
        return self.entry_lst

    def show_entry(self):
        for entry in self.entry_lst:
            print(entry)



        