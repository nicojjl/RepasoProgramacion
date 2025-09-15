#Listas
lista = [1, 2, 3, 4, "A","a"]
print(lista)
#imprimir un elemento: print(lista[3])
#modificar un elemento
lista[0] = 10 #primer elemento es la posicion 0
lista[3] = "B"
print(lista[3])
lista.append(6) #agrega un elemento al final
print(lista) #se agrego el 6 a la lista
lista.remove("a") #elimina el elemento "a"
print(lista)

#Tuplas (son inmutables)
tupla = (1, 2, 3, 4, "A","a")
print(tupla)
#tupla(1) = 10 Error, no se puede modificar

#Diccionarios (key-value)

diccionario = {
    "nombre": "nico",
    "apellido": "silva",
    "edad": 19,
    "esEstudiante": True
}
print(diccionario)
#imprimir un valor de diccionario
print(diccionario["nombre"])

#modificar un elemento del diccionario

diccionario["nombre"] = "pedro" 
print(diccionario["nombre"])

#Conjuntos (no tienen elementos repetidos)
conjunto = {1, 2, 3, 4, 4, 4, "A","a","A"}
conjuto2 = {3, 4, 5, 6}
print(conjunto) #no se repite el 4 ni la "A"

#Operaciones con conjuntos
union = conjunto.union(conjuto2) #une los dos conjuntos
print(union) #resultado: {1, 2, 3, 4, 5, 6, 'A', 'a'}
interseccion = conjunto.intersection(conjuto2) #elementos en comun
print(interseccion) #resultado: {3, 4}