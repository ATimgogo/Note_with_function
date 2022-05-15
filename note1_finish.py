import os  #os是operating system的縮寫
notes = []
def read_file(filename):

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "商品名稱, 價格" in line:
                continue
            name, price, quantity = line.strip().split(",")
            notes.append([name, price, quantity])

    return notes

def user_input(notes):
    while True:
        name = input("請輸入商品名稱:")
        if name == "q":
            break
        price = input("請輸入商品價格:") 
        price = int(price)
        quantity = input("請輸入商品數量:")
        quantity = int(quantity)
        notes.append([name, price, quantity])
    return notes
def print_notes(notes):
    for i in notes:
        print(i[0], "數量為:", i[2], "價格為:", i[1]) 
def write_file(filename, notes):
    with open("notes.csv", "w", encoding="utf-8") as f:
        f.write("商品名稱, 價格, 數量" + "\n")
        for i in notes:
           f.write(i[0] + "," + str(i[1]) + "," + str(i[2]) +"\n")


def main():
    filename = "notes.csv"
    if os.path.isfile(filename):
        print("找到檔案")   
        notes = read_file(filename)
    else:
        print("找不到檔案!!") 
        notes = []   #此處沒加，會出錯。由於全域變數與區域變數的觀念
    notes = user_input(notes)
    print_notes(notes)
    write_file("notes.csv", notes)



main()


