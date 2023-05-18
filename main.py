stonks_book = {
  "JPM": "33.33",
  "AAPL": "45.40",
  "ABBV": "17.20",
  "FENC": "31.11",
  "ESRT": "12.80",
  "ESTE": "14.71",
  "HBAN": "20.05",
  "KMDA": "64.30",
  "MOXC": "15.90",
  "MLSS": "8.34.00",
  "REGN": "20.20"
}
x = input('Enter Ticker Symbol Here: ')
z =stonks_book.get(x,'No Stonks. Ticker not found.')
print(z)