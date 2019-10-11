
#! usr/bin/env python
# -*- coding: utf-8 -*-
#database test

import sys, time, threading
import sqlite3
import mysql.connector

class DealWithDB:
    def __init__ (self,dbName):
        self.dbName = dbName
        self.dbConnect = ""
        if self.dbName != "":
            self.dbConnect = sqlite3.connect("dealDB01.db")
    def __del__ (self):
        self.dbName = ""
    def getName(self):
        print("method getName")
        return self.dbName
    def isConnected(self):
        self.cursor = self.dbConnect.cursor()

if __name__ =="__main__":
    print(__name__)

    db = DealWithDB("infoDB")
    db.getName()
