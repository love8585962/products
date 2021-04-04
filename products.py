products = []  #建立一個名為products的空清單
while True :  #建立無窮迴圈
    name = input("請輸入商品名稱: ")  #讓用戶輸入名稱
    if name == "q" : #輸入q結束迴圈
        break  #停止
    price = input("請輸入商品價格: ") #讓用戶輸入價格
    products.append([name, price]) #新增兩個名為"name","price"的兩個小清單到大清單中

for p in products:
    print(p[0], '的價格是',p[1]) #印出結果