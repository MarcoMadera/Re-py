string = "Marco"
print(len(string)) # return the length of the string

for i in range(len(string)):
  print(string[i])

print(string.capitalize())                #Marco
print(string.casefold())                  #Marco
print(string.center(len(string)+6,'-'))   #---Marco---
print(string.find('r'))                   #2
print(string.lower())                     #marco
print(string.upper())                     #MARCO
print(string.split(' '))                  #['Marco']
print(string.join('----'))                #-Marco-Marco-Marco-
print(string.startswith('m'))             #False
print(string.endswith('o'))               #True
print(string[1:])                         #arco
print(string[1:3])                        #ar
print(string[1:5:2])                      #ac
