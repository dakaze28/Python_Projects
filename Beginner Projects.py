#09. Check if a string is a palindrome
string = 'Harto me tiene'
string_no_space = string.replace(" ","")
string_lower = string_no_space.lower()
#print(list(string))
#print(list(string[::-1]))
longitud = len(string_lower)
media_longitud = int(longitud/2)
inv_media_longitud = media_longitud - 1

if longitud % 2 == 0:
    print(list(string_lower[0:media_longitud:1]))
    print(list(string_lower[-1:inv_media_longitud:-1]))
    if list(string_lower[0:media_longitud:1]) == list(string_lower[-1:inv_media_longitud:-1]):
        print('Es un palíndromo :)')
    else:
        print('No es un palíndromo :c')
else:
    print('Otra manera:')
    print(list(string_lower[0:media_longitud:1]))
    print(list(string_lower[-1:media_longitud:-1]))
    if list(string_lower[0:media_longitud:1]) == list(string_lower[-1:media_longitud:-1]):
        print('Es un palíndromo :)')
    else:
        print('No es un palíndromo :c')