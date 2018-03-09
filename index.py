#if STATEMENTS

result = int(input("please enter raw scores:"))

if result >= 91:
    print("A*")
elif result >= 75:
    print("A")
elif result >= 60:
    print("B")
elif result >= 50:
    print("C")
elif result >= 35:
    print("D")
elif result >= 20:
    print("E")
else:
    print("U")

'''
EXPECTED OUTCOME

please enter raw scores:90
A

'''


#for STATEMENTS

fruit_collection = ['apple','orange','guava','durian','rambutan']

for f in fruit_collection:
    print(f,len(f),f.upper())

'''
EXPECTED OUTPUT

(FOR STATEMENTS)

apple 5 APPLE
orange 6 ORANGE
guava 5 GUAVA
durian 6 DURIAN
rambutan 8 RAMBUTAN

'''

#THE RANGE FUNCTION

for i in range(5):
    print(i)
    
'''
EXPECTED OUTCOME

0
1
2
3
4

'''

for i in range(-4,4,2):
    print(i)

"""
-4
-2
0
2
"""


fruit_collection = ['apple','orange','guava','durian','rambutan'] #ini adalah list , dalam square bracket adalah list

fruit_collection
for i in range(len(fruit_collection)):
    print(i,fruit_collection[i])

'''
EXPECTED OUTCOME

(0, 'apple')
(1, 'orange')
(2, 'guava')
(3, 'durian')
(4, 'rambutan')

'''

for k,v in enumerate(fruit_collection): #ini short form untuk list yang kat atas
    print(k,v) #variable boleh jadi 1 atau 2 coz list hold untuk 2 value

'''
EXPECTED OUTCOME

(0, 'apple')
(1, 'orange')
(2, 'guava')
(3, 'durian')
(4, 'rambutan')

'''

range(4)
'''
EXPECTED OUTCOME
[0, 1, 2, 3]
'''

list(range(4))
'''
EXPECTED OUTCOME
[0, 1, 2, 3]
'''

list(fruit_collection)
'''
EXPECTED OUTCOME
['apple', 'orange', 'guava', 'durian', 'rambutan']
'''

#BREAK,AND CONTINUE STATEMENTS, AND ELSE CLAUSES ON LOOPS

for f in fruit_collection:
    if f == 'durian':
        print ("Found the smelly fruit!!! -->",f)
        break #boleh tukar jadi 'continue' kalau nak keluarkan rambutan sebab dia tak loop
    else:
        print("Love this fruit -->",f)

'''
EXPECTED OUTCOME

('Love this fruit -->', 'apple')
('Love this fruit -->', 'orange')
('Love this fruit -->', 'guava')
('Found the smelly fruit!!! -->', 'durian')
('Love this fruit -->', 'rambutan') Ni kalau tukar jadi continue

'''

for n in range(2,10):
    if n % 3 == 0:
        print("Found a number divisible by 3 -->", n)
        continue
    print("Just another number", n)

'''
EXPECTED OUTPUT

Just another number 2
Found a number divisible by 3 --> 3
Just another number 4
Just another number 5
Found a number divisible by 3 --> 6
Just another number 7
Just another number 8
Found a number divisible by 3 --> 9

'''

#PASS STATEMENTS

while True: #keep running background process. Jangan buat print hahah
    pass


"""
EXPECTED OUTPUT

Keep running until keyboard interrupt ctrl-C

"""

def calculate_random(object):
    pass #to implement

calculate_random(1)

"""
EXPECTED OUTPUT

Calculate randomly withoun an error

"""

#DEFINING FUNCTIONS

def square_fn(obj): #obj is an argument(actual parameters)-call by value
    return obj *obj

square_fn(5)

square_fn #error because no argument(obj)

sf=square_fn #nak declare sf tu apa then call
sf(4)

#Dapat Jawapan Function : 16


sf(4,5) #takes 1 positional argument but 2 were given

def tm(n):
"""
Return a list containing the
tm series up to 5

""" 
    result=[]
    a,b = 0,1
    while a < n:
        result.append(a) #function append tambahkkan dalam list[]
        a, b = b, a + b
    return result

f100 = tm(100)

f100

"""
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
f100.append(100)

f100

a=10
b=[]
b.append(a) #hanya list [] je boleh append, kalau integer tak dapat


f100.append(100) #dah define 100 then 100 akan masuk dalam list sekali
f100

#MORE ON DEFINING FUNCTIONS (DEFAULT ARGUMENT VALUES)

def car_color(color='red'):
    print(color)

car_color ()

car_color(color='blue')

my_color ='green'
def water_color(arg=my_color):
    print(arg) #Bila run tak jadi, so kena panggil eg water_color() sebab kita simpan dalam bakul water_color

def f (a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4)) #func print akan keluar ikut berapa banyak no of list nak kelua

"""
EXPECTED OUTCOME

>>> print(f(1))
[1]
>>> print(f(2))
[1, 2]
>>> print(f(3))
[1, 2, 3]
>>> print(f(4))
[1, 2, 3, 4]

Ni sebab L shared between subsequent calls

"""

def f(a, L=None): #If L by default None 
    if L is None: # this if line will be make the list standalone
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4))

"""
EXPECTED OUTCOME

>>> print(f(1))
[1]
>>> print(f(2))
[2]
>>> print(f(3))
[3]
>>> print(f(4))
[4]

"""

#KEYWORD ARGUMENTS

def parrot(a,s,b = 'plant', c = 'cat', d='red'): #b,c,d keyword argument a,s positional(non keyword) arguments
    print("the first argument is ", a)
    print("animals versus ",b)
    print("Computer vision comparing dogs versus ",c)
    print("The Sky is ",d)
    print("The Sky is ",s)

parrot(2,1) # a&s need the value because takde value dalam

"""
EXPECTED OUTCOME

('the first argument is ', 2) NI VALUE A
('animals versus ', 'plant')
('Computer vision comparing dogs versus ', 'cat')
('The Sky is ', 'red')
('The Sky is ', 1) NI VALUE S

positional argument must follow keyword argument

"""
parrot(a=2,s=3)

"""
>> parrot(a=2,s=3)
('the first argument is ', 2)
('animals versus ', 'plant')
('Computer vision comparing dogs versus ', 'cat')
('The Sky is ', 'red')
('The Sky is ', 3)
"""

def long_list(fruit, *tropic, **temperate): #Tuple = Positional arguments
    print(fruit)
    print(40 * "*")
    print("[INFO] This is in *tropic")
    for t in tropic: #Tuple is Positional Arguments, Doesnt have 
        print(t)
    print(40 * "*")
    print("[INFO] This is in **temperate") #Dictionary is Keyword Arguments and must declare with 
    for kw in temperate:
        print(kw, ":", temperate[kw])

long_list("fruits","banana","mango",Australia="orange", US="Sunkist")

"""
EXPECTED OUTCOME

Function Tuple & Dictionary boleh gunakan dalam list untuk positional & keyword

fruits
****************************************
[INFO] This is in *tropic
banana
mango
****************************************
[INFO] This is in **temperate
('Australia', ':', 'orange')
('US', ':', 'Sunkist')

"""

#UNPACKING ARGUMENT LISTS

list(range(3,6)) #[3, 4, 5]

args = [3,6]
list(range(*args)) #[3, 4, 5]

#LAMBDA EXPRESSIONS

sqrt = lambda m, n : m ** (1/n)
sqrt(4, 2)

def sqrt_func(m,n):
    return m ** (1/n)

sqrt_func(4,2)


#PRINT DOC STRING MACAM """CDWCSC"""

def my_func():
    """
    MOHAMAD HAFIZZY AHMAD
    THAT'S ALL IT SAYS, REALLY
    
    """
    pass

print (my_func.__doc__) #dia akan keluar apa yang ada dalam string

#CODING STYLE

#DATA STRUCTURE (ITERABLE)

sentence ='classic text' #AN INTERABLE

iter_sentence = iter(sentence) #AN ITERATOR

next(iter_sentence) 
next(iter_sentence)
next(iter_sentence)
next(iter_sentence)
next(iter_sentence)
next(iter_sentence)
next(iter_sentence)

#LISTS 1.0

a=[1,2,3] #append
a.append(5)
a #a=[1, 2, 3, 5]

b=[11,22] #extend
b.extend(a)
b #b=[11, 22, 1, 2, 3, 5]

b #insert
b.insert(3,1007)
b #b=[11, 22, 1, 1007, 2, 3, 5]

b #remove value in the list
b.remove(1007) #will get an error if wrong value in the list
b #b=[11, 22, 1, 2, 3, 5]

b #remove value based on position
b.pop(2)
b #[11, 22, 2, 3, 5]

a
b
c=a           #copy by reference
d=b.copy()  #shallow copy

c #[1, 2, 3, 5]
c.clear()
c

a
d
d.clear()
d






 

