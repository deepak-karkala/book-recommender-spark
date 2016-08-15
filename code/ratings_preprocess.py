# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:00:54 2016
Map userid, ISBN to integers ranging from 0 to number of distinct users and books.
@author: nesara
"""

import pandas as pd

ratings = pd.read_csv('../BX-CSV-Dump/ratings.csv')

filename = '../BX-CSV-Dump/ratings.csv'

dictWords = []
f = open(filename,"r")
for line in f:
    dictWords.append(line)

userid = 0
bookid = 0
csvfile = open('ratingsProcessed.csv', 'wb')
w = csv.writer(csvfile)
userMap = dict()                        
bookMap = dict()
for i in range(len(dictWords)):
    tmp = dictWords[i].split(';')           
    user = tmp[0]
    if user in userMap:
        usr = userMap[user]
    else:
        usr = userid
        userid = userid+1
        userMap[user] = usr
    book = tmp[1]
    if book in bookMap:
        bk = bookMap[book]
    else:
        bk = bookid
        bookid = bookid+1
        bookMap[book] = bk        
    ratings = int(tmp[2])
    w.writerow([usr,bk,ratings])
    
   
dictWords = []   
fileMain = open(filename, "r")
for line1 in fileMain:
    dictWords.append(line1.encode("utf-8").strip)