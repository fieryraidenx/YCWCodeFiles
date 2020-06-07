'''Warmup 1: Fix the errors with these loops'''

#Exercise 1-1
c = 0
#this prints out all the numbers from 1-10!
while c < 10:
	print(c)


#Exercise 1-2
listexample = ["1", "2", "3", "4", "5"]
#this prints out all the numbers in listexample
for i in listexample:
	print(listexample[i])


#Exercise 1-3
listexample = ["1", "2", "3", "4", "5"]
#this prints out the sum of the entire list
total = 0
for i in range(listexample):
	listexample[i] += total
print(total)