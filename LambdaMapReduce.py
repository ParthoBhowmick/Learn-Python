x = lambda x,y : x+y
print(x(1,3))

# use lambda as other function
sample_list = [('eggs',7.34),('chicken',150),('fish',100)]
print(sample_list)

# sort by value
sample_list.sort(key=lambda x: x[1])
print(sample_list)

#sort by key
sample_list.sort(key=lambda x: x[0])
print(sample_list)

sample_list2 = [{'name': 'bo','age' : 23},{'name' : 'naga', 'age' : 48},{'name':'joma','age' : 21}]
sample_list2 = sorted(sample_list2,key = lambda x:x['age'])
print(sample_list2)

# filter function
odds  = lambda x : x%2==1
sample_list3 = [1,2,3,4,4,5,6,7,8,4,34]
print(list(filter(odds,sample_list3)))

#print(str(8+9) + ' is odd')

#map function
print(list(map(lambda  x: x**2, list(filter(odds,sample_list3)))))

# lambda conditional function
starts_with_J = lambda x : True if x.startswith('J') else False
print(starts_with_J('Joma'))

wordb4 = lambda s,w : s.split()[s.split().index(w)-1] if w in s else None
print(wordb4('Four score and seventy years ago','seven'))
