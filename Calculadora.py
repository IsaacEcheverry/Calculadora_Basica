signos = ["*","/","-","+"] #lista de signos que se pueden usar

sign = str(input("Ingrese el signo que va a utilizar: ")) #Signo ingresado que se va a utilizar

while not sign in signos: # determinar si uso un signo correcto
    print ("Has ingresado un signo incorrecto - Los signos validos son: +, -, /, *")
    sign = str(input("Ingrese el signo que va a utilizar: "))

lista_num = [] # Ingreso de numeros que se van a restar, multiplicar...
espacio = "~"
while espacio != "":
    valor = input("Ingrese los numeros que quiere usar - Cuando quiera ver el resultado presione: enter")
    
    if valor == "": # Agregar los numeros ingresados a la lista
        espacio = valor
    else:
        lista_num.append(int(valor))



if sign == "/" or sign == "-": # Idetificar si al momento de dividir hay ceros para eliminarlos
    cont = 0
    for number in lista_num:
        if number == 0:
            lista_num.pop(cont)
        cont = cont + 1
print (lista_num)
    

s = "suma:"
m = "multiplicacion:"
d = "divicion:"
r = "resta:"

def suma (lista_num): # Suma
    resultado = 0
    for valor in lista_num:
        resultado = resultado + valor
    print (s , resultado)
    
if sign == "+": # Procedimiento
    suma (lista_num)
else:
    print ("")
    
def resta (lista_num): # Resta
    resultado = 0
    if len(lista_num) > 0: # Identifica ceros y los elimina
        ceros = 0
        for valor in lista_num:
            if ceros == 0:
                resultado = valor
            else:
                resultado = resultado - valor
            ceros = ceros + 1
        print (r , resultado)
        
if sign == "-": # Procedimiento
    resta (lista_num)
else:
    print ("")
    
def divicion (lista_num): # Divicion
    resultado = 0
    if len(lista_num) > 0: # Identificar si hay mas de 2 terminos
        ceros = 0
        for valor in lista_num:
            if ceros == 0:
                resultado = valor
            else:
                resultado = resultado / valor
            ceros = ceros + 1
        print (d , resultado)
    else:        
        print ("Para dividir se nesecitan almenos 2 números")
    

if sign == "/": # Procedimiento
    divicion (lista_num)

else:
    print ("")

def multiplicacion (lista_num): # Multiplicacion
    resultado = 0
    for valor in lista_num:
        resultado = resultado * valor
    print (m , resultado)
    
if sign == ("*"): # Procedimiento
    multiplicacion (lista_num)

else:
    print ("")
