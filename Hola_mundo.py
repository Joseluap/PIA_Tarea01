
# Crear archivo txt Python

def createFile(content, path = 'files/Hola_Mundo.txt'):
	with open(path, 'w') as file:
		file.write(content)

print('------------------------------')
print("Creación de archivos")
print('------------------------------')

# fileName = input('Nombre: ')
# fileContent = input('Escriba el contenido: ')
# createFile(fileContent, f'files/{fileName}.txt')
