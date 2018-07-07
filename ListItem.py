shopping_list = ['Milk','Bread','Cheese','Bow and Arrow']
print(shopping_list)
print(shopping_list[0])
print(shopping_list[-1]) # it will show the last iteam of the list

if 'Milk' in shopping_list:
    print("Oh good, You rememberd the milk")

supermarket_list = ['Milk', 'Bread', 'Cheese']
wumpus_r_us_list = ['Bow and Arrow', 'Lantern', 'Wumpus B Gone']
my_shopping_lists = [supermarket_list,wumpus_r_us_list]

# if i forget to add an item to the list we can add this process
wumpus_r_us_list.append('Rope')
print(wumpus_r_us_list)

# we can remove item from the list also
wumpus_r_us_list.remove('Wumpus B Gone')
print(wumpus_r_us_list)

# how to select first three from the wumpus_list
first_three = wumpus_r_us_list[0:3]
print(first_three)

# how to select last three item from the wumpus_list
last_three = wumpus_r_us_list[-3:]
print(last_three)
