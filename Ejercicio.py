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

def add_binary(a,b):
    print(a+b)

add_binary(1,1)