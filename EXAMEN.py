#Valor abosluto de un número:
n = float(input("Dame un nº: "))
valor = n if n >= 0 else -n
print("El valor absoluto es:", valor)

#Pasar el numero de una lista a letras (Ej: 59=cincuenta y nueva)
#En vez de usar "elif" se podría usar if, útil para evitar confusiones en otros ejerdcicios
n = int(input("Dime un número entre 1 y 99:"))
p = ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
s = ["","once","doce","trece","catorce","quize","dieciseis","diecisiete","dieciocho","dicinueve"]
f = ["","","veinte","trenta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
if n > 0 and n < 11:
    print(p[n])
elif n >= 11 and n < 20:
    r = n-10
    print(s[r])
elif n >=20 and n < 100:
    r1 =  n//10
    r2 = n%10
    if r2 ==0:
        print(f[r1])
    else:
        print(f[r1], "y", p[r2])

#DNI predicción
l = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
DNI = int(input("Dime los dígitos de tu DNI"))
let = DNI%23
print("Tu DNI es", DNI,l[let])

#Imprimir valores entre 2 números
i = 10
while i <=20:
    print(i)
    i+=1
#ALTERNATIVA:
n = int(input("Dame un numero: "))
l = int(input("Dame un límite: "))
for i in range (n,l+1):
    print(i)

#De Farenheit a celsius:
v = int(input("Dame la temperatura en Ferenheit:"))
t = 5/9 * (v - 32)
print("La temperatura en Celsius es:", t,"º")
#TABLA:
i = 0
for i in range (0,121,10):
    v = 5/9 * (i-32)
    print("Grados Farenheit:", i, "|" "Grados celisus:", v)
#Si se necesita hacer una cuenta la variable siempre tendra que tener un valor

#NUMEROS PARES entre 2 numeros:
n1 = int(input("Dame el 1º número: "))
n2 = int(input("Dame el 2º número: "))
if n1 > n2:
    for i in range (n2,n1+1):
        if i % 2==0:
            print(i)
elif n2 > n1:
    for i in range (n1,n2+1):
        if i % 2==0:
            print(i)

#NUMEROS TRIANGULARES:
n = int(input("Dime un número: "))
r = int(input("Dime el rango: "))
for i in range (1,r +1):
    rest = i * (i+1)//2
    print(i, "-", rest)

#FACTORIAL:
n = int(input("Cuantos número quieres: "))
for i in range (1,n+1):
    p = int(input("Dame el número: "))
    fact = 1
    for r in range (fact, p+1):
        fact = fact*r
        print(fact)

#Lineas de domino SIN REPETIR
n = int(input("Cuantos número quieres?: "))
for i in range (0,n+1):
    for r in range (i, n+1):
        i = i+0
        print(i,"-",r)

#Calcular CANTIDAD de numeros positivos, negativos y ceros que hay en un grupo de 10 números:
ceros = 0
positivo = 0
negativo = 0
for i in range (10):
    num = int(input("Dame 10 números: "))
    if num == 0:
        ceros = ceros + 1
    elif num >= 1:
        positivo = positivo + 1
    elif num <= -1:
        negativo = negativo+ 1
print("As introducido", ceros, "ceros")
print("As introducido", positivo, "números positivos")
print("As introducido", negativo, "números negatvos")

#Area de un triangulo VALIDANDO que no haya numeros negativos:
b = int(input("Dame la base: "))
a = int(input("Dame la altura: "))
if a and b >= 0:
    result = b*a
    print("El área es:",result)
elif b and a <= 0:
    while b and a<= 0:
        pregunta1 = int(input("Dame una base positiva: "))
        pregunta2 = int(input("Dame la altura positiva: "))
        if pregunta1 >=0 and pregunta2 >=0:
            result = pregunta1*pregunta2
            print("El área es:",result)
            break
elif b <= 0:
    while b <= 0 and a >=0:
        pregunta1 = int(input("Dame una base positiva: "))
        if pregunta1 >=0:
            result = pregunta1*a
            print("El área es:",result)
            break
elif a <= 0:
    while a <= 0 and b >=0:
        pregunta2 = int(input("Dame una altura positiva: "))
        if pregunta2 >=0:
            result= b*pregunta2
            print("El área es:",result)
            break

#TABLA DE MULTIPLICAR:
n = int(input("Dame un número: "))
while n > 0:
    for i in range (1,11):
        i = i * n
        print(i)
    n = int(input("Dame un número: "))
    if n == 0:
        break

#Codifica un programa que lea o soldo de cada un dos traballadores dunha empresa e obteña o número deles que ganan entre 1000 e 1750 €, ámbolos dous incluídos e, a porcentaxe de traballadores que ganan menos de 1000 €. Tendo en conta que non se coñece con antelación o numero de traballadores da empresa e non se admiten os soldos negativos (utiliza como condición de fin un soldo 0).
n = 1
i = 0
t = 0
sueld = 1
while n > 0:
    sueld = int(input("Cuanto cobras: "))
    if sueld >= 1000 and sueld <= 1750:
        i = i + 1
        print("Cobran entre 1000€ y 1750€ un total de:",i,"tabajadores")
    if sueld < 0 or sueld > 1750:
        print("ERROR")
    elif sueld == 0:
        break
    if sueld <= 1000 and sueld > 0:
        t = t + 1
        calc = (t*100)/(i+1)
        print("El porcentaje de los que cobra menos de 1000€ es del",calc,"%")

#PIRAMIDE:
n = int(input("Dame un número: "))
for i in range (1, n+1):
    print(" " * (n - i) + "* " * i)

#PEDIR NÚMEROS Y CALCULAR SUMA, SI SE DA LA CONDICIÓN DE SALIDA MOSTRAR LA SUMA DE LOS NÚMEROS QUE SE HAYAN INTRODUCIDO SIN LLEGAR AL LÍMITE:
suma = 0
for i in range (10):
    n = int(input("Dame un número: "))
    if n == 999:
        break
    suma+=n
print(suma)

#AÑADIR VALORES=
#variable = {}

#DAR VALORES A UNA LISTA
asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
notas = {}
for asignatura in asignaturas:
    nota = int(input(f"¿Que sacaste en {asignatura}?: "))
    notas[asignatura] = nota
for asignatura in asignaturas:
    print(f"Sacaste un {notas[asignatura]} en {asignatura}")

#NUEVA LISTA=
#lista_nueva = []
#lista_nueva.append(valores que queremos que tenga)

#ORDENAR DE MENOR A MAYOR
#lista.sort()

#PRINT SIN []
#*variable#

#RANGO QUE QUEREMOS ABARCAR
#lista[principio:fin:saltos]

#SEPARACIÓN QUE QUEREMOS PARA LOS VALORES
#sep="/" (o , . * ...)

#ORDEN DE MENOR A MAYOR:
numeros = []
for numero in range (8):
    loteria = int(input("Dime los número ganadores: "))
    numeros.append(loteria)
numeros.sort()
print("El numero de la lotería ordenado es :")
print(*numeros[0:8], sep="/")

#ORDEN INVERSO
#lista[::-1]
lista = [1,2,3,4,5,6,7,8,9,10]
print(*lista[::-1], sep =",")

#Escribir un programa que almacene as asignaturas dun curso (por exemplo Matemáticas, Física, Química, Historia e Língua) nunha lista, pregunte o usuario a nota que sacou en cada asignatura e elimine da lista as asignaturas aprobadas. O fin, o programa debe mostrar por pantalla as asignaturas que o usuario ten que repetir.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = {}
for asignatura in asignaturas:
    nota = int(input(f"¿Qué sacaste en {asignatura}?: "))
    notas[asignatura] = nota
print("Tienes que repetir: ")
for asignatura in asignaturas:
    if notas[asignatura] <5:
        print (asignatura)

#Dar valor a una lista:
#len(lista)
#En el ejemplo a=0, b=1 ... z=26

#Posiciones MULTIPLOS DE 3
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
sin = []
for letra in range(len(letras)):
    if (letra + 1) % 3!= 0:
        sin.append(letras[letra])
print(sin)

#PALINDROMO:
palabra = input("Dime una palabra: ")
if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#CONTAR CUENTAS VECES ESTA UN VALOR=
#lista.count(valor)

#CONTAR vocales (valor específico en una lista):
vocales = ["a","e","i","o","u"]
palabras = input("Dime una palabra: ")
for vocal in vocales:
    numero = palabras.count(vocal)
    print(f"{vocal} aparece {numero} veces")

#VALOR MAYOR Y MENOR DE UNA LISTA:
prezos = [50, 75, 46, 22, 80, 65, 8]
print(f"El precio mas bajo es: {min(prezos)}")
print(f"El precio mas alto es: {max(prezos)}")

#PRODUCTO ESCALAR:
vector = [1,2,3]
vecto = [-1,0,2]
lista = [vector[0]*vecto[0]+vector[1]*vecto[1]+vector[2]*vecto[2]]
print(lista)

#PRODUCTO MATRICES.
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
vector3 = [-1, 0]
vector4 = [0, 1]
vector5 = [1, 1]
lista = [
    [vector1[0]*vector3[0] + vector1[1]*vector4[0] + vector1[2]*vector5[0],
     vector1[0]*vector3[1] + vector1[1]*vector4[1] + vector1[2]*vector5[1]],
    [vector2[0]*vector3[0] + vector2[1]*vector4[0] + vector2[2]*vector5[0],
     vector2[0]*vector3[1] + vector2[1]*vector4[1] + vector2[2]*vector5[1]]
]
print("El producto de A x B es:", lista)

#MEDIA Y DESVIACIÓN TÍPICA:
calculo = 0
lista = []
for n in range (5):
    numero = int(input("Dame los números: "))
    lista.append(numero)
    calculo=(numero+calculo)
media = calculo/5
desviacion = 0
for numero in lista:
    desviacion += (numero-media)**2
c = (desviacion/5)**0.5
print("la media es: ",media)
print("La desviación típica es:", desviacion)
print(lista,sep=",")

#LONGITUD TEXTO:
frase = str(input(f"Ingrese una oracion: "))
print(f"La longitud de la frase es: {len(frase)}")

#in significa dentro de

#MOSTRAR CARACTER POR CARACTER:
frase = str("Python")
letras = list(frase)
for letra in letras:
    print(letra)

#CONVERTIR VARIABLE A LISTA
#list(variable)

#INVERTIR TEXTO:
frase = str("Python para todos")
letras = list(frase)
print(*letras[::-1])

#ELIMINAR ESPACIOS:
frase = str("Guido Van Rossum creou Python")
letras = frase.replace(" ","")
print(*letras,sep="")

#CONTAR VOCALES Y CONSONANTES:
frase = str("Python Python Python")
letras = frase.replace(" ","")
vocales = 0
consonantes = 0
for vocal in letras:
    if vocal in "aeiou":
        vocales+=1
    if vocal in "bcdfghjkmlnñpqrstvwxyzBCDFGHJKMLNÑPQRSTVWXYZ":
        consonantes += 1
print(f"La frase tiene {vocales} vocales")
print(f"La frase tiene {consonantes} vocales")

#DIVIDIR TEXTO Y LUEGO CONCATENAR:
frase = str("www.phytonparatodos.com")
cadena = frase
primer = cadena[:10]
segund = frase[10:]
suma = primer+segund
print(primer,segund)
print(suma)

#TRANFORMAR A MAYUSCULAS Y MINUSCULAS:
frase = str("phytoneros")
print(frase)
mayus = frase.upper()
print(mayus)
minus = mayus.lower()
print(minus)

#COMPARAR:
frase = str("phyton")
oracion = str("javascript")
if frase == oracion:
    print("son iguales")
else:
    print("son diferentes")

#SUSTITUIR:
frase = str("jeve jeve jeve")
java = frase.replace("e","a")
print(frase)
print(java)

#Tenta escribir un método, que dado un obxecto da clase str conte diferentes tipos de caracteres. En particular, o método deberá imprimir o número de letras, díxitos e espazos en branco da cadea. Tenta facer un programa que escriba o cálculo da cadea: «Ola, son alumno de DAM1, e son programador desde o 2025».
letras = 0
blanco = 0
frase = str("Ola, son alumno de DAM1, e son programador desde o 2025")
print(f"La frase tiene {len(frase)} dígitos")
for letra in frase:
    if letra in "abcdefghijkmlnñopqrstuvwxyzABCDEFGHIJKMLNÑOPQRSTUVWXYZ":
        letras+=1
print(f"La frase tiene {letras} letras")
for letra in frase:
    if letra in " ":
        blanco+=1
print(f"La frase tiene {blanco} espacios en blanco")

#FUNCION:
#def nombre_de_la_función (variable_que_vamos_a_usar):
#codigo
#nombre_de_la_función(variables_que_vamos_a_usar)

#IMPRIMIR 2 PRIMEROS CARACTERES, 3 ULTIMOS, IMPRIMIR CADA 2 CARACTERES, IMPRIMIR DEL DERECHO Y PEGADO DEL REVES
caracteres = str(input("Dame una cadena de carcateres: "))
def operacion(caracteres):
    list(caracteres)
    print(caracteres[:2])
    print(caracteres[:3])
    print(caracteres[::2])
    print(caracteres+caracteres[::-1])
operacion(caracteres)

#REEMPLAZAR POR UN CARACTER, SEPARAR PALABRAS CON UN CARACTER, REEMPLAZAR LOS DÍGITOS POR UN CARCATER Y INSERTAR CADA 3 DIGITOS:
cadena = str(input("Dame una cadena: "))
caracter = str(input("Dame un carcater: "))
def cadena_caracter(cadena,caracter):
    print(cadena.replace(" ",caracter))
    print(cadena.replace("",caracter))
    nueva_cadena = caracter
    for tres in cadena:
        if tres in cadena:
            nueva_cadena += caracter
    print(nueva_cadena)
    cuatro = ""
    simbolo = 1
    for tres in cadena:
        if tres in cadena:
            if simbolo % 3 == 0:
                cuatro += tres
                cuatro += caracter
            else:
                cuatro += tres
            simbolo += 1
    if cuatro:
        print(cuatro)
cadena_caracter(cadena,caracter)

#código anterior con CANTIDAD MÁXIMA Y MÍNIMA de reemplazos:
cadena = str(input("Dame una cadena: "))
caracter = str(input("Dame un carcater: "))
maximo = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter(cadena,caracter,maximo):
    print(cadena.replace(" ",caracter,maximo))
cadena_caracter(cadena,caracter,maximo)

cadena2 = str(input("Dame una cadena: "))
caracter2 = str(input("Dame un caracter: "))
maximo2 = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter2(cadena2,caracter2,maximo2):
    print(cadena2.replace("",caracter2,maximo2))
cadena_caracter2(cadena2,caracter2,maximo2)

cadena3 = str(input("Dame una cadena: "))
caracter3 = str(input("Dame un carcater: "))
maximo3 = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter3(cadena3,caracter3,maximo3):
    nueva_cadena = ""
    contador = 0
    for tres in cadena3:
        nueva_cadena += tres
        if contador < maximo3:
            nueva_cadena += caracter3
            contador += 1
    print(cadena3,caracter3,maximo3)
cadena_caracter3(cadena3,caracter3,maximo3)

cadena4 = str(input("Dame una cadena: "))
caracter4 = str(input("Dame un carcater: "))
maximo4 = int(input("Cantidad máxima de modificaciones: "))

def cadena_caracter4(cadena4,caracter4,maximo4):
    cuatro = ""
    simbolo = 1
    contador = 0
    for tres in cadena4:
        cuatro += tres
        if simbolo % 3 == 0 and contador < maximo4:
            cuatro += caracter4
            contador += 1
        simbolo += 1
    if cuatro:
        print(cuatro)
cadena_caracter4(cadena4,caracter4,maximo4)

#separaciones de MILES:
numero = input("Dame un numero: ")
puntos = "."
def punto_1(numero,puntos):
    numero = str(numero)
    numero = numero[::-1]
    punto=""
    calc=1
    for rest in numero:
        if rest in numero:
            if calc % 3 == 0:
                punto += rest
                punto += puntos
            else:
                punto += rest
            calc += 1
    if punto:
        print(punto[::-1])
punto_1(numero,puntos)

#DIVIDIR CADENA EN UNA LISTA QUE SEPARA CADA VALOR
#cadena.split()

#SIGLAS, PRIMERA LETRA DE CADA PALABRA DE LA CADENA EN MAYÚSCULA, PALABRA QUE EMPIECEN POR A (cierto carcater)
palabra = str(input("Dame una palabra: "))
def sigla(palabra):
    palabra = palabra.split()
    division = ""
    for palabras in palabra:
        division = division + palabras[0]
    print(division)
sigla(palabra)

palabra2 = str(input("Dame una palabra: "))
def sigla2(palabra2):
    palabra2 = palabra2.split()
    division2 = ""
    for palabra1 in palabra2:
        division2 += palabra1[0].upper() + palabra1[1:].lower() + " "
    print(division2)
sigla2(palabra2)

palabra3 = str(input("Dame una palabra: "))
def sigla3(palabra3):
    palabra3 = palabra3.split()
    division3 = ""
    for palabra2 in palabra3:
        if palabra2[0].lower() == "a":
            division3 += palabra2 + " "
    print(division3)
sigla3(palabra3)

#UNIR CON UN ESPACIO (UNIR)
# " ".join(variable)

#IMPRIMIR SOLO CONSONANTES, VOCALES, SUSTITUIR POR LA SIGUIENTES VOCALL:
palabra = input(str("Dime una palabra: "))
def consonantes (palabra):
    lista = ("bcdfghjkmlnñpqrstvwxyzBCDFGHIJKMLNÑPQRSTVWXYZ")
    conso = ""
    for consonante in palabra:
        if consonante in lista:
            conso += consonante
    print(conso)
consonantes(palabra)

palabra2 = input(str("Dame una palabra: "))
def vocal (palabra2):
    lista = "aeiouAEIOU"
    voca = ""
    for vocales in palabra2:
        if vocales in lista:
            voca += vocales
    print(voca)
vocal(palabra2)

palabra3 = input(str("Dime una palabra: "))
def siguiente(palabra3):
    lista = "aeiou"
    sig = ""
    for siguientes in palabra3:
        if siguientes == "a":
            sig += "e"
        elif siguientes == "e":
            sig += "i"
        elif siguientes == "i":
            sig += "o"
        elif siguientes == "o":
            sig += "u"
        elif siguientes == "u":
            sig += "a"
        else:
            sig += siguientes
    print(sig)
siguiente(palabra3)

#PALÍNDROMO:
palabra = input(str("Dame una palabra: "))
def palin (palabra):
    if palabra == palabra[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
palin(palabra)

#INDICAR SI UNA CADENA ES UNA SUBCADENA, DEVOLVER SOLO EL QUE ESTE ANTES EN EL ORDEN ALFABÉTICO:
palabra = input(str("Dime una palbara: "))
palabra2 = input(str("Dime otra palabra: "))
subcadena = "sub"
def sub(palabra,palabra2,subcadena):
    if palabra in subcadena+palabra2:
        print("Es una subcadena")
    else:
        print("no es una subcadena")
sub(palabra,palabra2,subcadena)

primero = input(str("Dime una palabra: "))
segundo = input(str("Dime otra palabra: "))
def orden (primero,segundo):
    if primero < segundo:
        print(primero)
    else:
        print(segundo)
orden(primero,segundo)

#PASAR BINARIO A DECIMAL:
#(variable, 2)

numero = input("Dame un número: ")
def binario(numero):
    return int(numero, 2)
print("decimal: ",binario(numero))

#COGER LONGITUD DE UNA PALABRA E IMPRIMIR EN ESA LONGITUD CARACTERES, Recibindo unha cadea de caracteres e un caracter, a función terá que comprobar si o caracter está na cadea. A función retornará un String no que aparezan guións e o caracter na posición ou posicións onde coincida na cadea.
palabra2 = input(str("Dime una palabra: "))
caracter2 = input(str("Dime un caracter: "))
raya = str("-")
def guion(palabra2,caracter2,raya):
    resultado = ""
    for palabras in palabra2:
        if palabras == caracter2:
            resultado = resultado + caracter2
        else:
            resultado = resultado + raya
    print(resultado)
guion(palabra2,caracter2,raya)

#VALIDAR CXONTRASEÑA=Escribe a función que permita validar un contasinal, recibindo o contrasinal como parámetro. O contrasinal ten que cumprir as condicións de mínimo 8 caracteres, o menos unha maiúscula, unha minúscula e un número. A función ten que retornar un booleano especificando si é válida ou non.
#SI QUEREMOS VAALIDAR ALGO SIEMPRE TENDRA QUE EMPEZAR EN False
#variable.isupper() es mayuscula...
#and todas las condiciones
#or una de ellas o si se cumple alguna
contraseña = input("Dame tu contraseña: ")
def validar_contraseña(contraseña):
    valido = False
    valido1 = False
    valido2 = False
    valido3 = False
    if len(contraseña) >= 8:
        valido = True
    for contra in contraseña:
        if contra.isupper():
            valido1 = True
        elif contra.islower():
            valido2 = True
        elif contra.isdigit():
            valido3 = True
    return valido and valido1 and valido2 and valido3
print(validar_contraseña(contraseña))

#RETURN LO QUE HACE ES DEVOLVER UN RESULTADO (EJ: def sumar(a, b): return a + b | resultado = sumar(3, 5) | print(resultado)

#FORMATEAR=Escribe a función que permita formatear de nomes. A función ten que eliminar os espazos en branco e poñer en maiúsculas o primeiro caracter d o nome e apelido pasado como parámetro. Finalmente retornará unha cadea co nome e apelidos co formato solicitado.
llamar = input(str("Dime tu nombre y apellido: "))
def nombre (llamar):
    llamar = llamar.split()
    mayus = ""
    for palabra in llamar:
        mayus += palabra[0].upper() + palabra[1:]
    print(mayus)
nombre(llamar)

#Crear a función que permíta realizar un analisis simple de texto. O analizador ten  a función de contar palabras, caracteres e encontrar a palabra mais longa. Mostrar os resultados por pantalla.
palabra = input(str("Dime una frase: "))
def analisis (palabra):
    letras = 0
    for letra in palabra:
        if letra in "abcdefghijkmlnñopqrstuvwxyzABCDEFGHIJKMLNÑOPQRSTUVWXYZ":
            letras = letras+1
    print(f"Tiene {letras} letras")
    caracteres = 0
    for letra in palabra:
        if letra in palabra:
            caracteres = caracteres + 1
    print(f"Tiene {caracteres} caracteres")
    palabras = palabra.split()
    largo = ""
    for letra in palabras:
        if len(letra) > len(largo):
            largo = letra
    print(f"La palabra mas larga es {largo}")
analisis(palabra)

#TUPLA=
#tupla = (1, 2 ,3) ("a","b","d") (1,"a",True)

#CONVERTIR EN TUPLA=
#variable = tuple(variable.split(",")

#INDICAR SI UNA TUPLA ESTA ORDENADA DE MENOR A MAYOR:
lista = input("Dame una tupla: ")
def orden(lista):
    lista = tuple(lista.split(','))
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            print("La tupla no está en orden de menor a mayor")
            return
    print("La tupla está en orden de menor a mayor")
orden(lista)

#INDICAR SI DOS FICHAS DE DOMINO ENCAJAN:
#BOOLEANO ES QUE VA A RECIBIR DE VALOR TRUE O FALSE, ES DECIR, NO HARÁ FALTA UN PRINT
ficha1 = input("Dime la ficha: ")
ficha2 = input("Dime otra: ")
def encaja(ficha1, ficha2):
    ficha1 = tuple(ficha1.split(','))
    ficha2 = tuple(ficha2.split(','))
    valido = False
    for val1 in ficha1:
        for val2 in ficha2:
            if val1 == val2:
                valido = True
    return valido
print(encaja(ficha1, ficha2))

#Escribir unha función que reciba unha tupla con nomes e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’
nombres = ("marta","alan","carlos")
def mensaje (nombres):
    for nombre in nombres:
        print(f"Estimado don/doña {nombre}")
mensaje (nombres)

#Escribir unha función que reciba unha tupla con nomes, unha posición de orixen p e unha cantidade n, e imprima a mensaxe anterior (exercicio 3) para os n nombres que se encontran a partires da posición p.
def mensaje(nombres, p, n):
    for nombre in nombres[p:p+n]:
        print(f"Estimado don/doña {nombre}")
lista_nombres = ("carlos", "alan", "ivan", "adrian", "marta", "martin")
mensaje(lista_nombres, 2, 4)

#Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo, deberán recibir unha tupla de tuplas, contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.
def mensaje(nombres):
    for nombre in nombres:
        if nombre[1] == "h":
            print(f"Hola don {nombre[0]}")
        elif nombre[1] == "m":
            print(f"Hola doña {nombre[0]}")
lista_nombres = (("carlos","h"), ("alan","h"), ("ivan","h"), ("adrian","h"), ("marta","m"), ("martin","h"))
mensaje(lista_nombres)

#DEVOLVER PRIMOS, SUMATORIO, PROMEDIO, FACTORIAL
lista = [1,2,3,4,5,6,7,8,9]
def numeros (n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for n in lista:
    if numeros(n):
        print(f"{n} primo ")
    else:
        print(f"{n} no es primo")
suma = 0
promedio = 0
for n in range (1,n+1):
    suma = suma + n
    promedio = suma//9
print(f"El sumatorio es {suma}, y el promedio {promedio}")
for n in range (1,n+1):
    fact = 1
    for r in range(fact,n+1):
        fact = fact * r
    print(f"el factorial de cada numero es {n}-{fact}")
numeros(lista)

#DEVOLVER 3 LISTAS, UNA CON LOS MENORES DE UN N8UMERO, OTRA MAYORES Y OTRA MULTIPLOS Y IGUALES
lista = [1,2,3,4,5,6,7,8,9,10]
numero = 4
mas = []
menos = []
multiplo = []
igual = []
def numeros (lista,numero):
    for i in lista:
        if i > numero:
            mas.append(i)
        if i < numero:
            menos.append(i)
        if i % numero == 0:
            multiplo.append(i)
        if i == numero:
            igual.append(i)
    print(mas)
    print(menos)
    print(igual)
    print(multiplo)
numeros(lista,numero)

#ORDENAR TUPLA=Escribir unha función que reciba unha lista de tuplas (Apelido, Nome, Inicial_segundo_nome) e devolte unha lista de cadenas onde cada unha conteña primero o nome, logo a inicial cun punto, e logo o apelido.
lista = [("Sande", "Adrian", "D")]
nueva_lista = []
def orden(lista,nueva_lista):
    for apellido, nombre, inicial in lista:
        cadena = f"{nombre} {inicial}. {apellido}"
        nueva_lista.append(cadena)
    print(nueva_lista)
orden(lista,nueva_lista)

#INDICAR REPETICIONES=Escribir unha función empaquetar para unha lista, onde empaquetar significa indicar a repetición de valores consecutivos mediante unha tupla (valor, cantidade de repeticións). Por exemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devoltar [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].
lista = [(1,1,1,3,5,1,1,3,3)]
def empaquetar(lista):
    numeros = lista[0]
    resultado = []
    actual = numeros[0]
    contador = 1
    for numero in numeros[1:]:
        if numero == actual:
            contador += 1
        else:
            resultado.append((actual, contador))
            actual = numero
            contador = 1
    resultado.append((actual, contador))
    print(resultado)
empaquetar(lista)

#SUMA DE MATRICES Y PRODUCTO:
matriz1 = [1,2]
matriz2 = [4,6]
def suma (matriz1,matriz2):
    suma1 = matriz1[0]+matriz2[0]
    suma2 = matriz1[1]+matriz2[1]
    print((f"({suma1},{suma2})"))
suma(matriz1,matriz2)
def producto (matriz1,matriz2):
    suma1 = matriz1[0]*matriz2[0]
    suma2 = matriz1[1]*matriz2[1]
    resultado = suma1 + suma2
    print(resultado)
producto(matriz1,matriz2)

#Pregado de un texto. Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas de como máximo esa lonxitude. As líñas deben cortarse correctamente nos espazos (sen cortar as palabras).
def plegar_texto(texto, max_len):
    palabras = texto.split()
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if len(linea_actual) + len(palabra) + (1 if linea_actual else 0) > max_len:
            lineas.append(linea_actual)
            linea_actual = palabra
        else:
            if linea_actual:
                linea_actual += " " + palabra
            else:
                linea_actual = palabra
    if linea_actual:
        lineas.append(linea_actual)

    return lineas
texto = "Escribir unha función que reciba un texto e unha lonxitude e devolva unha lista de cadeas."
resultado = plegar_texto(texto, 20)
for linea in resultado:
    print(linea)

#AHORCADO COMPLEJO:
import random
import unicodedata
palabras = [
    "apple", "table", "chair", "house", "water", "bread", "light", "music", "sport", "plant",
    "fruit", "style", "world", "sleep", "smile", "drink", "dance", "beach", "cloud", "stone",
    "grass", "heart", "brain", "dream", "power", "quiet", "quick", "happy", "magic", "green",
    "black", "white", "brown", "ocean", "river", "earth", "stars", "shine", "sweet", "sugar",
    "spice", "spicy", "honey", "berry", "peach", "mango", "lemon", "grape", "melon", "olive",
    "onion", "pizza", "pasta", "bacon", "cream", "sauce", "toast", "flour", "salad", "steak",
    "sushi", "curry", "bagel", "donut", "fries", "mocha", "latte", "cocoa", "guava", "papaw",
    "pecan", "maple", "cedar", "birch", "sprig", "coral", "shell", "plank", "brush", "cloth",
    "shirt", "pants", "dress", "scarf", "socks", "shoes", "watch", "phone", "cable", "mouse",
    "print", "paper", "ruler", "paint", "color", "azure", "fauna", "flora"
]
vidas = [   "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\\\n"
            "|  / \\\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\\\n"
            "|  /\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\\\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|  /|\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|   |\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|   O\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|   |\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "_____\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "=========",
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "=========",
            ]
palabra = random.choice(palabras)
guess = ["_"] * len(palabra)
vida = 9
print(vidas[vida])
while "_" in guess:
    print("".join(guess))
    letrat = str(input("Ingresa una letra: ")).lower()
    letrat = unicodedata.normalize("NFD", letrat)
    letra = ""
    for c in letrat:
        if unicodedata.category(c) != 'Mn':
            letra += c
    if letra in palabra:
        pos = []
        for i in range(len(palabra)):
            if palabra[i] == letra:
                guess[i] = letra
    else:
        vida -= 1
        if vida > 0:
            print("La letra no está")
            print(vidas[vida])
        else:
            print("Te quedaste sin vidas")
            guess = palabra
            print("La palabra era: ", guess)
print("Ganaste!!! la palabra era: ", "".join(guess))

#AHORCADO SENCILLO
import random
palabras = ["jotaro kujo", "star platinum", "dio brando", "the world", "joseph joestar", "hermit purple", "josuke higashikata", "crazy diamond", "okuyasu nijimura", "the hand", "koichi hirose", "echoes", "rohan kishibe", "heaven’s door", "giorno giovanna", "gold experience", "bruno bucciarati", "sticky fingers", "narancia ghirga", "aerosmith", "guido mista", "sex pistols", "leone abbacchio", "moody blues", "trish una", "spice girl", "jolyne cujoh", "stone free", "enrico pucci", "made in heaven", "weather report", "foo fighters", "johnny joestar", "tusk", "gyro zeppeli", "yoshikage kira", "killer queen", "caesar zeppeli", "lisa lisa", "hol horse", "lucy steel", "hot pants", "diego brando", "scary monsters", "sandman", "in a silent way", "pocoloco", "hey ya!", "valentine", "dirty deeds done dirt cheap", "mountain tim", "oh! lonesome me", "josuke higashikata (jojolion)", "soft & wet", "yasuho hirose", "paisley park", "jobin higashikata", "speed king", "tooru", "wonder of u", "norisuke higashikata iv", "king nothing", "rai muromuzé", "born this way"]
palabra = random.choice(palabras)
letras_adivinadas = [letra if letra == " " else "_" for letra in palabra]
intentos = 10
print("Estas jugando al ahorcado de JoJo's")
while intentos > 0:
    print("Palabra:", " ".join(letras_adivinadas))
    if "".join(letras_adivinadas) == palabra:
        print("¡Buena! Adivinaste de una:", palabra)
        break
    intento = input("Adivina una letra: ").lower()
    if intento in palabra:
        print("¡Lesgoo, bien hecho!")
        for i in range(len(palabra)):
            if palabra[i] == intento:
                letras_adivinadas[i] = intento
    else:
        print("MAL.")
        intentos -= 1
        print("Te quedan", intentos, "intentos.")
if intentos == 0:
    print("CAGASTE, la palabra era:", palabra)

#CAJAS SUPER:
efectivo = [['2', [50, 4], [20, 5], [0.5, 6]],
            ['1', [20, 15], [10, 5], [0.2, 5], [0.1, 4]],
            ['3', [20, 12], [5, 6], [0.02, 5]]]
def mostrarContidoUnhaCaixa(totalEfectivoCaixas):
    for contidoCaixa in totalEfectivoCaixas:
        caixa = contidoCaixa[0]
        print('O contido da caixa', caixa, 'e:')
        for i in range(1, len(contidoCaixa)):
            if contidoCaixa[i][0] > 2.0:
                print(contidoCaixa[i][1], 'billetes de', contidoCaixa[i][0], 'euros')
            else:
                print(contidoCaixa[i][1], 'moedas de', contidoCaixa[i][0], 'euros')
        print()
mostrarContidoUnhaCaixa(efectivo)

#COMPROBADOR DE FECHAS:
fecha = input("Dime una fecha formato (dd/mm/aaaa): ")
formato_valido = ( len(fecha) == 10 and
                   fecha[2] == "/" and
                   fecha[5] == "/" and " " not in fecha and
                   fecha.replace("/", "").isdigit() )

if formato_valido:
    dia = int(fecha[:2])
    mes = int(fecha[3:5])
    year = int(fecha[6:])
    if 1 <=dia <=31 and 1 <=mes <=12 and year <=2025:
        print("Formato correcto")
    else:
        print("Formato incorrecto")
else:
    print("Formato incorrecto")

#GENERADOR DE CONTRASEÑAS:
import random
num = random.randint(6, 12)
print(num)
passwd = ''
while num != 0:
    passwd += chr(random.randint(33, 126))
    num -= 1
print(passwd)

#GENERADOR DE CONTRASEÑAS PIDIENDO YO EL DÍGITO:
import random
def xeradorContrasinais(n):
    l = ['1234567890', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%^&*()_+-=[]{};:,.<>/?']
    i=0
    contrasinal=''
    while i<n:
        tipo = random.randint(0,3)
        iSim = random.randint(0,len(l[tipo])-1)
        contrasinal = contrasinal + l[tipo][iSim]
        i+=1
    return contrasinal
while True:
    n = int(input("Introduce un numero para xerar a lonxitude do contrasinal: "))
    if n >= 6 and n <=12:
        print(xeradorContrasinais(n))
    elif n ==0:
        break
    else:
        print("a lonxitude valida es entre 6 e 12")

#LISTA DE LA COMPRA:
list_compra = ['Limones', 'Naranjas', 'Queso', 'Pavo']
def añadir_elemento(lista):
    elemento = input('Engadir elemento: ')
    lista.append(elemento)
    print(lista)
def eliminar_elemento(lista):
    print(lista)
    eliminar = str(input('Que elemento desea eliminar: '))
    if eliminar in lista:
        lista.remove(eliminar)
def enseñar_lista(lista):
    print('Tu lista de la compra contiene:')
    for elemento in lista:
        print(elemento)
def menu():
    while True:
        print(''' Opciones:
          [1] Añadir elemento a lista
          [2] Eliminar elemento de lista
          [3] Enseñar lista
          [4] Salir''')
        opcion = int(input('Elija una opcion: '))
        if opcion == 1:
            añadir_elemento(list_compra)
        elif opcion == 2:
            eliminar_elemento(list_compra)
        elif opcion == 3:
            enseñar_lista(list_compra)
        elif opcion == 4:
            break
menu()

#QUITAR ACENTOS:
def eliminar_acentos(cadena):
    reemplazos = (
        ("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
        ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U")
    )
    for a, b in reemplazos:
        cadena = cadena.replace(a, b)
    return cadena

print(eliminar_acentos("Antón foi de viaxe a Ávila."))

#QUITAR ESPACIOS:
frase = str(input("Ingresa una frase: "))
while frase[0] == " ":
    frase = frase[1:]
frase = frase[::-1]
while frase[0] == " ":
    frase = frase[1:]
frase = frase[::-1]
print(frase)


#CLASEEEEES
#COMPROBAR AÑO CORRECTO:
class Data:
    def __init__(self, day, month, year):
        self.day = None
        self.month = None
        self.year = None

        self.setAno(year)
        self.setMes(month)
        self.setDia(day)

    def setDia(self, day):
        dias_mes = {1:31, 2:28, 3:31, 4: 30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        if self.month is None or self.year is None:
            self.day = None
            return

        if self.month == 2 and self.bisiesto(self.year):
            if 1 <= day <=29:
                self.day = day
            else:
                self.day = None
        else:
            if 1<= day <= dias_mes[self.month]:
                self.day = day
            else:
                self.day = None

    def getDia(self):
        return self.day

    def setMes(self, month):
        if 1 <= month <= 12:
            self.month = month
        else:
            self.month = None

    def setAno(self, year):
        if year >= 0:
            self.year = year
        else:
            self.year = None

    def getAno(self):
        return self.year

    def bisiesto(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year%400==0):
            return True
        return False

    def validar(self):
        if self.day is None or self.month is None or self.year is None:
            return False

        dias_mes = {
            1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
        }
        if self.month == 2 and self.bisiesto(self.year):
            return self.day <= 29
        return self.day <= dias_mes[self.month]

    def __str__(self):
        return f"La fecha será {self.day}/{self.month}/{self.year}"

fechas = [
    Data(29,2,2024),
    Data(29,2,2023),
    Data(31,4,2023),
    Data(15,10,2023),
]
for i in fechas:
    print(i)
    if i.validar():
        print("Fecha valida")
    else:
        print("Fecha invalida")
    print("-------")

#BOMBILLA (ON-OFF) ESTADO DE ALGO METODO
class Bombilla:
    def __init__(self, estado):
        self.__estado = estado

    def setEstado(self, estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado

    def acende(self):
        if self.__estado == "ON":
            self.__estado = "ON"
        if self.__estado == "OFF":
            self.__estado = "ON"

    def apaga(self):
        if self.__estado == "OFF":
            self.__estado = "OFF"
        if self.__estado == "ON":
            self.__estado = "OFF"

    def interuptor(self):
        if self.__estado == "OFF":
            self.__estado = "ON"
        if self.__estado == "ON":
            self.__estado = "OFF"

#RESOLUCIOOOOOOON
from Bombilla import Bombilla


bombilla1 = Bombilla("ON")
print(bombilla1.getEstado())

bombilla1.setEstado("OFF")
print(bombilla1.getEstado())

bombilla1.setEstado("OFF")
print(bombilla1.getEstado())


#CILINDRO
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return f"Punto: x = {self.x}, y = {self.y}\n"

class Cilindro(Punto):
    def __init__(self, x, y, radio, altura):
        super().__init__(x, y)
        self.radio = abs(radio)
        self.altura = altura

    def calcularArea(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

    def calcularVolumen(self):
        return math.pi * (self.radio**2) * self.altura

    def toString(self):
        cadena = super().toString()
        cadena += f"Cilindro: radio = {self.radio}, altura = {self.altura}\n"
        return cadena


c = Cilindro(5, 10, 3, 7)

print(c.toString())

print(f"Área del cilindro: {c.calcularArea():.2f}")
print(f"Volumen del cilindro: {c.calcularVolumen():.2f}")


#CIRCULO
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return f"Punto: x = {self.x}, y = {self.y}"

class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = abs(radio)

    def obtenerDiametro(self):
        return self.radio * 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def tostring(self):
        cadea = super().toString() + f" \nRadio: {self.radio}"
        return cadea

c = Circulo(4, 5, 3)
print(c.tostring())
print(f"Diámetro: {c.obtenerDiametro()}")
print(f"Perímetro: {c.calcularPerimetro():.2f}")
print(f"Área: {c.calcularArea():.2f}")


#CONO
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return f"Punto: x = {self.x}, y = {self.y}\n"

class Cono(Punto):
    def __init__(self, x, y, radio, altura):
        super().__init__(x, y)
        self.radio = abs(radio)
        self.altura = altura

    def calcularArea(self):
        return math.pi * self.radio * (self.radio + math.sqrt(self.radio**2 + self.altura**2))

    def calcularVolumen(self):
        return (1/3) * math.pi * (self.radio**2) * self.altura

    def toString(self):
        return super().toString() + f"Cono: radio = {self.radio}, altura = {self.altura}"

c = Cono(3, 4, 5, 6)
print(c.toString())
print(f"Área del cono: {c.calcularArea():.2f}")
print(f"Volumen del cono: {c.calcularVolumen():.2f}")


#COORDENADAS
class Punto2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        if type(x) == int or type(x) == float:
            if x >= 0:
                self.__x = x
            else:
                self.__x = 0
        else:
            self.__x = 0

    def setY(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__y = y
            else:
                self.__y = 0
        else:
            self.__y = 0

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def toString(self):
        cadeaPunto = "As coordenadas do punto son: \n\t x = " + str(self.__x) + " \n\t y = " + str(self.__y)
        return cadeaPunto

    def __str__(self):
        return self.toString()

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    x=property(getX, setX)
    y=property(getY, setY)

punto1 = Punto2(5, 3)
punto2 = Punto2(7, 8)
punto3 = Punto2(-2, 10)

print(punto1)
print(punto2)
print(punto3)

punto1.x = 10
punto1.y = 15

print("\nDespués de modificar punto1:")
print(punto1)

print("\nComparaciones:")
print("punto1 == punto2:", punto1 == punto2)
print("punto1 == punto1:", punto1 == punto1)


#TOROIDE
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)

    def toString(self):
        return f"Punto: x = {self.x}, y = {self.y}"

class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = abs(radio)

    def calcularArea(self):
        return math.pi * self.radio ** 2

    def tostring(self):
        return super().toString() + f" \nRadio: {self.radio}"

class Toroide(Circulo):
    def __init__(self, x, y, radio, centro):
        super().__init__(x, y, radio)
        self.centroToroX = centro.x
        self.centroToroY = centro.y

    def cacularRadioMaior(self):
        return self.distancia(Punto(self.centroToroX, self.centroToroY))

    def calcularRadioMenor(self):
        return self.radio

    def calcularArea(self):
        R = self.cacularRadioMaior()
        r = self.calcularRadioMenor()
        return 4 * math.pi**2 * R * r

    def calcularVolume(self):
        return 2 * math.pi * self.cacularRadioMaior() * self.calcularArea()

c = Punto(0, 0)
t = Toroide(3, 4, 2, c)

print(f"Centro del toroide: ({t.centroToroX}, {t.centroToroY})")
print(f"Radio mayor: {t.cacularRadioMaior():.2f}")
print(f"Radio menor: {t.calcularRadioMenor():.2f}")
print(f"Área del toroide: {t.calcularArea():.2f}")
print(f"Volumen del toroide: {t.calcularVolume():.2f}")


#FECHA DE UN AÑO METODO
class DATA:
    def __init__(self,dia,mes,ano):
        self.setd(dia)
        self.setm(mes)
        self.seta(ano)

    def setd(self, dia):
        if dia <= 1 or dia > 31:
            raise ValueError("El día debe estar entre 1 y 31")
        self.dia = dia

    def setm(self, mes):
        if mes <= 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        self.mes = mes

    def seta(self, ano):
        if ano <= 0:
            raise ValueError("El año debe ser mayor que 0")
        self.ano = ano

    def getd(self):
        return self.dia

    def getm(self):
        return self.mes

    def geta(self):
        return self.ano

    def validezdiames (self,dia,mes,ano):

        if mes == 2:
            if ano%4 == 0:
                if dia <= 29:
                    return True
            else:
                if dia <= 28:
                    return True
        elif mes % 2 == 0:
            if dia <= 30:
                return True
        elif dia <= 31:
            return True

#RESOLUCIOOOOOOOOOOOOOOOOON
from Data import DATA

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
ano = int(input("Introduce el año: "))

fecha = DATA(dia, mes, ano)

resultado = fecha.validezdiames(fecha.getd(), fecha.getm(), fecha.geta())

if resultado == True:
    print("La fecha es válida")
    print("Día:", fecha.getd())
    print("Mes:", fecha.getm())
    print("Año:", fecha.geta())
else:
    print("Fecha inválida:", resultado)


#ESFERA
import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def toString(self):
        return f"Punto: x = {self.x}, y = {self.y}"

class Circulo(Punto):
    def __init__(self, x, y, radio):
        super().__init__(x, y)
        self.radio = abs(radio)

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio

    def tostring(self):
        return super().toString() + f" \nRadio: {self.radio}"

class Esfera(Circulo):
    def __init__(self, x, y, radio):
        super().__init__(x, y, radio)

    def calcularArea(self):
        return 4 * super().calcularArea()

    def calcularVolume(self):
        return (4/3) * math.pi * (self.radio ** 3)

e = Esfera(0, 0, 3)
print(e.tostring())
print(f"Área de la esfera: {e.calcularArea():.2f}")
print(f"Volumen de la esfera: {e.calcularVolume():.2f}")


#COMPROBAR UNA HORA METODO
class horas:
    def __init__(self, horas, minutos,segundos):
        self.hora = horas
        self.minuto = minutos
        self.segundo = segundos

    def getmin(self):
        return self.minuto
    def gethoras(self):
        return self.hora
    def getsec(self):
        return self.segundo

    def sethoras(self,horas):
        self.hora = horas % 24
    def setsec(self,segundos):
        self.segundo = segundos % 60
    def setmin(self,minutos):
        self.minuto = minutos % 60

    def incrementarsec(self, massec):
        total = self.segundo + massec
        self.segundo = total % 60
        masmin = (self.minuto + total // 60)
        self.minuto = (self.minuto + total // 60) % 60
        self.hora = (self.hora + masmin // 60) % 24

    def incrementarmin(self, masmin):
        total = self.minuto + masmin
        self.minuto = total % 60
        self.hora = (self.hora + total // 60) % 24

    def incrementarh(self, mash):
        self.hora = (self.hora + mash) % 24

    def mostrarformato12h(self):
        sufijo = "AM"
        h = self.hora
        if h == 0:
            h = 12
        elif h == 12:
            sufijo = "PM"
        elif h > 12:
            h -= 12
            sufijo = "PM"
        return h, ":", self.minuto, ":", self.segundo, sufijo

#RESOLUCIOOOOOOOOOOOOOOOOOON
from hora import horas

t = horas(int(input("hora: ")), int(input("minuto: ")), int(input("segundo:")))
t.incrementarsec(int(input("suma segundos: ")))
t.incrementarmin(int(input("añade minutos: ")))
t.incrementarh(int(input("añade  horas:")))

print(t.gethoras(), t.getmin(), t.getsec())

print(t.mostrarformato12h())


#VALIDACION DATOS DE UNA PERSONA
class Persoa:
    def __init__(self, nombre, edad, dni, direccion, nacionalidad):
        self.nombre = nombre
        if self.comprobarEdade(edad):
            self.edad = edad
        else:
            self.edad = 0
        if self.comprobarDni(dni):
            self.dni = dni
        else:
            self.dni = "00000000X"
        self.direccion = direccion
        self.nacionalidad = nacionalidad

    def comprobarEdade(self, edad):
        if edad >= 0 or edad <= 150:
            return True
        else:
            return False

    def comprobarDni(self, dni):
        if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
            letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
            resto = int(dni[:-1]) % 23
            if letraDni[resto] == dni[-1:].upper():
                return True
            else:
                return False
        else:
            return False
p = Persoa("Ana", 25, "12345678Z", "Calle Falsa 123", "Española")
print(p.nombre)
print(p.edad)
print(p.dni)

#EXAMEN 1111111111111111111111111111111
def ejercicio1():
    i = 0
    lista = []
    while i != 7:
        c = int(input("Dime la temperatura media del dia "))
        lista.append(c)
        i = i+1
    print(lista)

def ejercicio2():
    stem = 0
    temp = 0
    lista = [20,25,19,18,15,18,20]
    for temp in lista:
        stem =  stem + temp
    mtemp = stem//7
    print (mtemp)

def ejercicio3():
    stem = 0
    temp = 0
    lista = [20, 25, 19, 18, 15, 18, 20]
    dias = 0
    i = 0
    for temp in lista:
        stem = stem + temp
    mtemp = stem / 7
    while i != len(lista):
        if lista[i] > mtemp:
            dias = dias + 1
            i = i + 1
        else:
            i = i + 1
    print("hay ", dias, " que se supera la media de temperatura")

def ejercicio4():
    lista = [20, 25, 19, 18, 15, 18, 20]
    temperatura = int(input("Temperatura de corte: "))
    i = 0
    for temp in lista:
        i = i + 1
        if temp > temperatura:
            if i == 1:
                dia = "lunes"
                print (dia, temp)
            elif i == 2:
                dia = "martes"
                print(dia, temp)
            elif i == 3:
                dia = "miercoles"
                print(dia, temp)
            elif i == 4:
                dia = "jueves"
                print(dia, temp)
            elif i == 5:
                dia = "viernes"
                print(dia, temp)
            elif i == 6:
                dia = "sabado"
                print(dia, temp)
            elif i == 7:
                dia = "domingo"
                print(dia, temp)
ejercicio = input("Ingresa ejercicio: ")
if ejercicio == "1":
    print(ejercicio1())
elif ejercicio == "2":
    print(ejercicio2())
elif ejercicio == "3":
    print(ejercicio3())
elif ejercicio == "4":
    print(ejercicio4())


#EXAMEN 2222222222222222222222
# 1.

usuarioContrasinal = [["Manuel", "canMorto"], ["Pepe", "usuaya"]]

def comprobar_usuario(lista_usuario_contrasinal):
    existe_usuario = False
    nome_usuario = input("Cal é o nome de usuario?: ")
    contrasinal = input ("Cal é o contrasinal?: ")
    for usuario_contrasinal in lista_usuario_contrasinal:
        if usuario_contrasinal[0] == nome_usuario:
            if usuario_contrasinal[1] == contrasinal:
                existe_usuario = True

    return existe_usuario

existe = comprobar_usuario(usuarioContrasinal)
if existe:
    print("Usuario validado ")
else:
    print("Usuario ou contrasinal erroneo")


# 2.

def comprobar_caracteres(contrasinal):
    if len(contrasinal) > 8:
        return True
    else:
        return False

if comprobar_caracteres("wefwefewfw"):
    print("Maior que 8")
else:
    print("Menor que 8")


# 3.

def comprobar_maiusculas_contrasinal(contrasinal): # Opción 1
    maiusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in contrasinal:
        for maiuscula in maiusculas:
            if maiuscula == letra:
                return True


def comprobar_maiusculas_contrasinal2(contrasinal): # Opción 2
    maiusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in contrasinal:
        if letra in maiusculas:
            return True


def comprobar_maiusculas_contrasinal3(contrasinal): # Opción 3
    for letra in contrasinal:
        if letra == letra.upper():
            return True


# 3.

def comprobar_numero_contrasinal(contrasinal): # Opción 1
    numeros = "0123456789"
    for numero in contrasinal:
        for existe in numeros:
            if existe == numero:
                return True


def comprobar_numero_contrasinal2(contrasinal): # Opción 2
    for caracter in contrasinal:
        if caracter.isdecimal():
            return True


# 4.

def comprobar_caracteres_especiais(contrasinal):
    caracteres_especiais = "|@#$%&*_"
    for caracter in contrasinal:
        for especial in caracteres_especiais:
            if caracter == especial:
                return True


# 5.

def ver_caracter(contrasinal):
    caracter_especial = "!@#$%&*_."
    valido = False
    for char in contrasinal:
        if char in caracter_especial:
            valido = True

    return valido

t1 = "abcd1"
t2 = "A2!d"
t3 = "#Bcd"
t4 = "a1%&"
print(ver_caracter(t1))
print(ver_caracter(t2))
print(ver_caracter(t3))
print(ver_caracter(t4))


# 6.

def contraseña_valida():
    nom = str(input("Ingresa tu nombre: "))
    cont = str(input("Ingresa tu contraseña: "))
    nome_cont = [nom, cont]
    nome_contrasinal = []
    caracteres = ["!","@","#","$","%","&","*","_","."]
    valido = False
    digit = False
    mayus = False
    carac = False
    while valido == False and cont != "":
        if len(cont) >= 8:
            for char in cont:
                if char.isdigit():
                    digit = True
                elif char in caracteres:
                    carac = True
                elif char == char.upper():
                    mayus = True
            valido = (digit and carac and mayus)
        else:
            print(False)
            print("Contraseña invalida")
            print("Numero:", digit)
            print("Caracteres:", carac)
            print("Mayus:", mayus)
            cont = str(input("Ingresa tu contraseña: "))

    nome_contrasinal.append(nome_cont)
    return True

print(contraseña_valida())

#CLASE LIRBO EJERCICIO 1:
class libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.numPaginas = numPaginas
        self.valoracion = valoracion

    def o_titulo(self):
        return self.titulo
    def o_autor(self):
        return self.autor
    def o_ano(self):
        return self.ano
    def o_numPaginas(self):
        return self.numPaginas
    def o_valoracion(self):
        return self.valoracion
    def completo(self):
        return (f"Título: {self.titulo} \n"
                f"Autor: {self.autor} \n"
                f"Ano: {self.ano} \n"
                f"Num Paginas: {self.numPaginas} \n"
                f"Valoracion: {self.valoracion}")

def main():
    libros = libro("El señor de los anillos", "J.R.R Tolkien", 1954, 1200, 9.5)
    print(libros.completo())
    libros.valoracion = 9.8
    print("\n Despues de modificar la valoración")
    print(libros.completo())
if __name__ == "__main__":
    main()


#CLASE CONSUMO EJERCICIO 2:
class Consumo:
    def __init__(self, km, litros, vMed, pGas):
        self.km = km
        self.litros = litros
        self.vMed = vMed
        self.pGas = pGas

    def get_km(self):
        return self.km
    def get_litros(self):
        return self.litros
    def get_vMed(self):
        return self.vMed
    def get_pGas(self):
        return self.pGas
    def set_km(self, km):
        if km >= 0:
            self.km = km

    def set_litros(self, litros):
        if litros >= 0:
            self.litros = litros
    def set_vMed(self, vMed):
        if vMed >= 0:
            self.vMed = vMed
    def set_pGas(self, pGas):
        if pGas >= 0:
            self.pGas = pGas
    def getTiempo(self):
        if self.vMed > 0:
            return self.km / self.vMed
        return 0
    def consumoMedio(self):
        if self.km > 0:
            return (self.litros / self.km) * 100
        return 0
    def consumoEuros(self):
        return self.consumoMedio() * self.pGas

consumo1 = Consumo(0, 0, 0, 0)
consumo1.set_litros(50)
consumo1.set_pGas(1.57)
consumo2 = Consumo(400, 30, 90, 1.57)
print(consumo2.consumoMedio())
consumo2.set_litros(40)
print(consumo2.get_vMed())


#CLASE COCHE EJERCICIO 3:
class Coche:
    def __init__(self):
        self.velocidade = 0

    def getVelocidade(self):
        return self.velocidade

    def acelerar(self,valor):
        self.velocidade =  self.velocidade + valor
        print(f"Acelerando {valor} km/h. Velocidade actual: {self.velocidade} km/h")

    def frenar(self, menos):
        self.velocidade = self.velocidade - menos
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"Frenando {menos} km/h. Velocidade actual: {self.velocidade} km/h")

class Boletin9_3:
    def __init__(self):
        coche2 = Coche()
        print("Velocidade inicial:", coche2.getVelocidade(), "km/h")
        coche2.acelerar(50)
        coche2.acelerar(20)
        coche2.frenar(30)
        coche2.frenar(70)
        print("Velocidade final:", coche2.getVelocidade(), "km/h")

def main():
    Boletin9_3()
if __name__ == "__main__":
    main()


#CLASE CONTA EJERCICIO 4
class Conta:
    def __init__(self, nome, numero, tipo, saldo):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo

    def get_nome(self):
        return self.nome
    def get_numero(self):
        return self.numero
    def get_tipo(self):
        return self.tipo
    def get_saldo(self):
        return self.saldo
    def set_nome(self, nome):
        self.nome = nome
    def set_numero(self, numero):
        self.numero = numero
    def set_tipo(self, interese):
        self.tipo = interese
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.saldo = saldo
        else:
            print("El saldo debe ser positivo")

    def ingreso(self, cantidade):
        if cantidade > 0:
            self.saldo += cantidade
        else:
            print("La cantidad debe ser positiva")

    def reintegro(self, cantidade):
        if cantidade > 0:
            if cantidade <= self.saldo:
                self.saldo -= cantidade
            else:
                print("Saldo insuficiente.")
        else:
            print("La cantidad debe ser positiva")

    def transferencia(self, conta_destino, importe):
        if importe > 0:
            if importe <= self.saldo:
                self.saldo -= importe
                conta_destino.ingreso(importe)
                print("Transferencia realizada con éxito.")
            else:
                print("Saldo insuficiente")
        else:
            print("El importe debe ser positivo")

conta1 = Conta("Ana", "ES123456", 1.5, 1000)
conta2 = Conta("Luis", "ES654321", 1.2, 500)
print("Saldo inicial Ana:", conta1.get_saldo())
print("Saldo inicial Luis:", conta2.get_saldo())
conta1.ingreso(200)
print("Saldo de Ana tras ingreso:", conta1.get_saldo())
conta1.reintegro(150)
print("Saldo de Ana tras reintegro:", conta1.get_saldo())
conta1.transferencia(conta2, 300)
print("Saldo final Ana:", conta1.get_saldo())
print("Saldo final Luis:", conta2.get_saldo())
----------------------------------------------
#CALCULADORA BINARIA

class calculadora:
    def __init__(self,a,b):
        self.set_a(a)
        self.set_b(b)

    def set_a(self,a):
        if isinstance(a, int) or isinstance(a, float):
            self.__a = a
        else:
            self.__a = 0
    def get_a(self):
        return self.__a

    def set_b(self,b):
        if isinstance(b, int) or isinstance(b, float):
            self.__b = b
        else:
            self.__b = 0
    def get_b(self):
        return self.__b

    def calcular(self,op):
        if op == "+":
            return self.__a + self.__b
        if op == "-":
            return self.__a - self.__b
        if op == "*":
            return self.__a * self.__b
        if op == "/":
            return self.__a / self.__b

    a = property(get_a,set_a)
    b = property(get_b,set_b)

if __name__=='__main__':
    c1 = calculadora(14,15)
    print(c1.calcular("/"))
    c2 = calculadora(2,0)
    try:
        print(c2.calcular("/"))
    except ZeroDivisionError:
        print("No se pode dividir por cero")
        intentos = 0
        b = int(input("Introduce un número distinto de 0: "))
        while b == 0 and intentos < 2:
            intentos += 1
            b = int(input("Introduce un número distinto de 0: "))
        c2.b = b
        if c2.b == 0:
            print("Con 0 no se puede hacer la división.")
        else:
            print(c2.calcular("/"))
    finally:
        print("Fin del programa")

#DNI ERROR
FICHERO ERROR DNI (SON TODOS IGUALES)
class DniError(Exception):
    def __init__(self, mensaxe):
        super().__init__()
        self.mensaxe = mensaxe
    def __str__(self):
        return "Error "+ str(self.mensaxe)

FICHERO PRINCIPAL
from ErrorDNi import DniError
class persoa:
    def __init__(self,nome,dni,idade):
        self.setNome(nome)
        self.setDni(dni)
        self.setIdade(idade)

    def setNome(self,nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            self.__nome = ("Error")
    def getNome(self):
        return self.__nome

    def setIdade(self,idade):
        if type(idade) == int:
            if idade >=0:
                self.__idade = idade
            else:
                self.__idade = ("Error")
        else:
            self.__idade = ("Error")
    def getIdade(self):
        return self.__idade

    def setDni(self,dni):
        if type(dni) == str:
            if len(dni) == 9 :
                int(dni[:-1])
                if dni[:-1].isdigit():
                    if dni[-1:].isalpha():
                        letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                        resto = int(dni[:-1]) % 23
                        letra_correcta = letraDni[resto]
                        if letra_correcta == dni[-1].upper():

                            self.__dni = dni.upper()
                        else:
                            raise DniError(f"La letra no es ta entre las selecionadas para un DNI")
                    else:
                        raise DniError(f"Los 9 primeros digitos no son numeros")
                else:
                    raise DniError(f"El ultimo dígito no es una letra")
            else:
                raise DniError(f"El numero de carateres no es el adecuado")
        else:
            raise TypeError(f"el tipo de {type(dni)} tiene que ser str")
    def getDni(self):
        return self.__dni


    def __str__(self):
        return (f"El nombre es: {self.__nome}, o DNI es: {self.__dni} y la edad es: {self.__idade}")
if __name__=='__main__':
    try:
        alan = persoa("Alan","00000000T",20)
        print("DNI válido:",alan)
    except DniError as e:
        print("Error con p1: ",e)

#ERROR DNI CON PROPERTY Y CONDICION
class persoa:
    def __init__(self,nome,dni,idade):
        self.setNome(nome)
        self.setDni(dni)
        self.setIdade(idade)

    def setNome(self,nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            self.__nome = ("Error")
    def getNome(self):
        return self.__nome

    def setIdade(self,idade):
        if type(idade) == int:
            if idade >=0:
                self.__idade = idade
            else:
                raise ValueError(f"O valor {idade} tenque ser maior que cero ")
        else:
            raise TypeError(f"el tipo de {type(idade)} tiene que ser int")
    def getIdade(self):
        return self.__idade

    def setDni(self,dni):
        if len(dni)== 9:
            if dni[-1:].isalpha():
                if dni[:-1].isalpha():
                    letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                    resto = int(dni[:-1]) % 23
                    if letraDni[resto] == dni[-1:].upper():
                        return True
                    else:
                        return False
                else:
                    raise ValueError("Letra del dni incorecta")
            else:
                raise ValueError("Los 8 primeros caracteres tien que ser numeros")
        else:
            raise ValueError("Lonxitude incorecta")
    def getDni(self):
        return self.__dni

    nome = property(getNome,setNome)
    idade = property(getIdade,setIdade)
    dni = property(getDni,setDni)

    def __str__(self):
        return self.__nome + " " + str(self.__dni) + " " + str(self.__idade)
if __name__=='__main__':
    try:
        p = persoa("Alan","554380238","10")
    except ValueError as e:
        print("Error: " + str(e))
        intentos = 0
        edade = int(input("Introduce la edad: "))
        while edade < 0 and intentos < 2:
            intentos += 1
            print("Edade non valida")
            edade = int(input("Introduce un número la edada: "))
        p = persoa("Alan","554380238",edade)
        print(p)

    except TypeError as t:
        print("Error: "+ str(t))

    finally:
        print("Fin del programa")

#NUSS ERROR
# archivo: trabajador.py
from Persoa2 import persoa   # Asegúrate de que Persoa2.py tenga la clase persoa
from NussError import NussError  # Tu clase de error personalizada para NUSS
from ErrorDNi import DniError    # Tu clase de error personalizada para DNI

class trabajador(persoa):
    def __init__(self, nome, dni, idade, nuss):
        super().__init__(nome, dni.upper(), idade)  # Forzar mayúscula en DNI
        self.setNUSS(nuss)

    # Setter de NUSS
    def setNUSS(self, nuss):
        if len(nuss) != 16:
            raise NussError("La longitud de NUSS es inadecuada (16)")
        # Validar barras en posiciones correctas
        if nuss[2] != "/" or nuss[11] != "/":
            raise NussError("Formato esperado: nn/nnnnnnnnn/nn")
        # Validar que los dígitos son correctos
        if not (nuss[:2].isdigit() and nuss[3:11].isdigit() and nuss[12:].isdigit()):
            raise NussError("Formato de NUSS incorrecto, error en los dígitos")
        self.nuss = nuss

    # Getter de NUSS
    def getNUSS(self):
        return self.nuss

    # Representación como string
    def __str__(self):
        return f"{self.nome} {self.dni} {self.idade} {self.nuss}"


# === EJEMPLO DE USO ===
if __name__ == "__main__":
    try:
        # DNI válido: 55438023G, edad int, NUSS válido: 12/12345678/90
        t = trabajador(nome="Alan", dni="26623774D", idade=30, nuss="12/111111111/90")
        print("Trabajador creado correctamente:")
        print(t)

    except ValueError as ve:
        print("Error de valor:", ve)
    except TypeError as te:
        print("Error de tipo:", te)
    except NussError as ne:
        print("Error de NUSS:", ne)
    except DniError as de:
        print("Error de DNI:", de)
    finally:
        print("Fin del programa")


PERSONA2
from ErrorDNi import DniError
class persoa:
    def __init__(self,nome,dni,idade):
        self.setNome(nome)
        self.setDni(dni)
        self.setIdade(idade)

    def setNome(self,nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            self.__nome = ("Error")
    def getNome(self):
        return self.__nome

    def setIdade(self,idade):
        if type(idade) == int:
            if idade >=0:
                self.__idade = idade
            else:
                self.__idade = ("Error")
        else:
            self.__idade = ("Error")
    def getIdade(self):
        return self.__idade

    def setDni(self,dni):
        if type(dni) == str:
            if len(dni) == 9 :
                int(dni[:-1])
                if dni[:-1].isdigit():
                    if dni[-1:].isalpha():
                        letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                        resto = int(dni[:-1]) % 23
                        letra_correcta = letraDni[resto]
                        if letra_correcta == dni[-1].upper():

                            self.__dni = dni.upper()
                        else:
                            raise DniError(f"La letra no es ta entre las selecionadas para un DNI")
                    else:
                        raise DniError(f"Los 9 primeros digitos no son numeros")
                else:
                    raise DniError(f"El ultimo dígito no es una letra")
            else:
                raise DniError(f"El numero de carateres no es el adecuado")
        else:
            raise TypeError(f"el tipo de {type(dni)} tiene que ser str")
    def getDni(self):
        return self.__dni


    def __str__(self):
        return (f"El nombre es: {self.__nome}, o DNI es: {self.__dni} y la edad es: {self.__idade}")
if __name__=='__main__':
    try:
        alan = persoa("Alan","00000000T",20)
        print("DNI válido:",alan)
    except DniError as e:
        print("Error con p1: ",e)

#1.  Dadas as clases mostradas no diagrama UML (Persoa, Deportista), codificar os métodos setter para que si o crear o obxecto do tipo persoa se introduce un DNI non válido xere unha excepción do tipo DniNonValido.
#Codificar o método setLicenza para que verifique que o formato da licenza sexa  correcto. O formato da licenza (aaaadddnnnnnn)  é  da seguinte maneira :
#aaaa, 4 números que representan o ano en curso.
#ddd, abreviatura do deporte (fut fútbol, bal balocesto, etc).
#nnnnnn, 6 números do número único de licenza.
from Persoa2 import persoa
from ErrorDNi import DniError
from ErrorLicencia import LicenciaError
class Persona(persoa):
    def __init__(self,nome,dni,idade,direcion):
        super().__init__(nome,dni,idade)
        self.setDirecion(direcion)

    def setDirecion(self,direcion):
        self.direcion = direcion
    def getDirecion(self):
        return self.direcion

    def __str__(self):
        return (f"El nombre es {self.getNome()}, o DNI es: {self.getDni()} , la edad es: {self.getIdade()} y la direción es: {self.getDirecion()}")

class Deportista:
    def __init__(self,deporte,club,licencia):
        self.setDeporte(deporte)
        self.setClub(club)
        self.setLicencia(licencia)

    def setDeporte(self,deporte):
        if type(deporte) == str:
            self.__deporte = deporte
        else:
            raise TypeError(f"El formato no es el corecto")
    def getDeporte(self):
        return self.__deporte

    def setClub(self,club):
        if type(club)== str:
            self.__club = club
        else:
            raise TypeError(f"El formato no es el corecto")
    def getClub(self):
        return self.__club

    def setLicencia(self,licencia):

        if type(licencia) == str:
            if len(licencia) == 13:
                if licencia[:4].isdigit() and licencia[:4] == "2026":
                    if licencia[4:7].isalpha() and licencia[4:7].upper() == self.getDeporte()[:3].upper():
                        if licencia[-6:].isdigit():
                            self.__licencia = licencia
                        else:
                            raise LicenciaError (f"Los ultimos 6 digitos tiene que ser números")
                    else:
                        raise LicenciaError (f"Los digitos de de deporte no son correctos ")
                else:
                    raise LicenciaError (f"O los 4 pimeros dijitos o no son 2026 o no son números")
            else:
                raise LicenciaError (f"La cantidad de caractere no es la adecuada tiene que ser 13 caracteres")
        else:
            raise TypeError(f"El formato no es el corecto")
    def getLicencia(self):
        return self.__licencia
    def __str__(self):
        return (f"El deporte que hace es: {self.getDeporte()}, pertenecer al club: {self.getClub()}, y su licencia es. {self.getLicencia()}")
if __name__=='__main__':
    try:
        alan = Persona("Alan","00000000T",20,"Gondomar")
        print("DNI válido:",alan)
    except DniError as e:
        print("Error con p1: ",e)

    try:
        De = Deportista("Futbal","Real Madrid","2026Fut300000")
        print("Licencia: ", De)
    except TypeError as t:
        print(t)
    except LicenciaError as l:
        print(l)

#2. Adaptar a clase Data, para que só admita datos correctos a hora de introducir os días, meses e anos, e que xere unha excepción si os datos non son correctos (FormatoDataError). As condicións para que os datos sexan correctos son:
#O número de día entre 1 e 28, 29, 30 e 31 (dependendo do mes e o ano). Ten que verificar si é bisesto.
#O número do mes entre 1 e 12.
#O número de ano entre 1970 e 2999.
from DataError import DataError
class Data:
    def __init__(self,dia,mes,ano):
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)



    def setDia(self,dia):
        if type(dia) == int:
            if dia>= 1 or dia<=31:
                self.__dia = dia
            else:
                raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
        else:
            raise TypeError(f"El formato tiene que ser INT")
    def getDia(self):
        return self.__dia

    def setMes(self,mes):
        if type(mes) == int:
            if len(mes) == 2:
                if mes>=1 or mes<=12:
                    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                        if self.__dia>= 1 or dia<=31:
                            self.__mes = mes
                        else:
                            raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
                    elif mmes == 4 or mes == 6 or mes ==9 or mes == 11:
                        if dia>= 1 or dia<=30:
                            self.__mes = mes
                        else:
                            raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
                    elif mes == 2:
                        if dia >= 1 or dia <= 29:
                            self.__mes = mes
                        else:
                            raise DataError(f"El número de dia esta mal solo puede estar entre 1 hasta 31")
                else:
                    raise DataError(f"Los meses solo pueden ir desde 1 a 12")
            else:
                raise DataError(f"Los meses Los meses solo pueden ir desde 1 a 12")
        else:
            raise TypeError(f"El formato tiene que ser INT")
    def getMes(self):
        return self.__mes

    def __str__(self):
        return print(f"Dia: {self.__dia}, Mes: {self.__mes}")

if __name__=='__main__':
    D = Data(31,6)
    try:

    except DataError as e:
        print("Error con p1: ",e)

#CALCULADORA BINARIA CON MATCH
class CalculadoraBinaria:
    def __init__(self, a, b):
        self.setA(a)
        self.setB(b)

    def setA(self, a):
        if type(a) == int:
            self.a = a
        else:
            raise ValueError("A debe ser un entero")

    def getA(self):
        return self.a

    def setB(self, b):
        if type(b) == int:
            self.b = b
        else:
            raise ValueError("B debe ser un entero")

    def getB(self):
        return self.b

    def operacion(self, op):
        match op:
            case "+":
                print(f"La suma es {self.a + self.b}")
            case "-":
                print(f"La resta es {self.a - self.b}")
            case "*":
                print(f"La multiplicación es {self.a * self.b}")
            case "/":
                if self.b != 0:
                    print(f"La división es {self.a / self.b}")
                else:
                    print("Error: división entre cero")
            case _:
                print("Operación no válida")

c = CalculadoraBinaria(2, 5)
c.operacion("+")
c.operacion("*")

#PUNTO CON DECORADORES
from abc import ABC, abstractmethod
class Punto(ABC):
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)

    def setX(self, x):
        if type(x)== int or type(x)== float:
            if x>=0:
                self._x = x
            else:
                raise ValueError(f"O valor de x ={x} no pertenece a primer cuadrante")
        else:
            raise TypeError(f"La clase {type(x)} tiene que ser int o float")

    def getX(self):
        return self._x


    def setY(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self._y = y
            else:
                raise ValueError(f"O valor de y ={y} no pertenece a primer cuadrante")
        else:
            raise TypeError(f"La clase {type(y)} tiene que ser int o float")
    def getY(self):
        return self._y
    y = property(getY,setY)
    x = property(getX,setX)

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularVolumen(self):
        pass

    def __str__(self):
        return f"El punto es {self._x} x , {self._y} "

if __name__=='__main__':
    try:
        p = Punto(3,1)
    except TypeError as t:
        print("Error: "+ str(t))

    except ValueError as e:
        print("Error: " + str(e))

    print(p)

#CIRCULO
from punto import Punto
from abc import ABC
import math
class Circulo(Punto,ABC):
    def __init__(self,x,y,radio):
        super().__init__(x,y)
        self._radio = radio

    @property
    def Radio(self):
        return self._radio
    @Radio.setter
    def Radio(self,radio):
        self._radio=radio

    def calcularArea(self):
        resultado = math.pi * radio ** 2
        return resultado

#CILINDRO
from circulo import Circulo
import math
class Cilindro(Circulo):
    def __init__(self,x,y,radio,altura):
        super().__init__(x,y,radio)
        self._altura = altura

    @property
    def Altura(self):
        return self._altura
    @Altura.setter
    def Altura(self,altura):
        self._altura= altura

    def __str__(self):
        return (f"El punto es: {self._x},{self._y}  | El radio es:{self._radio} | La altura es: {self._altura}")
    def calcularArea(self):
        area = 2 * math.pi * self._radio *(self._radio + self._altura)
        return area
    def calcularVolumen(self):
        volumen = math.pi * self._altura * self._radio ** 2
        return volumen

cil = Cilindro(2,4,28,45)
print(cil.calcularVolumen())

#COMPROBADOR DATA
class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

        if not self.es_fecha_valida():
            raise ValueError("Fecha no válida")

    def es_bisiesto(self):
        return (self.anio % 4 == 0 and self.anio % 100 != 0) or (self.anio % 400 == 0)

    def dias_del_mes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes == 2:
            return 29 if self.es_bisiesto() else 28
        else:
            return 0

    def es_fecha_valida(self):
        if self.anio < 1:
            return False
        if self.mes < 1 or self.mes > 12:
            return False
        if self.dia < 1 or self.dia > self.dias_del_mes():
            return False
        return True

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

#CATCH
x = 30
match x:# se parece al if
    case 10:
        print("X é 10")
    case 20:
        print("X é 20")
    case _:
        print("X non é")

match x:
    case 10|20|30:
        print("X")
    case _:
        print("X...")
match x:
    case 10 if x % 2 ==0:
        print("X....")

l = (2,3,3)
match l:
    case( x,y):
        print(f"la posicion {x}, {y}")
    case (x,y,z):
        print(f"la pososicion es {x},{y} y {z} ")

persoa = {"nome":"Manuel","curso":"Dam"}

match persoa:
    case {"nome":nome,"curso":curso}:
        print(f"Nome:{nome},curso:{curso}")
    case _:
        print("Hostia")

class figura:
    pass
class Circulo(figura):
    def __init__(self,r):
        self.radio=r
class Rectangulo(figura):
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

f = Circulo(15)

match f:
    case Circulo( radio = r):
        print(f"A figura e un circulo de radio {r}")
    case Rectangulo(ancho,alto):
        print(f" a figura e un rectangulo con {ancho} de ancho y {alto} de alto")

#VEHÍCULO CON DECORADORES
BASTRACTO
from abc import ABC, abstractmethod
class Vehiculo(ABC):
    def __init__(self,matricula,velocidadeMaxima,autonomia):
        self.setMatricula(matricula)
        self.setVelocidad(velocidadeMaxima)
        self.setAutonomia(autonomia)

    def setMatricula(self,matricula):
        self._matricula = matricula
    def getMatricula(self):
        return  self._matricula

    def setVelocidad(self, velocidadeMaxima):
        self._velocidadeMaxima = velocidadeMaxima
    def getVelocidad(self):
        return self._velocidadeMaxima

    def setAutonomia(self,autonimia):
        self._autonomia = autonimia
    def getAutonomia(self):
        return  self._autonomia

    def __str__(self):
        return (f"Matricula: {self._matricula}, Velocidade:{self._velocidadeMaxima}, Autonomia:{self._autonomia}")

    matricula = property(getMatricula,setMatricula)
    velocidadeMaxima = property(getVelocidad,setVelocidad)
    autonomia = property(getAutonomia,setAutonomia)

    @abstractmethod
    def arrincar(self):
        pass

    def deter(self):
        print(f"O vehiculo {self._matricula} está detido")

    @abstractmethod
    def mostrardatos(self):
        pass

#BASTRACTO2/TERRESTRE
from bastracto import Vehiculo
from abc import ABC
class Terrestre(Vehiculo,ABC):
    def __init__(self,matricula,velocidadeMaxima,autonomia,numeroRodas):
        super().__init__(matricula,velocidadeMaxima,autonomia)
        self.numero_rodas = numeroRodas

    @property
    def numero_rodas(self):
        return self._numero_rodas
    @numero_rodas.setter
    def numero_rodas(self,numeroRodas):
        self._numero_rodas= numeroRodas

#BASTRACTO3/AEREO
from bastracto import Vehiculo
from abc import ABC, abstractmethod
class Aereo(Vehiculo,ABC):
    def __init__(self,matricula,velocidadeMaxima,autonomia,AltitudeMaxima):
        super().__init__(matricula,velocidadeMaxima,autonomia)
        self.altitude_maxima = AltitudeMaxima

    @property
    def AltitudeMaxima(self):
        return self._altitude_maxima
    @numero_rodas.setter
    def numero_rodas(self,AltitudeMaxima):
        self._altitude_maxima= AltitudeMaxima

#BASTRACTO4/COCHE AUTONOMO
from bastracto2 import Terrestre
class CocheAutonomo(Terrestre):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numeroRodas, numeroPrazas):
        super().__init__(matricula,velocidadeMaxima,autonomia,numeroRodas)
        self.numeroPrazas = numeroPrazas

    @property
    def numeroPrazas(self):
        return self._numeroPrazas
    @numeroPrazas.setter
    def numeroPrazas(self,numeroPrazas):
        self._numeroPrazas = numeroPrazas

    def arrincar(self):
        print(f"O coche autonomo arrinca")
    def mostrardatos(self):
        print(f"La matricula: {self._matricula}, VelocidadMaxima: {self._velocidadeMaxima}, Autonimia: {self._autonomia}, Número de rodas: {self._numero_rodas}, Numero de prazas: {self._numeroPrazas} ")


coche = CocheAutonomo(1231,234,123,4,5)

print(coche.mostrardatos())
MIKM
