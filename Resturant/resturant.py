menu = {
    'Pizza':480,
    'Burger':210,
    'Pasta':80,
    'Salad':120,
    'Fried rice':70,
    'Coffee':60,
}

#Greeting message
print("Welcome to Tech cafe")
print('Pizza:480,\nBurger:210,\nPasta:80,\nSalad:120,\nFried rice:70,\nCoffee:60')

total_order =0

item_1 =input('Enter the name of the item you want to order =')
if item_1 in menu:
    total_order+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item is not available at the time !")

another_item = input("Do you like to order something extra? (yes/no)")
if another_item=="yes":
    item_2 = input("Enter the name of the extra item you want to order !")
    if item_2 in menu:
       total_order+=menu[item_2]
       print(f"Item {item_2} has been added to your order")
    else:
        print(f"The ordered item is not available at a time")

print(f"The total number of item to pay is {total_order}")