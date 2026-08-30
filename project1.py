

def menu():
    print("###_QuickBite Menu_###")
    print("1.Burger -60" )
    print("2.Pizza - 160")
    print("3.Pasta -80")
    print("4.noodles -90")
    print("5.cold coffee -100")

name = input("enter your name: ")
print("\nwelcome", name)
menu()
choice=int(input("enter your choice(1-5)"))
quantity=int(input("enter quantity"))


if choice == 1:
    item = "burger"
    price = 60
elif choice == 2:
    item = "Pizza"
    price = 160
elif choice == 3:
    item = "Pasta"
    price = 80
elif choice == 4:
    item = "noodles"
    price = 100
elif choice == 5:
    item = "Cold coffee"
    price = 100
else:
    print("choice not available")
    price = 0

print("__Checkout Details__")
print("item:",item)
print("quntity:",quantity)

bill = price*quantity
print("your total bill:",bill)
print("thankyou for your purchase")

