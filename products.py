from asyncio.proactor_events import _ProactorDuplexPipeTransport


products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price]) #  p = []     p.append(name)    p.append(price)    products.append(p)
print(products)

products[0][0]