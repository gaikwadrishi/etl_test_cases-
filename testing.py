class bank1:
    def bank_info(self):#it class
        print("her name is indu")
class bank2:
    def bank_info2(self):#it class
        print("and sir name is athwa")
class division(bank1,bank2):#it create object
    pass#pass complsory becz iy make empty
a1=division()
a1.bank_info()
a1.bank_info2()














def is_even(number):
    return number % 2 == 0

# Test cases
def test_is_even():
    # Test case 1: Even number
    assert is_even(4) == True, "Failed for even number"

    # Test case 2: Odd number
    assert is_even(7) == False, "Failed for odd number"

    # Test case 3: Zero
    assert is_even(0) == True, "Failed for zero"

    # Test case 4: Negative even number
    assert is_even(-10) == True, "Failed for negative even number"

    # Test case 5: Negative odd number
    assert is_even(-3) == False, "Failed for negative odd number"

    print("All test cases pass")

# Run the test cases
test_is_even()





my_list = [1, 2, 2, 3, 3, 3, 4, 4]

# Count duplicates using iteration
duplicate_count = {}
for item in my_list:
    if item in duplicate_count:
        duplicate_count[item] += 1
    else:
        duplicate_count[item] = 1

duplicate_count = {item: count for item, count in duplicate_count.items() if count > 1}

print(duplicate_count)  # Output: {2: 2, 3: 3, 4: 4}


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

a = 45
b = 45
if a > b:
    print("yes a grreter than a")
elif a == b:
    print("a equal to b")
else:
    print("b is greter than a")

r=y=h="ri9shi","raj","me"

print(y,r,h)
print(h)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


a = "Hello@ World@ python , java, is a good langage"

print(a.split(" ")) #seperator



thislist = ["apple", 12, 23.3, 23, "CID", 2.3, True]
a = thislist[0]
print(a + " is good")
print(thislist[1:3])
print(type(thislist))
print(len(thislist))
print(thislist[-2])

thislist = [2345, "banana", "cherry"]
thislist[0] = "watermelon"
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)



thislist = ["apple", "banana", "cherry"]

thislist.remove("banana")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print(fruits)




this = {
    "brand":"tata",
    "model":"land rover",
    "year" :"2222"
}
print(this)
x=this["brand"]
y=this.keys()
z=this.values()
print(x)
print(y)
print(z)



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for c,d in thisdict.items():
    print(c,d)

d={'1':'z','2':'v','3':'b','4':'c'}
for x,y in d.items():
    print(x,y)

for x,y in d.items():
    print(x,y)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x,y in myfamily.items():
    print(x,y)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : [2004,2006,2011,2023]
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child1"]["year"][-1])
#print(myfamily["child1"]["name"])
#print(myfamily["child2"]["year"])
#print(myfamily["child3"]["name"])

d={'1':'z','2':'v','3':'b','4':'c'}
for x,y in d.items():
    print(x,y)

a=500
b=400

if a>b:
    print("a is greter than b")
elif b>a:
    print("b is greter than a")
else:
    print("a equal to b")
print("a is equal to b ") if a==b else print("a is not equal to b")

a = 500
b = 330
print("a is equal to b") if a > b  else print("b")

a=200
b=800
c=700
print("b is greter value") if b>c and b>a else print("b is not greter")



fruits = ["apple", "banana", "cherry",10,20.3]
for x in fruits:
  print(x)
  if x == 10:
    break


fruits = ["apple", "banana", "cherry",10,20.3]
for x in fruits:
  if x == 10:
    continue
  print(x)

for i in range(1,50):
 if i % 2 == 1:
  print(i)

for i in range(1,51):
 if i % 2 == 1:
  print(i)

for i in range(1,40):
 if i%2==0:
     print(i)



i=3
while i<9:
    print(i)
    i+=1

i=2
while i<101:
    print(i)
    i=i*i


i = 1
while i < 6:
    i += 1
    if i == 3:
        continue #skip the current true condition
    print(i)



def add(a, b, c):
    d = a * b * c
    print(d)

add(5, 8,4)


def add(y, z):
    c = y + z
    print(c)


add(20, 30)
add(5, 10)
add(50, 100)
add(200, 400)


def my_fun(fname):
    print(fname+"  gaikwad")

my_fun("rishi")
my_fun("rassu")
my_fun("akshra")


def my_function(*kids):
  print("The youngest child is " + kids[1])

#variable length positional arguments
my_function("Emil", "Tobias", "Linus")



def my_function(child3, child2, child1):
  print("The youngest child is " + child1)
#keyword arguments
my_function(child1 = "Emil rishi", child2 = "Tobias", child3 = "Linus")
#order does not matter

def my_function(country = "Norway"):
  print("I am from " + country)

#default arguments
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(fruits):
  print(type(fruits))
  for x in fruits:
    print(x)
fruits = ["apple", "banana", "cherry"]

my_function(fruits)




def my_function(x):
  return 5 * x
#return main result to function
print("15:-", my_function(3))
print(my_function(5))
print(my_function(9))


hey = lambda z: z + 10
print(type(hey))
print(hey(5))

multi= lambda  x:x*x
print(multi(5))



def myfunc(n):
  print(n)
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

try:
  print(x)
  #username
  #password
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:

    print(tt)
except:
    print("password is incorrect")
else:
    print("login successfully")
finally:
    print("close the file")


import datetime
z= datetime.datetime.now()
print(z.year)
print(z.month)
print(z.day)
print(z.time())


import datetime
z=datetime.datetime(1997,8,31)

print(z.year)
print(z.day)
print(z.month)


try:
    print("rassu")
except:
    print("password is incorrect")
else:
    print("sucessfully log in")
finally:
    print("close file")


from datetime import datetime, timedelta
diff = datetime.today() - timedelta()
print(diff) #returns the complete date.
print(diff.year)
print(diff.month)
print(diff.day)







class carmodel:
    name = "lamborgini"
    model= 2005
def run(self):
    print("best car is= ",self.name)
    print("best ever model= ",self.model)
def car(self):
    print("car best is ever sceen= ",self.name)

obj = carmodel()
print(obj.name)
print(obj.model)





















class fruits:
    def __init__(self,name,price,mono):
        self.name= name
        self.price = price
        self.mono = mono
    def values(self):
        print("fruits name is ",self.name,"price is ",self.price,"mono is ",self.mono)
    def contact(self):
        print("contact no is ",self.mono)
fruits_obj1 = fruits("mango",200,12345678)
fruits_obj2 = fruits("kiwi",4500,14444455)
fruits_obj3 = fruits("waterlemon",7000,5465646)

print(fruits_obj1.name)
print(fruits_obj1.price)
print((fruits_obj1.mono))

fruits_obj1.values()

class lab:
    def __init__(self,name,rowno,seats):
        self.name=name
        self.rowno=rowno
        self.seats=seats
    def values(self):
        print("name is surjan bhau",self.name,"rowno is",self.rowno,"seats are",self.seats)
lab_obj1 = lab("surjan_bhau",1,"reserve")
lab_obj2 = lab("kunal",2,"not reserve")

print(lab_obj1.name)
print(lab_obj1.rowno)
print(lab_obj1.seats)







"""""


class student:
    def __init__(self,name,roll_no,marks,div):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.div = div
    def display(self):
        print("my name is ; ",self.name)
        print("and this is my roll number",self.roll_no)
        print("tottal makrs; ",self.marks)
        print("and division is ; ",self.div)
    obj1 = student("rishi",12,45,"a")
    obj2 = student("rassu",18,96,"b")

obj1.display()
obj2.display()


"""""


tuple = (2,3,4,5)
s = list(map(lambda x: x * x * x, tuple))
print(s)

tupl = (1,2,3)
s = list(map(lambda x: x*x*x,tuple ))
print(s)

lis = [1,2,3,4,5,6,7,8,9,10] #iterable
#syntax = filter(function, iterable)
s = list(filter(lambda x: x%2 == 0, lis))
print(s)



lis = [2,4,6,7,8,9] #reduce it to one value #sum avg
s = (rd(lambda x,y: x+y, lis)) #addition of all number's
#s = (reduce(lambda x,y: x if x>y else y, lis))
#dont use list type conversionhere...
print(s)


