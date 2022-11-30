# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:28:01 2022

@author: Crystal
"""
import sqlite3

connection = sqlite3.connect('ffff.db')

cursor = connection.cursor()

query =("ALTER TABLE product DROP COLUMN sku")

cursor.execute(query)

connection.commit()
connection.close()