'''Warmup 3: I have a huge list that I need to filter values from. Here is a placeholder function'''

def filter_values(lst, x):
	pass

#here is our huge_list
from random import randint

huge_list = [randint(25) for counter in range(1,100)]

'''When I call the function, I want all values below x to be removed from the list. So if x is 5, I want all numbers below 5 to be removed from the list'''

filtered_list = filter_values(huge_list, 20)
print(filtered_list)#no numbers below 20 should exist in this list