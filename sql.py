#!/usr/bin/python
import sqlite3
from sqlite3 import Error

class sql_fxn:
    def __init__(self, file_name):
        self.conn = self.connect_db(file_name)
        self.cur = self.conn.cursor()

    def connect_db(self,file_name):
        try:
            conn = sqlite3.connect(file_name)
            return conn
        except Error as e:
            print(e)

        return None

    def find_all_package_by_id(self,id):
        self.cur.execute("SELECT * FROM Packages WHERE BuzzcardNumber=?", (id,))
        return cur.fetchall()

    def find_unchecked_packages_by_id(self,id):
        self.cur.execute("""SELECT * FROM Packages WHERE BuzzcardNumber=?
        AND CheckedOut=0""", (id,))

        return cur.fetchall()

    def find_unchecked_packages_by_room(self,conn,room):
        self.cur.execute("""SELECT * FROM Packages WHERE RoomNumber=? AND
        CheckedOut=0""", (id,))
        return cur.fetchall()

    def find_current_resident_by_id(self,conn, id):
        self.cur.execute("""SELECT * FROM Roster WHERE BuzzcardNumber=? AND
        CurrentResident=1""", (id,))
        return cur.fetchall()

    def check_out_all(self):
        check = self.cur.execute("UPDATE Roster SET CurrentResident = 0")
        self.conn.commit()
        return check

    def update_roster(self, arr):
        check = self.cur.executemany("""INSERT OR REPLACE INTO Roster
        ('BuzzcardNumber', 'FirstName', 'LastName', 'RoomNumber', 'Date') VALUES (?, ?, ?, ?, ?)""", arr)
        self.conn.commit()
        return check

    def close(self):
        self.conn.close()
