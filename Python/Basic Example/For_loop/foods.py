my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are :")
print(my_foods)

print("\nMy friend's favorite foods are : ")
print(friend_foods)


print("\nThe first three items in the list are : "  )
print(friend_foods[0:3])
print("\nThree items from the middle of the list are:")
print(friend_foods[1:4])
print("\nThe last three items in the list are: ")
print(friend_foods[-3:])

print("\nThe last three items in the list are: ")
for each_item in friend_foods[-3:]:
    print(each_item.title())