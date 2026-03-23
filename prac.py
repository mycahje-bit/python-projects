order = []


def addOrder(item, price, quantity, total):
    order.append((item, price, quantity, total))


def showOrder():

    for item, price, quantity, total in order:
        print(f"Item: {item} | Price: {price} | Quantity: {quantity} | Total: {total}")
        print("-------------------------------------------------------")

while True:

    item = input("Enter order: ").lower()

    if item == "done":
        print("Transaction done")
        break;
    
    while True:
        try: 
            price = int(input("Enter price: "))
            quan = int(input("Input quantity: "))
            total = price * quan
            break
        except ValueError:
            print("!! Enter a valid number !!")
            continue

    addOrder(item, price, quan, total)

    print("===")
    print("-- item added -- ")
    print()
    


showOrder()
