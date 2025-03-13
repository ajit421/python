chai= "masala chai"
Quantity=2

list = [chai, Quantity]
print(repr(list))  # Output: "['masala chai', 2]"

order = "I have ordered {} cups of {} chai"
print (order) # Output: 'I have ordered {} cups of {} chai'

print(order.format(Quantity, chai))  # Output: 'I have ordered 2 cups of masala chai'


