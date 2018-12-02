###  Allen Klus  ###
###  CIS 111     ###
###  9/6/18      ###
###  Volume calc ###



### Input/Output ###


print('This program calculates the volume discounts')

print('\n')

id = input('Enter the item\'s ID: ')

price = float(input('Enter the item\'s price: '))

quantity = float(input('How many did you buy: '))


### Calculations ###

subtotal = price * quantity



if quantity < 144:
    discount = 0
    
if quantity >= 144 and quantity <= 999:
    discount = (10 * subtotal) / 100.0
    
if quantity >= 1000:
    discount = (20 * subtotal) / 100.0


### Outputting the receipt ###
print('\n')

print('Subtotal: {0:>10,.2f}'.format(subtotal))
print('Discount: {0:>10,.2f}'.format(discount))

total = subtotal - discount

print('{0:>20}'.format('-------'))

print('Total: {0:>13,.2f}'.format(total))

print('\n')


input('Press any key to exit')



