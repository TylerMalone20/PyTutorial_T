__author__ = 'tyler'

class MyClass:
    variable = "blah"

    def function(self):
        print "This is a message inside the class."

myobjectx = MyClass()

print myobjectx.variable

myobjecty = MyClass()

myobjecty.variable = "yackity"

print myobjectx.variable
print myobjecty.variable

myobjectx.function()

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

#Alternatively
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)

del phonebook["John"]

#Alternatively

phonebook.pop("Jack")

import urllib


