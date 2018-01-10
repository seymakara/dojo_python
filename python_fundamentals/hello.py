def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + ' from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'
say_hello('seyma')

name = "Zen"
print "My name is comma", 5

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 5
print hw

x = "Buyuk harf"
print x.upper()

str = "this is string example....wow!!!"

sub = "i"
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow"
print "str.count(sub) : ", str.count(sub)

suffix = "wow!!!"
print "wow", str.endswith(suffix)
print "wow20", str.endswith(suffix,20)

suffix = "is"
print "wow2-4", str.endswith(suffix, 2, 4)
print "wow2-6", str.endswith(suffix, 2, 6)

str1 = "this is string example....wow!!!"
str2 = "exam"
print "exam", str1.find(str2)
print "exam10", str1.find(str2, 10)
print "exam40", str1.find(str2, 40)

str = "this2009"  # No space in this string, parameters: NA
print "isalnum1", str.isalnum()

str = "this is string example....wow!!!"
print "isalnum2", str.isalnum()

str = "THIS is string example....wow!!!"
print "is it all lower?", str.islower()

str = "this is string example....wow!!!"
print "is it all lower?", str.islower()

str = "this";  # No space & digit in this string
print "is it alphabetic characters only?", str.isalpha()

str = "this is string example....wow!!!"
print "is it alphabetic characters only?", str.isalpha()

s = " "
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )
print str.split(' ', 2 ) 
'''str.split(str="", num=string.count(str)). 
str − This is any delimeter, by default it is space. 
num - limiting the number of splits to num.'''
