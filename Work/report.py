# report.py
#
# Exercise 2.4
import csv

f = r'C:\Users\julia\OneDrive\School\OS3\Python\practical-python-master\Work\Data\portfolio.csv'

def read_portfoliolist(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    total = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        for name, shares, price in portfolio:
            total += shares*price
    return portfolio, total

def read_portfoliolistdict(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    total = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name'  :   row[0],
                'shares':   int(row[1]),
                'cost'  :   float(row[2])
            }
            portfolio.append(stock)

    return portfolio

#print(read_portfoliolist(f))
print(read_portfoliolistdict(f))

