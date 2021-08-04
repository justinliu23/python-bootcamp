name = 'Josh'
if name == 'Rob':
  print('Match - Rob')
elif name == 'Matthew':
  print('Match - Matthew')
elif name == 'Josh':
  print('Match - Josh')
else:
  print('Not a match')

# finding the sum of the sequence, [1, 2, 3, ... , 100]
count, i = 0, 1
while i <= 100:
	count = count + i
	i = i + 1
print(count)

# the below code does the exact same thing as the previous while loop, just with a for loop
count = 0
for i in range(101):
  # count += i is the same as count = count + i
  count += i
print(count)

# prints out all the even numbers in [0, 9]
for i in range(0, 10, 2):
    print(i)

# prints out numbers in descending order (with a step size of 1), starting from 5 and ending at 0
for i in range(5, 0, -1):
    print(i)

# print 5 random numbers that can range from 1 to 10
import random
for i in range(5):
    print(random.randint(1, 10))

# terminates the program
import sys
sys.exit()
