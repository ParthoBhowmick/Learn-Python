# working with textual data
# author -  partho 20 dec 2019\

message = 'Hello world' 
print(message)

message2 = 'Hello\'s world' 
# also can be written "hello's world"
print (message2)

multiline_message = '''hello world .. 
this is python!!'''
print(multiline_message)


#length
print(len(message))

#count -> counts the total occurance of a given string 
print(message.count('l'))
print(message.count('Hello')) 

#find -> return the index where the given string starts 
print(message.find('world'))
print(message.find('hello'))

print(message[6:])
print(message[:5])

#string replace function return a new string 
message = message.replace("world","universe")
print(message)

#string concatetion 
greeting = "Hello" 
name = "Python" 

print(greeting + '  ' + name + ', Welcome')
print('{}  {} , Welcome'.format(greeting,name))
print(f'{greeting}  {name} , Welcome')

#find related function that attached to a variable
print(dir(name))

#find the function description of type 
print(help(str))
print(help(str.lower))