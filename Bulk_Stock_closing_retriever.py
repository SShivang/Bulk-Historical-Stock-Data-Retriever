import pandas_datareader as pdr
from datetime import datetime
f = open("C:/S&P500.txt", 'r')
SP500 = [' ']
import csv
myfile = open("C:/S&P500.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

for line in f.readlines():
    SP500.append(line)

#rows = []

for symbol in SP500:
    symbol = symbol[:-1]
    stock = pdr.get_data_yahoo(symbols=symbol, start=datetime(2012, 5, 1), end=datetime(2017, 5, 1))
    row = stock['Adj Close']
    rows = zip(rows, wr.writerow(stock['Adj Close']))

 
stock = ""

for symbol in SP500:
    symbol = symbol[:-1]
    stock = stock + "," + "\"" + symbol +  "\""

print stock



f.close()
