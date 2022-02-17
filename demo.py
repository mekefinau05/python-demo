first_name = 'Meke'
print(first_name)

last_name = "Finau"
print(last_name )

# print(f"Hello, {first_name}.")

age = 29 #int
bank_account = 540.55 #float
loves_code = True #boolean

# age = 'twenty nine'
# print(age)
# print(type(age))

# if age >=18:
#   print('I am an adult!')
# elif age >=13:
#       print('I am a teen')
# else: 
#   print('I am a child.')
  
numbers = [1,2,3,4,5,6,7,8,9,10]

# for idx, val in enumerate(numbers):     #loops around the whole array
      # print(idx, val)

# for number in numbers:
#   print(number)
  
if age <= 21 and first_name == 'Meke':
    print('Yes!')
    
my_cats = ['Jake', 'buddy', 'gogi', 'macy']

for cat in my_cats:
      print(cat.capitalize())
      
print(len(my_cats))      #length of the array


      
open_file = open('FinalGrades.csv')

open.file.seek(0,0)      #to restart every loop, use it after every loop

# for row in open_file:
#       print(row)
      
# for row in open_file:
#       split = row.split(',')
#       for value in split:
#             if value.startswith('R'):
#                   print(value)
                  
total_a = 0
total_b = 0
total_c = 0

for row in open_file:
  item = row.rstrip('\n').split(',')
  for value in item:
    if value == 'A':
      total_a += 1
    elif value == 'B':
      total_b += 1
    elif value == 'C':
      total_c += 1    
      
print("A's:", total_a)
print("B's:", total_b)
print("C's:", total_c)          

      
open_file.close()
  
  
    