"""
get number_of_items
total_price = 0
for i in range(number_of_items)
    get price
    total_price += price
if total_price > 100 ..... not including
    total *= 0.9
display message with total.

note, along with the error checking I was told to add, another system can be used to ensure all items are not less than 0
This is handled the same way that the number of items was handled, but this time inside the for loop.
"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
