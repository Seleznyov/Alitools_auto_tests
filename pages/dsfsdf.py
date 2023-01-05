x = "3 185,55 руб."
price = x.translate({ord(i): None for i in ' руб.$€¥₽US'})
print(price)
price = price.replace(' ', '')
print(price)
price = price.replace(",", ".")
print(price)
print(float(price))