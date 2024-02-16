#These global variables define our order quantity
coffee_order=int(input('How Many Coffees? \n'))
muffin_order=int(input('How Many Muffins? \n'))

#This function initializes the order by printing the responses to our input variables
def order():
    print('My Coffee and Muffin Shop')
    print('Number of Coffees bought?\n',coffee_order)
    print('Number of muffins bought? \n',muffin_order)
    
#This function uses math operators to find the prices and total for the order including the tax and prints it all in a neat receipt
def receipt():
    COFFEE_PRICE=(5)
    MUFFIN_PRICE=(4)
    TAX=.06
    coffee_subtotal=coffee_order*COFFEE_PRICE
    muffin_subtotal=muffin_order*MUFFIN_PRICE
    subtotal=coffee_subtotal+muffin_subtotal
    tax_amount=subtotal*TAX
    total=subtotal+tax_amount
    print('My Coffee and Muffin Shop')
    print(coffee_order,'Coffee at $',COFFEE_PRICE,'each: $',coffee_subtotal)
    print(muffin_order,'muffin at $',MUFFIN_PRICE,'each: $',muffin_subtotal)
    print('6% tax: $',tax_amount)
    print('---------')
    print('total: $',total)
    
#This function is simply for the * symbol that are shown within the sections.
def ornament():
    print('*'*39)

#This main function calls all other functions to print an order sheet and a receipt displaying total price
def main():
    ornament()
    order()
    ornament()
    print()
    ornament()
    receipt()
    ornament()
    
main()
