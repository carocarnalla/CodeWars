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

def digitize(n):
    lis=[]
    if n==0:
        lis.append(n)
        return lis
    else:
        while n > 0:
            lis.append(n % 10)
            n==n/10
        return lis

print(digitize(10))