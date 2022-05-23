symbols = 'AAPL,IBM,MSFT,YHOO,SCO'

symbols = symbols + ',GOOG'
print(symbols)

symbols = 'HPQ,'+ symbols
print(symbols)

print('IBM' in symbols)

print(symbols.find('MSFT'))

line = 'GOOG,100,490.10'
row = line.split(',')
print(row)
