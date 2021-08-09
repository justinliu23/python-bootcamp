def hello(name):
  print('Hello, ' + name)

hello('Matthew')
# doesn't work, name is only in local scope of the function, hello()
# print(name)

def get_sum(num1, num2):
  return num1 + num2

sum = get_sum(2, 7)
print(sum)

my_list = ['rat', 'bat', 'cat', 'elephant']

for i in range(5):
  print(i)

for i in range(len(my_list)):
  print(my_list[i])

for i in range(0, len(my_list), 2):
  print(my_list[i])

# remember that "item" is a local variable in the context of only this specific for loop; likewise for functions
for item in my_list:
  print(item)

print(my_list[::-1])

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
  print('Index ' + str(index) + ' in supplies is: ' + item)

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)


my_list[0] = 'giraffe'
print(my_list)

# throws an error because strings are tuples, which are immutable
# my_string = 'giraffe'
# my_string[0] = 'j'
# print(my_string)

num = 4
num *= num
# same as num = num * num
print(num)