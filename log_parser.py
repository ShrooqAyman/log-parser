from log_file import LogFile
from log_entry import LogEntry
from filter_strategy import FilterContext
from log_filter import LevelFilter, DataRangeFilter, ModuleFilter
from agg_strategy import AggregateContext
from file_strategy import SaveContext
from log_agg import ModuleAggregator, LevelAggregator, DateAggregator
from file_manger import CSVFileManger, JSONFileManger, TXTFileManger
from constants import CSV_FILE_NAME, JSON_FILE_NAME, TXT_FILE_NAME
import argparse

class LogParser:

    def __init__(self, file_name):
        self.log_file = LogFile(filename=file_name)
        self.log_file_content = self.log_file.read_file()
        self.filter = FilterContext(LevelFilter())
        self.aggregate = AggregateContext(ModuleAggregator())
        self.output = self.log_file_content
        self.save = SaveContext(CSVFileManger())

    def filter_log(self, strategy, context):
        self.filter.set_strategy(strategy)
      
        self.output = self.filter.filter(self.output, context=context)
        return self.output
    
    def agg_log(self, strategy):
        self.aggregate.set_strategy(strategy)
        self.output = self.aggregate.aggregate(self.output)
      

    def save_output(self, strategy, filename):
        self.save.set_strategy(strategy)
        if len(self.output) > 0:
            if isinstance(self.output[0], LogEntry):
                results = []
                for entry in self.output:
                    results.append({'timestamp':entry.timestamp, 'level':entry.level, 'module':entry.module, 'message':entry.message})
                self.output = results
            self.save.save(self.output, filename)
        
# command line parser
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', type=str, help='server logs file name')
parser.add_argument('-o', '--output', type=str, help='output file type')
parser.add_argument('-l', '--level', type=str, help='filter by level')
parser.add_argument('-m', '--module', type=str, help='filter by module')
parser.add_argument('-d', '--date', nargs=2, type=str, help='filter by date')
parser.add_argument('-a', '--aggregate', type=str, help='aggregation')

args = parser.parse_args()
try:
    if args.file:
        log_parser = LogParser(args.file)
        if args.level :
            log_parser.filter_log(LevelFilter(), context=args.level)

        if args.module :
            log_parser.filter_log(ModuleFilter(), context=args.module)

        if args.date :
            context = {'date1':args.date[0], 'date2':args.date[1]}
            log_parser.filter_log(DataRangeFilter(), context=context)

        if args.aggregate == 'level':
            log_parser.agg_log(LevelAggregator())

        if args.aggregate == 'module':
            log_parser.agg_log(ModuleAggregator())
        
        if args.aggregate == 'date':
            log_parser.agg_log(DateAggregator())

        if args.output == 'csv':
            log_parser.save_output(CSVFileManger(), CSV_FILE_NAME)

        elif args.output == 'json':
            log_parser.save_output(JSONFileManger(), JSON_FILE_NAME)
        
        elif args.output == 'txt':
            log_parser.save_output(TXTFileManger(), TXT_FILE_NAME)
            
    else:
        parser.print_help()
except Exception as e:
    print(f'Error: {e}')



