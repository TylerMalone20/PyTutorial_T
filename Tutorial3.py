__author__ = 'tyler'

import random

def lottery():
    for i in xrange(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)

for random_number in lottery():
    print "And the next number is... %d!" % random_number

##### Next #####

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))

#Alternatively

word_lengths = [len(word) for word in words if word != "the"]

def foo(first, second, third, *therest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(therest)

foo(1, 2, 3, 4, 5)

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print "Result: %d" % result

############# Exception Handling #############

def do_stuff_with_number(n):
    print n

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError:
        do_stuff_with_number(0)

############## Sets ###################

print set("my name is Eric and Eric is my name".split())

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print a.intersection(b)
print a.symmetric_difference(b)
print a.difference(b)
print a.union(b)


############# File i/o #################

my_list = [i**2 for i in range(1,11)]

f = open("Output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.write("fishtaco")
f.close()

read_file = open("Output.txt", "r")

print read_file.read()

read_file = open("Output.txt", "r")
for line in read_file:
    print line + " yup"




