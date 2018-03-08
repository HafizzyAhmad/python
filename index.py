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

while True:
    print('durian')
    pass






