# # Las variables en python son de tipo dinamica

# strNombre = "Roberto Eduardo Guzmán Ruiz"
# fltNumero = 0.01
# intNumero = 10
# print(intNumero)

# Comparaciones en python
# boolData = True
# if boolData:
#     print("Si es verdadero")
# elif boolData == False:
#     print("No es verdadero")

# sumaUno = 10
# sumaDos = 11

# resultado = sumaUno + sumaDos

# print(resultado)

# # Cade de String
# strNombre = 'Roberto Eduardo Guzmán Ruiz'
# indexStart = 0
# indexEnd = 18
# print(strNombre[-5:] + strNombre[-5:])


# # Listas

lista = [1, 2, 3, 4, 5]
lista = lista + [6, 7, 8, 9]
lista += [10, 11, 12, 13]

listaAnterior = ["A", "B", "C", "D", "E", "F"]
listaNueva = ["G","H", "I", "J", "K", "L", "M"]

listaTotal = [*listaAnterior, *listaNueva]

listaTotal.append("O")

print(listaTotal)