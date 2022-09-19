# imprime todos los números enteros del 0 al 150.
for x in range(151):
    print(x)

#imprime todos los múltiplos de 5 entre 5 y 1,000.

for x  in range(5,1001,5):
    print(x)

#imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” 
#en su lugar. Si es divisible por 10, imprime "Coding Dojo".

for x  in range(101):
    if x%5 == 0:
        print("Coding")
    if x%10 == 0:
        print("Coding Dojo")

#Whoa. Es un gran idiota: 
#agrega los enteros impares del 0 al 500,000, e imprime la suma final.
Imparestotal=0
for x  in range(1,500000,2):
    Imparestotal = Imparestotal + x
resultado="La suma total de enteros impares del al 500,000 es: {:,}"
print(resultado.format(Imparestotal))

#Cuenta regresiva de a 4: imprime números positivos comenzando desde 
#el 2018, en cuenta regresiva de 4 en 4.

for x  in range(2018,1,-4):
    print(x)

#Contador flexible: establece tres variables: lowNum, highNum, mult. 
#Comenzando en lowNum y pasando por highNum, imprime solo los enteros 
#que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3.
#El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

lowNum=int(input("Ingrese el numero de inicio: "))
highNum=int(input("Ingrese el numero de termino: "))
mult=int(input("Ingrese el multiplo: "))
result=[]
for x in range(lowNum,highNum+1):
    if x%mult == 0:
        result.append(x)
print("Los numeros multiplos de", mult, "son:", result)