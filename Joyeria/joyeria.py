import os

#Lista de productos e inventario disponible

productos = [
    {"nombre": "Anillo de diamante", "precio": 10000, "cantidad": 5}, #Diccionarios
    {"nombre": "Anillo de cuarzo", "precio": 400, "cantidad": 8},
    {"nombre": "Anillo de plata", "precio": 1000, "cantidad": 12},
    {"nombre": "Anillo de oro", "precio": 6000, "cantidad": 5},
]

carrito = []

def limpiar_pantalla():
    if os.name == "nt" :
        os.system("cls") #Limpiar pantalla en windows
    else:
        os.system("clear") #limpiar terminal en linux o mac

def mostrar_productos():
    limpiar_pantalla()
    print ("-----------Menu de Productos------------")
    for i, producto in enumerate(productos):
        print (f"{i + 1}. {producto["nombre"]} - precio ${producto["precio"]} - cantidad {producto["cantidad"]}")


def agregar_al_carrito():
    limpiar_pantalla()
    mostrar_productos()
    try:
        opcion= int(input("Digite la opcion de el producto que desea agregar: "))
        if 1 <= opcion <= len(productos):
            cantidad = int(input("Digite la cantidad de productos a comprar: "))
            producto = productos[opcion - 1]
            if cantidad > producto ["cantidad"]:
                print ("No hay suficiente existencia del producto")
            else:
                productos[opcion - 1]["cantidad"] -= cantidad
                carrito.append({"nombre": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad })
                print (f"¡Felicidades! Añadiste {cantidad} {producto["nombre"]} de manera exitosa")


    except Exception as e:
        print ("Se ha producido un error", e)

def mostrar_carrito():
    limpiar_pantalla()
    if carrito:
        print ("carrito de compras")
        for i, item in enumerate(carrito, 1):
            print (f"{i+1}. producto: {item["nombre"]} - ${item["precio"]} - cantidad: {item["cantidad"]}")
    else:
        print ("El carrito esta vacio")

def calcular_total():
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    print (f"El total a pagar es: ${total}")


def finalizar_compra():
    limpiar_pantalla()
    mostrar_carrito()

    if carrito: 
        calcular_total()
        confirmar = input ("¿Desea finalizar su compra (s/n?): ")

        if confirmar.lower() == "s":
            carrito.clear()
            print ("La compra fue realizada exitosamente")
        else:
            print ("La compra fue cancelada")
    else:
        print ("El carrito esta vacio")

def main():
    while True:
        limpiar_pantalla()
        print ("--------------Menu Joyeria--------------")
        print ("1. Mostrar productos disponibles")
        print ("2. Añadir productos al carrito")
        print ("3. Mostrar carrito")
        print ("4. Finalizar compra")
        print ("5. Salir de la compra")

        try:
            opciones = {
                1: mostrar_productos,
                2: agregar_al_carrito,
                3: mostrar_carrito,
                4: finalizar_compra
            }

            seleccion = int(input("Digite la opcion deseada: "))
            if seleccion in opciones:
                opciones [seleccion]()
                input ("Presione enter para continuar")
            elif seleccion == 5:
                break
        except ValueError:
            print ("La entrada es invalida, por favor digite un numero")
            input ("Presione enter para continuar...")

        except Exception:
            print ("Se ha presentado un error")
            input ("Presione enter par continuar...")

main()