shopping_list = ['Milk','Bread','Cheese','Bow and Arrow']
print(shopping_list)
print(shopping_list[0])
print(shopping_list[-1]) # it will show the last iteam of the list

if 'Milk' in shopping_list:
    print("Oh good, You rememberd the milk")

supermarket_list = ['Milk', 'Bread', 'Cheese']
wumpus_r_us_list = ['Bow and Arrow', 'Lantern', 'Wumpus B Gone']
my_shopping_lists = [supermarket_list,wumpus_r_us_list]

#for loops in python
print "Wumpus hunting checklist:"
for each_item in wumpus_r_us_list:
    print(each_item)
    if each_item == "Lantern":
        print("Don't Forget to light your Lantern")
        print("once you are down there")
