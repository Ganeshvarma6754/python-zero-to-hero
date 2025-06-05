print(round(24))
print(round(3.9))
import math
print(math.sin(3))  
print(20-3+4%13//6)
a=12
print(bin(a))
a=123
print(a)
_user_case="edi okka l***ja ko***duku katha"
print(_user_case)
name=123
iq=name+123
print(iq)
k,b,c=1,2,3
print(k)
print(b)
print(c)
some_value=5
some_value=+2
print(some_value)
a=5
a=-5
print(a)
print(type("ganesh_varma"))
long_stringa='''
:)
:(
:|
:0
'''
print(long_stringa)
first_name ="ganesh"
second_name="varma"
full_name=first_name+" "+second_name
print(full_name)
print(type(str(100)))
a=str(100)
b=int(a)
c=type(b)
print(c)
print("\u2764")
name = "ganesh"
age = 25
print("iam name %s and my age is age %d"%(name,age))
print(f"iam  {name} and my age is {age}")
a=5
b=10
print(f"the sume is {a+b}")
ganesh = "ganesh"
print(ganesh[0:])
real= "123456789"
real=real[0:2:4]+"10"
print(real)
Ganesh="ramesh"
Ganesh="g"+Ganesh[1::]
print(Ganesh)
Ganesh.upper()
print(Ganesh.upper())
print(len(Ganesh))
print("\a")
print(_user_case.encode())
print(Ganesh.format())
my_list=[1,2,3,4,"ganesh"]
my_list.remove(2)
print(my_list)
numbers=[5,0,1,6,9,10]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
application ={
  "name":"ganesh",
  "age":25,
  "occupation":"software developer"
}
print(application["age"])
students=[
  {
    "name":"ganesh",
    "age":25,
    "occupation":"software developer"
  },
  {
    "name":"ramesh",
    "age":25,
    "occupation":"QA engineer"
  }
]
for students in students:
  print(students["name"],students["occupation"])
students = [
    {"name": "Amit", "age": 22, "marks": 85},
    {"name": "Sara", "age": 23, "marks": 90},
    {"name": "John", "age": 21, "marks": 88}
]
print(students[0]["name"],students[2]["age"])
print(students[0].get("family","ramakirshna"))
ganesh = 1,2,3,5
print(ganesh)
print(len(ganesh))
for item in ganesh:
  print(item,end="")
lenja=("sahana","neethu azmal","deepika",1,2,3)
print(lenja[0:3])
age=60
if age<20:
  print("your not eligible to vote")
elif age>=20:
  print("your eligible to vote")
else:
  print("your not born")
x=10
if x>5:
  if x<20:
      print("x is the fine number")
x=10
print("lenjakodaka") if x==10 else print("lenja")

is_magican= False 
is_expert = False
if is_magican and is_expert:
  print("your are a magican")
elif is_magican and not is_expert:
    print("atleast you are getting there")
else:
  print("you need magic powers")

print(True== 1)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  for item in ["ganesh","varma","likith",]:
      if item+fruit:
          print(item,fruit)



application={
  "name":"ganesh",
  "age":25,
  "occupation":"software developer"
}
for k,v in application.items():
  print(k,v)

my_list=[1,2,3,4,5,6,7,8,9,10]
counter=0
for item in my_list:
  counter=0
  counter=counter+item
print(counter)

my_list = [3, 6, 9, 12, 15, 18, 21, 24]
counter=0
for i in my_list:
  if i%2==0:
    counter=counter+i

print(counter)


my_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
counter=0
for i in my_grid:
  for j in i:
    if j%2==0 and not j%3==0:
      counter=counter+j
print(counter)

my_grid = [
    [5, 12, 7, 8],
    [3, 6, 9, 10],
    [2, 14, 15, 18],
    [4, 11, 13, 16]
]

count=0
for i in my_grid:
  for j in i:
    if j%2==0 and j>5 and not j%3==0:
      count=count+j
    

print(count)

for i in range(1,10):
  print(i,end="")


fruits=["apple","banana","cherry"]
for fruit in enumerate(fruits):
  print(fruit)

ganesh={
  "name":"varma",
  "age":25,
  "occupation":"software developer"
}

for i,j in enumerate(ganesh.keys(),start=1):
  print(i ,j)

while True:
  print("ganesh")
  break

count=0
while count<10:
  print(count)
  count=count+1



some_list=["a","b","b","c","c","d","e","f","g","g","h"]
if set(some_list):
  pass
else:
    print("no duplicates")
def greet_ganesh():
  greet= "hello_ganesh"
  if range(0,10):
    print(greet)

greet_ganesh()

def movie(hero_name,heroine_name,villan_name):
  print(f"{hero_name} is a hero and {heroine_name} is a heroine and {villan_name} is a villan for pokiri movie")
  return movie
movie("ganesh","sahana","azmal")
movie("ganesh","sahana","azmal")

def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()

def add_numbers(a,b,c,d,e):
  print(a,b,c,d,e)
  return sum([a,b,c,d,e])
  
result=add_numbers(1,2,3,4,5)
print("sum",add_numbers(1,2,3,4,5))

a=30
def ganesh():
  a=20
  def varma():
    return a
  print(varma())
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)



    



  


  





    
  
