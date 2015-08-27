__author__ = 'tyler'

print "This line will be printed."
print "Then this guy..."

x = 1
if x == 1:
    print "x is 1."

print "Hello world!"

myint = 7

myfloat = 7.0
myfloat = float(7)

mystring = 'hello'
mystring = "hello"


a, b = 3, 4

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print x

number = 1 + 2 * 3 / 4.0

remainder = 11 % 3

squared = 7 ** 2

cubed = 2 ** 3

helloworld = "hello" + " " "world"

lotsofhellos = "hello" * 10

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers

name = "John"
print "Hello, %s!" %name

age = 23

print "%s is %d years old." %(name, age)

mylist = [1, 2, 3]
print "A list: %s" % mylist

astring = "Hello world!"

print len(astring)
print astring.index("o")
print astring.count("l")
print astring.upper()
print astring.lower()
print astring.startswith("Hello")
print astring.endswith("asdfasdfasdf")
afewwords = astring.split(" ")

x = 2
print x == 2
print x == 3
print x < 3

name = "John"
age = 23
if name == "John" and age == 23:
    print "Your name is JOhn, and you are also 23 years old."

if name == "John" or name == "Rick":
    print "Your name is either John or Rick"

if name in ["John", "Rick"]:
    print "Your name is on the guest list, and is either John or Rick."

x = 2
if x == 2:
    print "x equals two!"
else:
    print "x does not equal two"

x = [1, 2, 3]
y = [1, 2, 3]
print x == y
print x is y


print not False
print (not False) == (False)

primes = [2, 3, 5, 7]
for prime in primes:
    print prime

for x in xrange(5):
    print x

for x in xrange(3, 6):
    print x

for x in xrange(3, 8, 2):
    print x

count = 0
while count < 5:
    print count
    count += 1

count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

for x in xrange(10):
    if x % 2 == 0:
        continue
    print x

def my_function():
    print "Hello From My Function!"

def my_function_with_args(username, greeting):
    print "Hello, %s, From My Function!, I wish you %s" %(username, greeting)

def sum_two_numbers(a, b):
    return a + b

my_function()

my_function_with_args("John Doe", "a great year")

x = sum_two_numbers(1,2)

#from Bio import SeqIO

#SeqIO.FastaIO.Seq





