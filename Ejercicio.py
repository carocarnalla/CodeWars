#Ejercicio suma de array
#ubhnkjmlubnkjml
#ubnkjmkl
'''
print('Hello GitHub')

  cambio=[('1','0'),('2','0'),('3','0'),('4','0'),('5','1'),('6','1'),('7','1'),('8','1'),('9','1')]

print('Hello GitHub blabla')
'''
#Fake Binary
#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
#Note: input will never be an empty string

'''
def fake_bin(x):
    nuevo=x.replace('1','0')
    nuevo=nuevo.replace('2','0')
    nuevo=nuevo.replace('3','0')
    nuevo=nuevo.replace('4','0')
    nuevo=nuevo.replace('5','1')
    nuevo=nuevo.replace('6','1')
    nuevo=nuevo.replace('7','1')
    nuevo=nuevo.replace('8','1')
    nuevo=nuevo.replace('9','1')
    return nuevo
'''
#La mejor solución
'''
def fake_bin(x):
    print( ''.join('0' if c < '5' else '1' for c in x))

fake_bin('91919191')
'''


#Sum Mixed Array
#Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#Return your answer as a number.

'''
def sum_mix(arr):
    sum=0
    for i in arr:
        sum=sum+i
    print(sum)


sum_mix(9,1)


def sum_mix(arr):
    sum = 0
    for num in arr:
        sum += int(num)
    return sum

sum_mix(9,1)



test.assert_equals(sum_mix([9, 3, '7', '3']), 22)
        test.assert_equals(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42)
        test.assert_equals(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41)
        test.assert_equals(sum_mix(['1', '5', '8', 8, 9, 9, 2, '3']), 45)
        test.assert_equals(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)'''

#Solución eficiente
'''
def sum_mix(arr):
    return sum(map(int, arr))


sum_mix(9,1)'''

#Ejercicio
#Are you playing banjo?
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
#The function takes a name as its only argument, and returns one of the following strings:
#name + " plays banjo" 
#name + " does not play banjo"
#Names given are always valid strings.
'''
def are_you_playing_banjo(name):
    if name[0].lower()=='r':
         return name + ' plays banjo'
    return name + ' does not play the banjo'
    #return name[0].lower()

print(are_you_playing_banjo('Raul'))
print(are_you_playing_banjo('raul'))
print(are_you_playing_banjo('Caro'))
'''

#Ejercicio
#Beginner Series #2 Clock

#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time since midnight in milliseconds.

#Example:
#h = 0
#m = 1
#s = 1

#result = 61000
#Input constraints:

# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59
'''def past(h, m, s):
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        sum=(h*3600000)+(m*60000)+(s*1000)
        return sum
    return 'no'

print(past(0,1,1))
print(past(1,1,1))
past(0,0,0)
past(1,0,1)
past(1,0,0)'''

#Ejercicio 
#Beginner - Reduce but Grow

#Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''
def grow(arr):
    sum=1
    for i in arr:
        sum*=i
    return sum

print(grow[1,2,3]) '''   

#Ejercicio
#Invert values
#Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

#Este va modificando la lista inicial
'''
def invert(lst):
    for i in range(0,len(lst)):
        lst[i]==(-1)*(lst[i])
    return lst

print(invert[1,2,3])'''

#Este no cambia la lista inicial
#Se van guardando los nuevos valores en una nueva lista
'''def invert(lst):
    res=[]
    for i in range(len(lst)):
        res.append((-1)*(lst[i]))
    return res'''

#La solución óptima
'''def invert(lst):
    return [-x for x in lst]'''


#Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

#Example(Input => Output):
#35231 => [1,3,2,5,3]
#0 => [0]

'''def digitize(n):
    lis=[]
    if n==0:
        lis.append(n)
        return lis
    else:
        while n > 0:
            lis.append(n % 10)
            n=n//10
        return lis'''

#solución óptima

'''def digitize(n):
    return map(int, str(n)[::-1])'''


#Ejercicio
#Sum of positive
#You get an array of numbers, return the sum of all of the positives ones.
#Example [1,-4,7,12] => 1 + 7 + 12 = 20
#Note: if there is nothing to sum, the sum is default to 0.

'''def positive_sum(arr):
    a=0
    for i in range(0,len(arr)):
        if arr[i]>0:
            a=a+arr[i]
    return a

#Mejor:
def positive_sum(arr):
    a=0
    for i in arr:
        if i>0:
            a=a+i
    return a'''


#L1: Set alarm
#Write a function named setAlarm which receives two parameters. 
#The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

#The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). 
#It should return false otherwise. Examples:

# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true

'''def set_alarm(employed, vacation):
    if employed==True and vacation ==False:
        return True
    else:
        return False

#Óptima
def set_alarm(employed, vacation):
    return employed and not vacation'''


#Will you make it?
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

# Considering these factors, write a function that tells you if it is possible to get to the pump or not.

# Function should return true if it is possible and false if not.

'''def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg*fuel_left:
        return True
    else:
        return False'''

#Óptima
'''def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


print(zeroFuel(50,25,1))'''

#If you can't sleep, just count sheep!!
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.


'''def count_sheep(n):
    a=''
    if n==0:
        print(a)
    else:
        for i in range(1,n+1):
            a=a+('{} sheep...'.format(i))
        print(a)'''

'''count_sheep(5)'''


'''def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))'''


# Descending Order
# DESCRIPTION:
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

'''def descending_order(num):
    a=str(num)
    b=sorted(a, reverse=True)
    c=''.join(b)
    d=int(c)
    return d'''

#Óptima
'''def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))'''

# Binary Addition
# Implement a function that adds two numbers together and returns their sum in binary. 
# The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

'''def add_binary(a,b):
    c=format(a+b,'b')
    return c'''

#Poniendo la función bin se pone en binario, pero con un prefijo 0b
#Con este formato ya es binario solo

# Óptima
'''def add_binary(a,b):
    return bin(a+b)[2:]'''

# Aquí usaron bin, pero le están indicando que sólo imprima a partir del i=2, o sea, del tercer lugar.




# Returning Strings
# Make a function that will return a greeting statement that uses an input; 
# your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

# def greet(name):
#     return (f"Hello, {name} how are you doing today?")

# print(greet('Caro'))





# Remove String Spaces
# Simple, remove the spaces from the string, then return the resultant string.

# def no_space(x):
#     return (x.replace(' ', ''))




# List Filtering
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]



# def filter_list(l):
#     new_list=[i for i in l if isinstance(i, int)]
#     return new_list

# def filter_list(l):
#   'return a new list with the strings filtered out'
#   return [x for x in l if type(x) is not str]

# Esta está más tranquila porque directamente revisa el tipo de dato de x
# e indica que si no es str, que lo puede guardar




# Convert a Boolean to a String
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

# def boolean_to_string(b):
#     return 'True' if b==True else 'False'

# Aunque no hay necesidad de poner el '==True' porque, por si solo le dices que 'if b'
# o sea, que si es True, haga eso


# La óptima
# def boolean_to_string(b):
#     return str(b)



#Sum of two lowest positive integers
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

# def sum_two_smallest_numbers(numbers):
#     b=sorted(numbers)
#     return b[0]+b[1]

# La óptima
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])




# How good are you really?
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. 
# You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. 
# Now calculate the average and compare your score!

# Return True if you're better, else False!

# Note:
# Your points are not included in the array of your class's points. 
# For calculating the average point you may add your point to the given array!

# def better_than_average(class_points, your_points):
#     if (sum(class_points)/len(class_points))<your_points:
#         return True
#     else:
#         return False

# la óptima

# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)




# Is this a triangle?

# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

# def is_triangle(a, b, c):
#     if a+b>c and b+c>a and c+a>b:
#         return True
#     else:
#         return False


# La óptima
# def is_triangle(a, b, c):
#     return (a<b+c) and (b<a+c) and (c<a+b)



# Convert boolean values to strings 'Yes' or 'No'
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
#     return 'Yes' if boolean else 'No'

# Es igual a la óptima



# You can't code under pressure #1
# Code as fast as you can! you need to double the integer and return it

# def double_integer(i):
#     return 2*i



# Count by X
# Create a function with two arguments that 
# will return an array of the first n multiples of x.

# Assume both the given number and the number of times 
# to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]

# La primera que escribiste
# def count_by(x, n):
#     a=[]
#     for i in  range(1,n+1):
#         a.append(x*i)
#     return a

# Es la segunda óptima, pero la hiciste tú
# def count_by(x, n):
#      return [x*i for i in range(1,n+1)]




# Keep Hydrated!
# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 
# 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return 
# the number of litres Nathan will drink, rounded to the smallest value.

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5

# def litres(time):
#     return int(time*0.5)
    # o mejor
   #return time//2





# RGB to Hex Conversion
# The rgb function is incomplete. 
# Complete it so that passing in RGB decimal values will result 
# in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. 
# Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand 
# with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


# def rgb(r, g, b):
#     ro=format(r,'X')
#     gr=format(g,'X')
#     bl=format(b,'X')
#     print(f"{ro:02}",f"{gr:02}",f"{bl:02}",sep='')

# rgb(1,0,0)

#********************************************************************
# def rgb(r, g, b):
#     if 0<=r<=255:
#         ro=format(r,'X')
#     elif r<0:
#         ro=format(0,'X')
#     else:
#         ro=format(255,'X')
    
#     if 0<=g<=255:
#         gr=format(g,'X')
#     elif g<0:
#         gr=format(0,'X')
#     else:
#         gr=format(255,'X')

#     if 0<=b<=255:
#         bl=format(b,'X')
#     elif b<0:
#         bl=format(0,'X')
#     else:
#         bl=format(255,'X')
    
#     a=(f"{ro:02}"+f"{gr:02}"+f"{bl:02}")
#     print(a)

# rgb(216,14,15)
#*********************************************************************

# # r=1
# # ro=format(r,'X')
# # print(ro)
# # a=f"{ro:02}"
# # print(a)

# r=1
# ro=format(r,'X')
# gr=1
# bl=1
# a=(f"{ro:02}"+f"{gr:02}"+f"{bl:02}")
# print(a)
# print(ro)


# r=15
# ro=format(r,'X')
# print(ro)

# Solución mía

# def rgb(r, g, b):
#     if 16<=r<=255:
#         ro=format(r,'X')
#     elif 0<=r<=15:
#         ro='0'+str(format(r,'X'))
#     elif r<0:
#         ro=format(0,'X')
#     else:
#         ro=format(255,'X')
    
#     if 16<=g<=255:
#         gr=format(g,'X')
#     elif 0<=g<=15:
#         gr='0'+str(format(g,'X'))
#     elif g<0:
#         gr=format(0,'X')
#     else:
#         gr=format(255,'X')

#     if 16<=b<=255:
#         bl=format(b,'X')
#     elif 0<=b<=5:
#         bl='0'+str(format(b,'X'))
#     elif b<0:
#         bl=format(0,'X')
#     else:
#         bl=format(255,'X')
    
#     a=(f"{ro:02}"+f"{gr:02}"+f"{bl:02}")
#     return a



# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


# En esta parte min(255, max(x, 0))
# evalúa primero el máximo entre 0 y el número dado, de ahí
# toma el mínimo entre el 255 y el número que salió de la evaluación anterior

# return ("{:02X}" * 3).format(round(r), round(g), round(b))
# En esta parte, el formato de dos dígitos se pone dos veces 
# y con format, acomodamos las tres funciones que estamos llamando
# y cada función, toma su respectiva variable en la x 

# Otra

# def limit(num):
#     if num < 0:
#         return 0
#     if num > 255:
#         return 255
#     return num


# def rgb(r, g, b):
#     return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))




# Bit Counting
# Write a function that takes an integer as input, and returns the number 
# of bits that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.

# Example: 
# The binary representation of 1234 is 10011010010, so 
# the function should return 5 in this case


#Falta resolver
# def count_bits(n):
#     a=bin(n,[2:])

# count_bits(1)