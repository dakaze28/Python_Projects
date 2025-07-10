import math

'''
#21. Print numbers from 1 to 100 using a loop
x=1
while x <101:
    print(x)
    x = x+1
'''

'''
#22. Check if a character is a vowel or a consonant
vowels = ['a','e','i','o','u']
character = input('Ingrese una letra:')
if character in vowels:
    print(f'La letra {character} es vocal.')
else:
    print(f'La letra {character} es consonante.')
'''

'''
#23. Calculate the area of a circle given a radius
radius = 9
pi = math.pi
area = (radius**2)*pi

print(f'The area of the circle is {round(area,2)}.')
'''
'''
#24. Create a list and append user input to it
stop_wordlist='y'
wordlist = []
while stop_wordlist=='y':
    new_string = input('Ingrese una palabra: ')
    wordlist.append(new_string)
    stop_wordlist=input('¿Quieres agregar otra palabra?')
print('Las palabras que anotaste fueron',wordlist)
'''
'''
#25. Remove an element from a list by value
number_list=[1,2,4,5,6,7,8,9,10]
print(number_list)
number_list.remove(6)
print(number_list)
'''
'''
#26. Create a tuple and acces elements by index
numbers_tuple = (1,'abuela',3,'primo',5,'tía',7,8.99,9)
print(numbers_tuple[7])
'''
'''
#27. Check if an element exists in a list
value = 10
wordlist = ['abuela',1,25,'hola',True]
if value in wordlist:
    print(f'El valor {value} está dentro de la lista')
else:
    print(f'El valor {value} NO SE ENCUENTRA dentro de la lista')
'''
'''
#28. Count the number of times a value appears in a list
value = 2
wordlist = [1,1,1,1,2,2,2,3,4,5,1,6,87,2,4,1,1,90]
print(f'El valor {value} aparece {wordlist.count(value)} veces')
'''
'''
#29. Sort a list in ascending and descending order
wordlist = [1,24,34,100,2,76,8,19]
wordlist.sort()
print(wordlist)
wordlist.sort(reverse=True)
print(wordlist)
'''
'''
#30. Use range() to create a list of numbers
numbers = list(range(2,101,2))
print(numbers)
'''
'''
#31. Use break to exit a loop early
numbers = list(range(1,101))
new_list=[]
for number in numbers:
    new_list.append(number)
    print(new_list)
    if number == 50:
        break
'''
'''
#32. Use continue to skip an iteration in a loop
numbers = list(range(1,21))
new_list=[]
for number in numbers:
    if number%2 == 1: #Todos los números pares, saltarlos
        continue
    new_list.append(number)
    print(new_list)
'''
'''
#33. Create a nested list and access elements
matrix = [['abuelo',    'abuela',   'abuele'],
          ['mama',      'papa',     'tio'],
          ['hermano',   'hermana',  'primo']]
pariente = matrix[1][0]
print(f'El pariente que escogiste es {pariente}')
'''
'''
#34. Concatenate two strings
string_1='Este es el primero'
string_2=' y este es el segundo.'
print(string_1+string_2)
'''
'''
#35. Use isalpha() and isdigit() on a string
string_1='Palabra'
print(string_1.isalpha())
print(string_1.isdigit())
'''
'''
#36. Write a function that returns the square of a number
def square():
    number=int(input('Ingrese un número entero: '))
    print(f'El cuadrado de {number} es {number**2}.')

square()
'''
'''
#37. Convert a string to uppercase and lowercase
string_1='Este es un texto básico'
print(string_1)
print(string_1.upper())
print(string_1.lower())
'''
'''
#38. Create a simple menu using if-else-elif
print('Escoge una de las siguientes opciones \n 1. Tomar agua \n 2. Comer comida \n 3. Dormir \n 4. Sorpresa')
user_input=int(input('Opción:'))
if user_input==1:
    print('Has tomado agua. ¡Qué bien por ti!')
elif user_input==2:
    print('Has comido comida. ¡Qué bien por ti!')
elif user_input==3:
    print('Larga a dormir, jooooo.')
else:
    print('Fuck you .|.')
'''
'''
#39. Use a dictionary to store and retrieve contact names and numbers
contact_table = []
contact_dict = {'name':'Andres','contact':88998022}
contact_table.append(contact_dict)
contact_dict = {'name':'Pablo','contact':78663322}
contact_table.append(contact_dict)
contact_dict = {'name':'Carlos','contact':27273838}
contact_table.append(contact_dict)
print(contact_table)
'''
'''
#40. Count down from 10 to 1 using a loop
x = 10
while x>0:
    print(x)
    x = x-1
print('Congratulations!')
'''
