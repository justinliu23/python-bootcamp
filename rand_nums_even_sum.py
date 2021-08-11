# Workshop 4 Practice Problem 1
import random

list_of_nums = []
for i in range(10):
  random_num = random.randint(1, 10)
  list_of_nums.append(random_num)

sum = 0
for num in list_of_nums:
  if num % 2 == 0:
    sum += num

print('Our random generated list:', list_of_nums)
print('Sum:', sum)