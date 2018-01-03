from sql import sql_fxn
import csv

class roster:
    def __init__(self, fn):
        self.fn = fn

    def import_list(self):
        arr = []
        with open(self.fn, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                #print(','.join(row))
                row = row[:len(row)-2]
                arr.append(tuple(row))
        print(arr)
        return arr

    def insert_list(self, arr):
        arr = self.import_list()
        db = sql_fxn()
        return db.update_roster(arr)

r = roster('roster.csv')
r.import_list()
