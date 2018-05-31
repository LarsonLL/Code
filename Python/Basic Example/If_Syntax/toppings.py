requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies !")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now .")
	else:
		print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# confirm the list is not null.

requested_toppings = []

# Python 将再列表至少包含一个元素事返回True，并在列表为空时返回false。
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza ?")


# 处理多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry , we don't have " + requested_topping + '.')

print("\nFinished making your pizza!")


