import random

'''
#01. Print Hello World

print("Hello World")
'''

'''#02. Add two number

x = 2+5
print(x)
'''

'''
#03. Check if a number is odd or even
numbers = [1,2,3,4,5,6,7,8,9,10]
y = int(input("Ingrese un número del 1 al 10:"))

if y % 2 == 0:
    print("E número",y,"es par")
else:
    print("El número",y,"es impar")
'''

'''
#04. Find the largest of three numbers

x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo número: '))
z = int(input('Ingrese el tercer número: '))

options = [x,y,z]

print('El número más grande es:',max(options))
'''

'''
#05. Swap 2 variables

first = 'arrow'
second = 25

first, second = second, first

print('First:',first,' y Second:',second)
print(type(first),type(second))
'''

'''
#06. Convert Celsius to Fahrenheit

celsius = int(input('Ingrese temperatura en Celsius: '))

Farenheit = 32 + ((9/5)*celsius)

print('la temperatura en Farenheit es:',Farenheit,'°F')
'''

'''
#07. Calculate the factorial of a number (loop)
y = 0 
x = int(input('Ingresa un número entero, plis: '))
z=x
y=z
while z != 1:
    y = (z-1)
    z=z-1
print('El factorial de',x,'es',y)
'''

'''
#08. Use a for loop to sum numbers in a list
list = []
add_num = 'y'
while add_num == 'y':
    value = int(input('Ingrese un número para la lista: '))
    list.append(value)
    add_num = input('¿Quieres agregar mas numeros? (y/n) ')

print('La suma de los valores es:',sum(list))
'''

'''
#09. Check if a string is a palindrome
string = 'mama'
string_no_space = string.replace(" ","")
string_lower = string_no_space.lower()
#print(list(string_lower))
#print(list(string_lower[::-1]))
if list(string_lower) == list(string_lower[::-1]):
    print('Es un palíndromo :)')
else:
    print('No es un palíndromo :c')
'''

'''
#10. Count vowels in a string
vowels = ['a','e','i','o','u']
string = 'Sabe a caramelo. Escribe LULO CON MAYUSCULA'
string_lower = string.lower()
counter = 0
for character in string_lower:
    if character in vowels:
        counter = counter + 1

print('Hay',counter,'vocales')
'''

'''
#11. Reverse a list
listation = [1,2,'abc',0.5]
print(listation)
print(listation[::-1])
'''

'''
#12. Find the lenght- of a string without len()
string = 'Hijo de la gran'
counter = 0
print(list(string))
for letter in string:
    counter = counter +1
print('La palabra tiene',counter,'letras.')
'''

'''
#13. Use a while loop to print numbers 1 to 10
amount = 1
while amount < 11:
    print(amount)
    amount = amount + 1
'''

'''
#14. Create a simple calculator using if statements
def calculator():
    open_calculator='y'
    while open_calculator == 'y':
        operation = input('What operation do you want? (Add, Subtract, Multiply, Divide): ')
        if operation.lower() == 'add':
            x=int((input('Ingrese el primer número:')))
            y=int((input('Ingrese el segundo número:')))
            result = x + y
            print('The result is:',result,'\nDo you wish to do another operation?',)
        if operation.lower() == 'subtract':
            x=int((input('Ingrese el primer número:')))
            y=int((input('Ingrese el segundo número:')))
            result = x - y
            print('The result is:',result,'\nDo you wish to do another operation?',)
        if operation.lower() == 'multiply':
            x=int((input('Ingrese el primer número:')))
            y=int((input('Ingrese el segundo número:')))
            result = x * y
            print('The result is:',result,'\nDo you wish to do another operation?',)
        if operation.lower() == 'divide':
            x=int((input('Ingrese el primer número:')))
            y=int((input('Ingrese el segundo número:')))
            result = x / y
            print('The result is:',result,'\nDo you wish to do another operation?',)
        open_calculator=input('y/n ')
#calculator()
'''

'''
def calculator_2():
    open_calculator='y'
    operators = ['+', '*', '/', '-']
    while open_calculator == 'y':
        operation = input('Escriba la operación a realizar: ')
        print(list(operation))
        for symbol in operators:
            if symbol in list(operation):
                after_operator = operation.index(symbol)+1 #Posicion donde comienza el segundo numero
                if symbol == '+':
                    print(int(operation[0:operation.index(symbol):1])+int(operation[after_operator::1]))
                if symbol == '-':
                    print(int(operation[0:operation.index(symbol):1])-int(operation[after_operator::1]))
                if symbol == '/':
                    print(int(operation[0:operation.index(symbol):1])/int(operation[after_operator::1]))
                if symbol == '*':
                    print(int(operation[0:operation.index(symbol):1])*int(operation[after_operator::1]))
        open_calculator=input('¿Continuar? y/n ')
calculator_2()
'''

'''
#15. Use input() to get user input and print it
string = input('Escribe un texto aquí: ')
print(f'¡Excelente! Has escrito: "{string}"')
'''

'''
#16. Print a multiplication table (1 to 10)
factors = list(range(1,11))
iterador = iter(factors)
print(factors)
for factor in factors:
    table = []
    for factor_2 in factors:
        multiple = (factor * factor_2)
        table.append(multiple)
    print(f'La tabla del {factor} es {table}')
'''

'''
#17. Use a list comprehension to square number
numbers = list(range(1,11))
print(numbers)
number_squared = [a**3 for a in numbers if a%2==0]
print(number_squared)
'''

'''
#18. Create and access dictionary values
dictionary = {'person':'Juan','age':30,'job':'Accountant','salary':1800}
#print(dictionary.keys()) #Llaves
#print(dictionary.values()) #Valores
#print(dictionary.items()) #Todo

print(f'La persona {dictionary['person']} tiene {dictionary['age']} años')
'''

'''
#19. Use Try-except block for division by zero
a = 15
b = int(input('Ingrese el divisor: '))
try:
    print(a/b)
except ZeroDivisionError:
    print('No se puede dividir entre cero. Fuck you')
'''

'''
#20.Write and call a simple function
def calling():
    print('Calling... \nfuck you')
calling()
'''