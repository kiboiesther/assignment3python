# question one
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        return price * 20/100
    else:
        return price
discounted_price =calculate_discount(200,30)
print(discounted_price)

#question two
def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        return price * 20/100
    else:
        return price
price = int(input("enter the original price: "))
discount_percent = int(input("enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)
if final_price != price:
     print(f"the final price is: {final_price}")
else:
    print(f"no discount applied. the price is {price}")