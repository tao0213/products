products = []
while True:
	name = input('請輸入商品名稱： ')
	if bame == 'q':
		break
	price = input('請輸入商品價格： ')
	p = [name, price]
	products.append(name)
print(products)