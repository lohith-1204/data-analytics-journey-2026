# External Libraries - QR Code & Currency Converter

# QR Code Generator

import qrcode

data = "https://github.com/lohith-1204/Python"  # your link

qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR Code generated successfully!")

# Currency Converter

from currency_converter import CurrencyConverter

c = CurrencyConverter()

amount = 100  # USD
converted = c.convert(amount, 'USD', 'INR')

print("\nCurrency Conversion:")
print(f"{amount} USD = {converted:.2f} INR")