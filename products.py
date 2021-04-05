import os

#讀取檔案
def read_file(file_name):
    products = []  #建立一個名為products的空清單
    with open(file_name,"r", encoding = "utf-8") as file :
        for line in file :
            if "商品,價格" in line :
                continue #繼續
            name, price = line.strip().split(",") #先移除\n 再切割 ","
            products.append([name, price])   #將商品跟價格加入 products這個大清單中
    return products  #返回products的值


#讓使用者輸入
def user_input(products) :
    while True :  #建立無窮迴圈
        name = input("請輸入商品名稱: ")  #讓用戶輸入名稱
        if name == "q" : #輸入q結束迴圈
            break  #停止
        price = input("請輸入商品價格: ") #讓用戶輸入價格
        price = int(price)
        products.append([name, price]) #新增兩個名為"name","price"的兩個小清單到大清單中
    print(products)
    return products


#印出購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是',p[1]) #印出結果


#寫入檔案
def write_file(file_name, products) :
    with open(file_name, "w", encoding = "utf-8") as file :
        file.write("商品,價格\n")
        for p in products:
            file.write(str(p[0]) + "," + str(p[1]) + "\n")


def main():
    file_name = 'products.csv'
    if os.path.isfile(file_name): #檢查檔案在不在
        print("已找到檔案")
        products = read_file(file_name)
    else :
        print("找不到檔案.. ,重新建立清單")
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()