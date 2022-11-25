import random


class Cliente:
    def __init__(self) -> None:
        self.nombre=input('Escriba su nombre: ')
        self.ciudad=input('Escriba su ciudad: ')
        self.correoElectronico=input('Escriba su correo electrónico: ')
        self.facturacion=input('Diga su facturacion: ')

    def confirmarRegistro(self):
        print(f'Se ha guardado {self.nombre}')
    def calcularNeto(self,neto,pagas):
        neto=(neto*0.8)/pagas
        print(f'El cliente {self.nombre} tiene un neto de {neto}')

cliente1=Cliente()
cliente1.calcularNeto(2000,12) #cliente calcula su salario neto
cliente1.confirmarRegistro()


#añadir productos a lista de deseos
productos=[]
print("--------------------")
print("-LISTA DE PRODUCTOS-")
print("--------------------")
print()

while True:
    print("1. Añadir producto.")
    print("2. Eliminar producto.")
    print("3. Mostrar lista de productos.")
    print("4. Realizar compra.")
    print("5. Salir")
    print()
    opcion=input("-->")
    print()

    if opcion=="1":
        producto=input("Introduce el producto: ").capitalize()
        productos.append(producto)
    elif opcion=="2":
        producto=input("Introduce el producto: ").capitalize()
        productos.remove(producto)
    elif opcion=="3":
        print("Lista de deseos")
        for e in productos:
            print("-", e)
    elif opcion=="4":
        pais=input('País de envío: ').capitalize()
        if pais==('España'):
            print("+0.15 de IVA")
        else:
            print("+0.6 de IVA")

        for i in range(1):
            print("Se ha enviado la factura a su correo electrónico")
            print("SMS")
            print(f'Su código de seguimiento es {random.randrange(1000,9999)}')
            
        break
    elif opcion=="5":
        print("Salir")
        break
    else:
        print("Introduce una opción correcta.")
