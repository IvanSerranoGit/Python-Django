objetos = ['hola', 3, 4.5, True]

print(objetos)

objetos.append(False)
print(objetos)
objetos.pop(3)
print(objetos)

for elemento in objetos:
	print(elemento)

objetos[ : : -1]
print(objetos)