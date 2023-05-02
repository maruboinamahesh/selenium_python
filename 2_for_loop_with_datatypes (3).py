'''
1. We can use all data types in for loop except number.
'''

## string iterate character by characters
s = 'sri ram'
for c in s:
    print(c)

## LIST iterate value by value 
names = ['sri','ram','kumar','nagesh', 'balu']
for name in names:
   print(name)

## TUPLE iterate value by value 
names = ('sri','ram','kumar','nagesh', 'balu')
for name in names:
   print(name)

## SET iterate value by value 
names = {'sri','ram','kumar','nagesh', 'balu'}
for name in names:
   print(name)

# Dictionary iterate based on key
emp_det = {'name':'sri', 'eid':35, 'dname':'IT'}
for k in emp_det:
    print(k)

for k,v in emp_det.items():
    print(k,v)

## Number object does not support for iterable
NO =  345
for n in NO: 
    print(n)
    
#nested loop with for loop
for i in [1,2,3,4]:
    print("-----",i)
    for n in 'src':
        print("    *****",n)

'''output:----- 1
    ***** s
    ***** r 
    ***** c
----- 2
    ***** s 
    ***** r 
    ***** c
----- 3
    ***** s
    ***** r 
    ***** c
----- 4
    ***** s 
    ***** r 
    ***** c'''
