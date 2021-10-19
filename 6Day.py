import numpy as np
import random
#Operating System
import os
import matplotlib.pyplot as plt
import pandas as pd
#Third Party Library
from sklearn import linear_model


#This will fetch the current working directory
#cwd -> Current Working Directory
ProjectPath = os.getcwd()
print(ProjectPath)

MyFile = ProjectPath + "\\DataFolder\\RegressionData.csv"
print(MyFile)

df = pd.read_csv(MyFile)  #Data Frame
print(df)

x = np.array(df['X']).reshape(-1,1)
y = np.array(df['Y']).reshape(-1,1)

regr = linear_model.LinearRegression()
regr.fit(x, y)

print("\nb0 = ",regr.intercept_)
print("\nb1 = ",regr.coef_)





'''
x = df[['Temp','Humidity','Rainfall','Soil']]
y = df['Biomass']

regr = linear_model.LinearRegression()
regr.fit(x, y)

print(regr.coef_)
for r in range(0,len(df)):
    t = df['Temp'][r]
    h = df['Humidity'][r]
    rf = df['Rainfall'][r]
    s = df['Soil'][r]
    p = regr.predict([[t, h, rf, s]])
    print("x = %d, %d, %d, %d, %d\tPredicted=%f"%(df['Temp'][r],df['Humidity'][r],df['Rainfall'][r],df['Soil'][r],df['Biomass'][r],p))

t=25
h=30
rf=623
s=40
p = regr.predict([[t, h, rf, s]])
print("x = %d, %d, %d, %d, \tPredicted=%f"%(t,h,rf,s,p))

'''




'''
#Duplicacy Check --> Pattern Matching

X = df[['Mathes']]
y = df['Final']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[76]])

print(predictedCO2)

#print(df.duplicated(keep=False))
'''



'''
Data  = {
            'x': [2,   3  , 4  , 5  , 6  ],
            'y': [2.3, 4.5, 6.7, 0.9, 9.8],
            'z': ["ABC", "XYZ", "LMN", "PQR", "RST"]
        }
df = pd.DataFrame(Data,columns=['x','y','z'])
print(df)
'''













'''
#getcwd --> Get the current working directory
ProjectPath = os.getcwd()

MyFile = ProjectPath + "\\TestFile.xls"
#MyFile =  "H:\\TestFile.xls"
df = pd.read_excel(MyFile)  #Data Frame
print(df)
'''

'''
a = [2, 3, 4, 5]                    #Int Array
b = ["abc", "xyz", "pqr", "lmn"]    #String Array

# We can collect or combined a and b in a single dta structure called as data frame.

x = {
        'a': a,
        'b': b,
        'c': [9.8, 4.5, 6.7,8.9],
        'dob': ["1-1-1976","2-3-2000","12-5-1989","13-09-2011"]
    }
 
df = pd.DataFrame(x,columns=['a','b','c','dob'])
print(df)
print(df['a'])
'''

'''
Score=10
for r in range(2,5,2):
    Score = Score-1
print(Score)
'''    


'''
#Task:
#1. Create a file named RandNumbers.txt.
#2. Write 100 random numbers in range (0, 1000) with 10 random numbers
#   in each line.
#3. Write the Sum of each line in the end.
#4. The file writing should be supported by proper formatting
#5. Also mention the file path at the top of the file

Start = 0
End = 1000
N = 100

#CWD --> Current Working Directory
ProjectPath = os.getcwd()
print(ProjectPath)
FilePath = ProjectPath + "\Test.txt"
#fpt --> File Pointer
fpt = open(FilePath,"w")

for r in range(0,N):
    t = random.randint(Start,End)
'''    

'''
#CWD --> Current Working Directory
ProjectPath = os.getcwd()
print(ProjectPath)

FilePath = ProjectPath + "\Test.txt"
#fpt --> File Pointer
'''
'''
fpt = open(FilePath,"w")
Names = ["Arnav","Vikas","Verma","Goel","asjdkfhjkasdh"]
#\n --> New Line Character --> Inserts new line in the print format
NewNames=[]
for r in range(0,len(Names)):
    temp = sorted(str(Names[r]).lower()) #'a','a','n','r','v'
    s = ''  # Blank String
    for c in range(0,len(temp)):
        s = s + temp[c]
    NewNames.append(s)
    fpt.write("%d %s %s\n"%(r+1,Names[r],NewNames[r]))
    
fpt.close()
'''

'''
fpt = open(FilePath,"r")
lineRead = (fpt.read()).split("\n")
fpt.close()

for r in range(0,len(lineRead)):
    print("\n",lineRead[r])
    temp = lineRead[r].split(" ")
    for c in range(0,len(temp)):
        print(temp[c])

'''
'''
#\n --> New Line Character --> Inserts new line in the print format
NewNames=[]
for r in range(0,len(Names)):
    temp = sorted(str(Names[r]).lower()) #'a','a','n','r','v'
    s = ''  # Blank String
    for c in range(0,len(temp)):
        s = s + temp[c]
    NewNames.append(s)
    fpt.write("%5d%20s%20s\n"%(r+1,Names[r],NewNames[r]))
'''


'''
Names = ["Arnav","Vikas","Verma","Goel","asjdkfhjkasdh"]
Names.sort()
print(Names)


NewNames=[]
for r in range(0,len(Names)):
    temp = sorted(str(Names[r]).lower()) #'a','a','n','r','v'
    s = ''  # Blank String
    for c in range(0,len(temp)):
        s = s + temp[c]
    NewNames.append(s)
print(NewNames)
'''



#Task:
#    1. Generate 10 random numnbers BETWEEN 0 TO 20.
#    2. Arrange them in ascending order and get the sum of first 5 terms
#    3. Arrange them in descending order and get the sum of first 5 terms
'''
N = 5
Num=[]
for r in range(0,N):
    Num.append(random.randint(0,20))
print(Num)
'''



'''
x = [2, 3, 8, 4, 90, 76]
print("Before Sorting: ",x)

y = sorted(x)
print("After Sorting in ascending : ",y)

y = sorted(x,reverse=True)
print("After Sorting in descending: ",y)

print("Original Array: ",x)

x = ["Vikas","Arnav","Verma","Goel"]
print("\n",x)

y = sorted(x)
print("After Sorting in ascending : ",y)

y = sorted(x,reverse=True)
print("After Sorting in descending: ",y)

print("Original Array: ",x)
'''

'''
x = np.array(["Vikas","Arnav","Verma","Goel"])
print("\n",x)

y = np.argsort(x)
print(y)

z = x[y]
print("z = ",z)
'''

#Task: 


#Task:  Fill an array with natural numbers till the sum is 1000.
#       Extract out the fibonacii elements from the series.
#       Count the number of fibonacii elements
#       Get the Fibonacii elements above 20

'''
Sum = 0
r=0
elements=[]
while(Sum<1000):
    Sum = Sum + r
    elements.append(r)
    r=r+1
print("\nSum = ",Sum,"\n")    
print(elements)

t1=0
t2=1
Count=0
print("\n")
for r in range(0,len(elements)):
    t = t1 + t2
#    print(t)
    for i in range(0,len(elements)):
        if(elements[i]==t):
            print("Element-",i," = ",elements[i])
            Count = Count+1
    t1 = t2
    t2 = t
print("\nTotal no. of Fibonacii Elemenets = ",Count)
'''


'''
Sum = 1 + 2 + 3 + 4 + ............... = 1000
Fibonacii elements: 1, 1, 2, 3, 5, .....
No. of Fibonacii elements: 
'''





#Task:  Write a code to get the power of 2 
#       till the power of 2 is less than or equal to 
#       800;



''' 
x=2
for r in range(0,10):
    t = math.pow(x,r)    
    print(r,"\tt = ",t)


x=2
t = 0
r=0;
print("\n\n")
while(t<800):
    t = math.pow(x,r)    
    print(r,"\tt = ",t)
    r=r+1
'''    


















#Task:
#       If the principal amount is 100 and rate of interest (simple) is 10%,
#       then in how many years, the amount will be doubled?

'''
P = 100 # Principal Amount
I = 4   # Rate of interest
n = 1   # Years
FA = 10*P

Sum = P

while(Sum <= FA):
    Sum = P + (P * I * n)/(100)
    print("P = %.1f,\tn = %d,\tFA = %.1f"%(P,n,Sum))
    n = n+1
    P = Sum
'''
'''
x = 2
y = 4
z = x**y
print("%d^%d = %d"%(x,y,z))

x = 2
y = 4.5
z = x**y
print("%d^%d = %s"%(x,y,z))

x = 2
y = 4.5
z = math.pow(x,y)
print("%d^%s = %s"%(x,y,z))
'''


'''
Sum = 0
r=0
while(Sum<=1000):
    Sum = Sum + r*r
    print("r=%d\tSum = %d"%(r,Sum))
    r=r+1
    
'''

#Task: Find out the prime numbers from 1 to 50
'''
while(1):
    if keyboard.is_pressed('q'):
       print("You Pressed A Key!")

'''

'''
def CheckPrime(n):
    Flag=1
    for r in range(2, (n//2)):
        if(n%r == 0):
            Flag = 0
    if(n%2==0):
        Flag=0;
    return(Flag)         
    
Start = 20
End = 100

for x in range(Start,End):
    Flag = CheckPrime(x)
    if(Flag==1):
        print("The number = %d is a prime number"%x)

'''




'''
#Task:
#        1. Find the first 30 Fibonacii elements.
#        2. Separate the even, odd and prime numbers in different arrays.
#        3. Given counts of each even, odd and prime numbers.
#        4. Sum of all even, prime and odd numbers.
'''

'''
Example: 1 to 10
1, 1, 2, 3, 5, 8, 13, 21, 34, 55

Even: 2, 8, 34 (3)
Prime: 1, 1, 3, 5, 13, (5)
Odd: 1,1, 3, 5, 13, 21, 55 (7)
'''





'''
Start = 20
End = 100
for n in range(Start, End):
'''    


'''
Num = 21

Flag = 1
for r in range(3, (Num//2)):
    if(Num%r == 0):
        Flag = 0
if(Flag==1):
    print("%d is a Prime Number"%Num)
          
if(Flag==0):
    print("%d is a not Prime Number"%Num)
'''

'''
x = [[1, 0 , 3], [4, 6, 78], [89, 65, 44], [34, 67, 98], [22, 65, 85], [35, 76, 23]]

print(len(x))
print(x[0])
print(len(x[0]))
for n in range(0, len(x)):
    for r in range(0,len(x[0])):
        print(x[n][r])
'''
'''
ROW = 10
COL = 10

s =[]   #(([])*ROW)*COL  #Blank Array of s[ROW][COL] = s[10][3]

for r in range(0,10):
    t=[]
    t.append((r+1)*2)
    t.append((r+1)*3)
    t.append((r+1)*4)
    t.append((r+1)*5)
    s.append(t)
#    print(t)

for r in range(0,ROW):
    print("%d\t%d\t%d\t%d"%(s[r][0],s[r][1],s[r][2],s[r][3]))
#   \t --> Tab          Escape Sequence
#   \n --> New Line     Escape Sequence
'''
'''
a = 1
b = 1
n = 50
print(a)
print(b)
Even=[]
Odd=[]
for n in range(2, n):
    t = a + b
    if(t%2==0): Even.append(t)
    if(t%2==1): Odd.append(t)
    a = b
    b = t
    print(t)
print("Even terms of F-bonacii Series:",Even)
print("Odd  terms of F-bonacii Series:",Odd)
'''
'''
#s = ([0])*10 #Array of 10 elements named as s
s = []       #Blank Array
NO_OF_ELEMENTS=10
for r in range(0,NO_OF_ELEMENTS):
    s.append(r*5)       #Append -- Add on
    #s[r]=r*5
    print("s[%d] = %d"%(r,s[r]))
'''

'''
def calcArea(a, b, c):
    Flag=0
    perimeter=0
    FlagRA=0
    area=0
    if((a+b>c) or (b+c>a) or (a+c>b)):
        Flag=1
    if(Flag==1):
        if((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2)):
            FlagRA=1
        s = (a + b + c)/2
        perimeter = a +b + c
        area = sqrt(s*(s-a)*(s-b)*(s-c))
    if(FlagRA==1 and Flag==1):
       print("It is a right angle triangle")
    if(FlagRA==0 and Flag==1):
       print("It is not a right angle triangle")
                    
    return (perimeter, area)

#Indenting

    
a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))

perimeter, area = calcArea(a, b, c)
print("Perimeter of the triangle = %.2f unit , Area of the triangle = %.2f sq. unit" %(perimeter, area))
'''
'''
Sum=0
SumSq=0
SumCube=0
for n in range(0,11):   
    Sum = Sum + n
    SumSq=SumSq+(n**2)
    SumCube = SumCube+n**3
print("Sum = %d"%Sum)
print("Sum of Squares = %d"%SumSq)
print("Sum of cubes   = %d"%SumCube)
'''

#MISRA --> Motor Industry Software Research Agency -->
#() --> Soft Brackets
#  [] -> Square Bracket
#    {} --> Curly Bracket

# Parenthesis Balancing
'''
evenNum = 0
oddNum = 0

Start = 10
End = 100
for n in range(Start, End + 1):
    if(n % 2) == 0:
        evenNum = evenNum + n
    else:
        oddNum = oddNum + n

print("Sum of even numbers from 1 to 10 = ", evenNum)
print("Sum of odd numbers from 1 to 10 = ", oddNum)
'''

'''
x = 3
y = 3
z = x/y

a = floor(z)
b = ceil(z)
print(x,"/",y," = ",z)
print("a = ",a)
print("b = ",b)
'''


'''
import math

# input--> keyword
# chr --> Character

def calcArea(L,W):
    A = L*W
    return(A)

def calcAreaCircle(radius):
    pi = 3.1457
    a = pi*radius**2
    return(A, V)

    
x = int(input("Enter the length: "))    
y = int(input("Enter the width : "))    

Area = calcArea(x,y)        #Function Calling
print(Area)

V, area_2 = areacircle(r)
'''


'''
x = int(input("Enter first  number: "))
y = int(input("Enter second number: "))
z= x/y
#   Formatting
#print("%.2f/%.2f = %.4f"%(x,y,z))

z = x**4
print("z = x**4 = %d"%z)

z = x*4
print("z = x*4 = %d"%z)
'''

'''
# Blok comment
x = 1000
y = int(x/1000)		# 1
z = int(x%1000)	        # 234
u = int(z/100)		# 2
v = int(z%100)		# 34
w = int(v/10)		# 3
m = int(v%10)		# 4

print(y,u,w,m)
'''

