from sql import sql_fxn
import csv
import time

class roster:
    def __init__(self, fn):
        self.fn = fn

    def import_list(self):
        arr = []
        skip = True
        with open(self.fn, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if skip:
                    skip = False
                else:
                    row[0] = int(row[0])
                    row = row[:len(row)-2]
                    tm = int(time.time())
                    row.append(tm)
                    arr.append(tuple(row))
        #print(arr)
        return arr

    def insert_list(self):
        arr = self.import_list()
        db = sql_fxn("MailDB.db")
        db.check_out_all()
        check = db.update_roster(arr)
        db.close()
        return check

r = roster('test.csv')
#r.import_list()
r.insert_list()
