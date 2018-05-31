# users = ['admin', 'lucy', 'larson', 'eric']

log_user = 'admin'

if log_user == 'admin':
	print("Hello " + log_user.title() + ", would you like to see a status report? ")
else:
	print("Hello " + log_user.title() + ", thank you for logging in again.")

users = []

if len(users) == 0:
	print("We need  find some users .")

current_users = ['admin', 'lucy', 'larson', 'eric', 'tome']
new_users = ['tom', 'Lucy', 'larson', 'nelson', 'wilson']

for each_user in new_users:
	if each_user.lower() in current_users:
		print("Sorry, user name " + each_user + " is alread be used , please change others.")
	else:
		print("The user name " + each_user + " can be used.")

# 5-11 序数

numbers = [values for values in range(1, 10)]
print(numbers)

for each_number in numbers:
	if each_number == 1:
		print("\n" + str(each_number)+"st")
	elif each_number == 2:
		print("\n" + str(each_number) + "nd")
	elif each_number == 3:
		print("\n" + str(each_number) + "rd")
	else:
		print("\n" + str(each_number) + "th")



