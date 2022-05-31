import csv

file = r'C:\Users\julia\OneDrive\School\OS3\Python\practical-python-master\Work\Data\prices.csv'

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

print(read_prices(file))