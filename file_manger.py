from abc import ABC, abstractmethod
import csv, json

class FileManger(ABC):
    """
    Abstract class representing a file manager.
    """
    @abstractmethod
    def save(self, data):
        """
        Abstract method that saves data to a file.
        
        Args:
            data: the data to be saved.
            filename: the name of the file to save the data to.
        """
        pass

class CSVFileManger(FileManger):
    """
    Class representing a file manager for CSV files.
    """
    def save(self, data, filename):
        """
        Saves the data to a CSV file.
        
        Args:
            data: the data to be saved.
            filename: the name of the CSV file to save the data to.
        """
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

            # Write the header row
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        

class JSONFileManger(FileManger):
    """
    Class representing a file manager for CSV files.
    """
    def save(self, data, filename):
        """
        Saves the data to a json file.
        
        Args:
            data: the data to be saved.
            filename: the name of the json file to save the data to.
        """
        with open(filename, 'w') as json_file:
            json.dump(data,json_file )

class TXTFileManger(FileManger):
    """
    Class representing a file manager for txt files.
    """
    def save(self, data, filename):
        """
        Saves the data to a json file.
        
        Args:
            data: the data to be saved.
            filename: the name of the json file to save the data to.
        """
        with open(filename, 'w') as txt_file: 
            for dic in data:
                for key, value in dic.items(): 
                    txt_file.write('%s:%s\n' % (key, value))