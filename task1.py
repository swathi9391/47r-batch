# create a string with your name and print
name="cristiano ronaldoo"
print(name)

# first charecter from the string
name="rahul chowdary"
first_char=name[0]
print(first_char)

#last charecter from the string
name="dhoni"
last_char=name[-1]
print(last_char)

#concatenate two strings
name="my favorite player is"
name2="shreyas iyyer"
a=name+" "+name2
print(a)

#repeat a string 3 times
game="chess"
print(game*3)

#slice the first five charecters
name="roman reigns"
print(name[5::])


#reverse a string using slicing
word="mirchi"
print(word[::-1])


#chech if a substring exists in a string
string1="luchbox"
string2="box"
if string2 in string1:
    print("yes")
else:
    print("no")
 
#length of string  
name="michel jackson"   
print(len(name))
    
    
# convert sting to uppercase    
word="raj"
word2=word.upper()
print(word2)

#convert sting to lowercase
word="RAJ"
word2=word.lower()
print(word2)

# captilize the first letter
name="live a little darling"
print(name.capitalize())

#convert to string to title case
name="live a little darling"
print(name.title())

#remove  leading spaces using l strip
word="     prabhs is very handsome     "
print(len(word))
word2=word.lstrip()
print(word2,len(word2))

word2=word.rstrip()
print(word2,len(word2))

