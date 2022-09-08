import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))
phone = phonebook['Chris']
print(phone)
print(len(phonebook))

mydictionary = dict(m=8,n=9)
print(mydictionary)

#if you want to clear dictionary
mydict={}
print(mydict)
print()
print('*****  end section 1 ********')
print()


'''


print()
print('*****  start section 2 - search dictionary ********')
print()
'''
name = 'chris'
if name in phonebook:
    print(phonebook[name])
else:
    print(name, 'not found')



'''

print()
print('*****  end section 2 ********')
print()
'''







print()
print('*****  start section 3 - edit/append dictionary ********')
print()
print(phonebook)
phonebook['Chris'] = '555-0123'
phonebook['Joe'] = '555-4444'

print(phonebook)


'''
print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()
'''
#del phonebook ['Chris']
#print(phonebook)



print()
print('*****  end section 4 ********')
print()
'''

'''



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()
#it just iterate for the key, if you want to iterate other things, you need to 
for k in phonebook:
    print(k)
    print(phonebook[k])

for value in phonebook.values():
    print(value)#it will print out the value on the key

for k,v in phonebook.items():
    print('key:',k,'     value:  ',v)
for tuple in phonebook.items():
    print(tuple)#it will return the tuple 
print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("chris","key not found")#if get it, apply on left, otherwise on right
print(phone)

#phonebook.clear()
#print(phonebook)
#which will clear phonebook content


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#remove=phonebook.pop('Chris','key not found')
#print(remove)
#print(phonebook)





print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()

#select the random 

#a = phonebook.popitem()#it suppose to pick up the random, but it pick the last item 
#print(a)
#print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)#
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))])#exact same thing on the upper list.
print()
print('*****  end section 9 ********')
print()







