"""def common_latter():

    str1=input("enter 1st latter")
    str2=input("enter 2nd latter")

    s1 = set(str1)
    s2 = set(str2)

    lst= s1 & s2
    print(lst)
common_latter()"""

d={'1':'z','2':'v','3':'b','4':'c'}
for x,y in d.items():
    print(x,y)




list = [1,2,3,4,5]

list2 = list[::-1]

print(list2)

sentence = "rishi is 26 yr old he is got 120 rankes"
num = []

for word in sentence.split():
    if word.isdigit():
        num.append(word)

    print(num)
""""
arr = [1,4,2,4,7,4,6,4,4,57,4]

arr1 = set(arr)
print(arr1)
num1 = int(input("enter 1st no"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))
def smallest_number(num1,num2,num3):
    if num1<num2 and num1<num3:
        print("1st number is smallest number")
    elif num2<num1 and num2< num3:
        print("2nd is smallest number")
    else:
        print("3rd number is smallest  number")
smallest_number(num1,num2,num3)




lis = []
num = int(input("how many u want"))
for i in range(1,num1):
    element = int (input("enter extact number"))
lis.append(element)

print("original no is ",lis)
print("the largest number is =",lis)




lis = []
num = int(input("how many u want"))
for i in range(1,num+1):
    statement = int(input("eneter number:"))
    lis.append(statement)
print("orginal list is :",lis)
print("max number is ;",list [-1])





s = tuple(filter(lambda fruit: 'a' in fruit, ["mango", "apple", "cherry"]))
print(s)


lis = [2,4,6,7,8,9] #reduce it to one value #sum avg
#s = (reduce(lambda x,y: x+y, lis)) #addition of all number's
s = (reduce(lambda x,y: x if x>y else y, lis))
#dont use list type conversionhere...
print(s)





num1 = input("enter num 1:")
num2 = input("enter num2 ;")

print("value of num 1 before swap",num1)
print("value of num 1 before swap",num2)

temp = num1
num1 = num2
num2 = temp

print("values after swap =",num1)
print("values after swap = ",num2)


num = input("enter number=")

count = 0

if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print("numberis prime")
    else:
        print("number is not prime no")



"""""

n1 = 0
n2 = 1

print(n1)
print(n2)
for i in range(1,10):
    sum  = n1 + n2
    print(sum)
    n1=n2
    n2=n1


for i in range(2,10):
    sum = n1+n2
    print(sum)
    n1=n2
    n2=sum


try:
    x = 00
    print(x)
except:
    print("something went wrong")
else:
    print("nothing went wrong ")
finally:
    print("file closed")






x = 19
if x <= 18:
  raise Exception("Sorry,Your age is not acceptable for Voting.")

try:
  f = open("demofile.txt")# default read mode
  try:
    f.write("Hello world")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Please check a file permission when opening the file")

class university:
    collage = "sgbau"
    dpt     = "meachanical"
    rank    = 3

    def run(self):
        print("best colllage id= ",self.collage)
        print("and best department in sgbau is = ",self.dpt)
        print("overall rank is = ",self.rank)

obj = university()
print(obj.collage)
print(obj.dpt)
print(obj.rank)
obj.run()


class fruits:
    def __init__(self,name,price,id):
        self.name = name
        self.price = price
        self.id = id

    def value(self):
        print("the fruits is = ",
              self.name,"price is = ",
              self.price,"id = ",self.id)

fruits_obj = fruits("mango",30,142436)
fruits_obj2 = fruits("kiwi",50,12324)

print(fruits_obj.name)
print(fruits_obj2.price)
print(fruits_obj.id)

fruits_obj.value()
fruits_obj2.value()


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x,'=', y)

  fruits = ["apple", "banana", "cherry", 10, 20.3, 11]
  for x in fruits:
      if x == "cherry":
          continue
      print(x)



for i in range(211,215):
  print(i)

for i in range(1, 11):
    if i % 2 == 1:
        print(i)

for i in range(1,11):
  if i % 2 == 0:
    print(i)



from datetime import date
curr_date = date.today()
print(curr_date)

import datetime
now = datetime.datetime.now()
print(now)
curr_time = now.strftime("%H:%M:%S")
print("current time is:- ", curr_time)


from datetime import datetime, timedelta
diff = datetime.today() - timedelta(days=365)
print(diff) #returns the complete date.
print(diff.year)
print(diff.month)
print(diff.day)



class Fruit:
    def __init__(self, name, price, mono): #constructor
        self.name = name #initilization (exact assigning the value)
        self.price = price #price = 400
        self.mono = mono
    def value(self):
        print("Fruit name is", self.name, "and price is", self.price,". Please react out to", self.mono)
    def contact(self):
        print("contact number - ", self.mono)
# use only one constructor per class(limitation)
fruit_obj = Fruit("Mango", 200, 123456789)
fruit_obj2 = Fruit("Watermelon", 400, 123456789)
print(fruit_obj.name)
print(fruit_obj.price)
fruit_obj.value()
fruit_obj.contact()
fruit_obj2.value()

class university:
    def __init__(self,name,collage,rank):
        self.name = name
        self.collage = collage
        self.rank = rank
    def value(self):
        print("The university name is =",self.name,"collage is =",self.collage,"And rank in whole university is =",self.rank)
uni_obj = university("SGBAU","pote collage","A+++")
uni_obj2 = university("Pune university","D.Y.Patil collage","B++")
print(uni_obj.name)
print(uni_obj.collage)
uni_obj.value()
uni_obj2.value()


class library:
    def __init__(self,name,candidate,seats):
        self.name = name
        self.candidate = candidate
        self.seats = seats
    def value(self):
        print("the lab name is = ",self.name,"....canditates name  is = ",self.candidate,"...seats no reserve =",self.seats)
sent_no = library("yashogeet","sarjan_bhau","23")
sent_no2 = library("yashogeet","kunal","27")
sent_no3 = library("yashogeet","rishi","29")

print(sent_no.name)
print(sent_no2.candidate)
print(sent_no3.seats)

sent_no.value()
sent_no2.value()
sent_no3.value()


