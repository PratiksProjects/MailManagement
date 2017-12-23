#!/usr/bin/python
import sqlite3
from sqlite3 import Error

def connect_db(file_name):
    try:
        conn = sqlite3.connect(file_name)
        return conn
    except Error as e:
        print(e)

    return None

def find_all_package_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Packages WHERE BuzzcardNumber=?", (id,))
    return cur.fetchall()

def find_unchecked_packages_by_id(conn,id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Packages WHERE BuzzcardNumber=? AND CheckedOut=0", (id,))
    return cur.fetchall()

def find_current_resident_by_id(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Roster WHERE BuzzcardNumber=? AND CurrentResident=1", (id,))
    return cur.fetchall()
