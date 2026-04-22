#billing system at the supermarket
while True:
    name = input("ENter the customer's name:")
    total = 0
    
    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount:"))
        quantity = float(input("Enter the quantity:"))
        total += amount*quantity
        repeat = input("Do you want to add more items? (yes/no):")
        if repeat == "no" or repeat == "No":
            break
    print("-"*40)
    print("Name",name)
    print("Amount to be paid:",total)
    print("-"*40)
    print("********************Happyyyyyy Shopinnggggg**************************************")
    repeat1= ("Do you wannt to go to next customer (yes/no):")
    if repeat1 == "no" or repeat == "No":
        break