#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro
#Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).
print()
print("Ejersicio 1")
print()
hasta = int(input("Ingrese un número para encontrar todos los números primos hasta ese número: "))
def mostrar_primos(hasta):
      primos = []
      for num in range(2, hasta + 1):
          if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
              primos.append(num)
          elif primos is not hasta:
            print("Debe ingresar un número")
          else:
            print("No ingreso un número")
            break

      print(f"Los números primos hasta {hasta} son: {primos}")
mostrar_primos(hasta)
print()
print("Ejercicio 2")
print()
condimentos = {
    1: "Mayonesa",
    2: "Sabora",
    3: "Ketchup",
    4: "Salsa de Apio",
    5: "Salsa de Queso"
}

print("Lista de condimentos disponibles:")
for num, condimento in condimentos.items():
    print(f"{num}: {condimento}")

sandwich = []

while True:
    pedido = input("¿Desea agregar un condimento? (SI / NO): ")
    if pedido.lower() == "si":
        opcion = input("Ingrese el número del condimento que desea agregar: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion in condimentos:
                condimento_elegido = condimentos[opcion]
                sandwich.append(condimento_elegido)
                print(f"Tu sandwich tiene: {sandwich}")
            elif opcion is not condimentos:
                print("El condimento que quiere no existe en la lista de condimentos.")
            else:
              print("Intente de nuevo.")
        else:
            print("Ingrese un número válido.")
    elif pedido.lower() == "no":
        print("Pedido finalizado.")
        break
    else:
        print("Opción inválida. Intente de nuevo con 'SI' o 'NO'.")
        

print()
print("Ejersicio 4")
print()

def fibonacci(n):
    fib_series = []

    for i in range(n):
        if i == 0:
            fib_series.append(0)
        elif i == 1:
            fib_series.append(1)
        else:
            fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

print("Si quiere ver los primeros 3 números, ingrese el npumero 3.")
n = int(input("Ingrese la cantidad de números de la serie de Fibonacci que quiere ver: "))
result = fibonacci(n)
print(f"Los primeros {n} números de la serie de Fibonacci son: {result}")

print()
print("Ejersicio 5")
print()
import math
print("Tabla de multiplicar")
salir = "salir"

def tabla():
 print()
 print("Menú de Opciones, seleccione una opción de la calculadora que quiera ejecutar.")
 print("Ingrese la plabra salir para terminar el programa.")
 print()
numero1 = float( input( "Introduce el primer número: "))
numero2 = float( input( "Introduce el segundo número: "))
print()
print("1 Multiplicar:")
print("2 Dividir")
print("3 Sumar")
print("4 Restar")
print("5 Raiz Cuadrada")
while True:
  tabla()
  opcion = (input("Ingrese una opcion: "))
  if opcion.lower() == salir:
        print(f"Fin del programa '{salir}'.")
        break
  elif opcion == 1:
    print(f"La multiplicación es:",(numero1 * numero2))
    break
  elif opcion == 3 :
    print(f"La suma es:",(numero1 + numero2))
    break
  elif opcion == 4:
    print(f"La resta es:",(numero1 - numero2))
    break
  elif opcion == 5:
    print("La raiz cuadrada es:",math.sqrt(numero1))
    break
  else :
    print("Opcion ingresada valida.")
print()
print("Ejersicio 8")
print()
def calcular_primos():
    primos = []
    for num in range(1, 1000):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primos.append(num)
    return primos

def calcular_multiplos_3_y_5():
    multiplos = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
    return multiplos

def menu():
    print("\nMenú de Opciones:")
    print("1 Calcular Números Primos")
    print("2 Calcular Múltiplos de 3 y 5")
    print("3 Salir")

def main():
    while True:
        menu()
        opcion = input("Ingrese una opción (1, 2 o 3): ")

        if opcion == "1":
            primos = calcular_primos()
            print("Números primos:")
            print(primos)
        elif opcion == "2":
            multiplos = calcular_multiplos_3_y_5()
            print("Múltiplos de 3 y 5:")
            print(multiplos)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingrese 1, 2 o 3.")

if __name__ == "__main__":
    print("Ejercicio 8\n")
    print("Tabla de multiplicar")
    main()
