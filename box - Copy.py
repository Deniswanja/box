# Define our function
operation= input('''
Please 
* for multiplication
''')
num1= int(input("enter the height of big box: "))
num2= int(input("enter the height of Small box: "))
num3= int(input("enter the height of your books: "))
num4=int(input("enter number of books ordered:"))
print('{} * {} / {}= '.format(num3, num4, num1))
print(num3 * num4 / num1)
