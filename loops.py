""" Loops """

""" 

for iterador in collection:
    sentences


while condition:
    sentences

"""

nombres = ["Hugo", "Paco", "Luis"]

for i in range(1, 10): # start = 0, stop = ?, step = 1 
    print(i)
    
for i in range(len(nombres)):
    print(nombres[i])
    
for nombre in nombres:
    print(nombre)
    
    
indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice+=1
    
    
nombres_uppercase = [ name.upper() for name in nombres]
print(nombres_uppercase)


nombres_uppercase2 = list(map(lambda name: name.upper(), nombres))
print(nombres_uppercase2)


def filter_names(name):
    return True if 'a' in name else False

nombres_filtrados = list(filter(filter_names, nombres))
print(nombres_filtrados)