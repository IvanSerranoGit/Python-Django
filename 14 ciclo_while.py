def run():
    # cONSTANTE EN MAYUSCULAS
    LIMITE = 1000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
      print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))  
      contador = contador +1
      potencia_2 = 2**contador

if __name__ == '__main__':
    run()


contador = 1
print(contador)
while contador < 1000:
    contador += 1
    print(contador)

# def run():S
#     LIMITE = 1000000
#     contador = 0
#     pontencia_2 = 2**contador
#     while pontencia_2 < LIMITE:
#         print(f'2 elevado a la {contador} es igual a {pontencia_2}')
#         contador = contador + 1
#         pontencia_2 = 2**contador

# if __name__ == "__main__":
#     run()

# Para que no tengan que poner el str en el print lo mejor es poner f’ ’ y las variables entre corchetes {}.


# Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True).

# La sintaxis del bucle while es la siguiente:

# while condicion:
#     cuerpo del bucle
# Python evalúa la condición:
# si el resultado es True se ejecuta el cuerpo del bucle. Una vez ejecutado el cuerpo del bucle, se repite el proceso (se evalúa de nuevo la condición y, si es cierta, se ejecuta de nuevo el cuerpo del bucle) una y otra vez mientras la condición sea cierta.
# Si el resultado es False , el cuerpo del bucle no se ejecuta y continúa la ejecución del resto del programa.