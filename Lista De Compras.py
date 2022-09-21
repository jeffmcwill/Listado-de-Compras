import time
#--------------------------------------------------------------------------------------------------
def Caratula():
	print("""
------------------------------------------------------------------
      ___                    ___                         ___     
     /  /\       ___        /  /\          ___          /  /\    
    /  /:/      /__/\      /  /::\        /__/\        /  /::\   
   /  /:/       \__\:\    /__/:/\:\       \  \:\      /  /:/\:\  
  /  /:/        /  /::\  _\_ \:\ \:\       \__\:\    /  /::\ \:\ 
 /__/:/      __/  /:/\/ /__/\ \:\ \:\      /  /::\  /__/:/\:\_\:\

 \  \:\     /__/\/:/~~  \  \:\ \:\_\/     /  /:/\:\ \__\/  \:\/:/
  \  \:\    \  \::/      \  \:\_\:\      /  /:/__\/      \__\::/ 
   \  \:\    \  \:\       \  \:\/:/     /__/:/           /  /:/  
    \  \:\    \__\/        \  \::/      \__\/           /__/:/   
     \__\/                  \__\/                       \__\/ 
     		>LISTADO DE COMPRAS BY JEFF MCWILL<
-----------------------------------------------------------------""")
	time.sleep(2)
	print("""Esto servira para tener un mayor control
de tus finanzas al momento de querer comprar.""")
	time.sleep(2)

#------------------------------------------------------
lista1=[]
#------------------------------------------------------
#FUNCIONES DEL PROOGRAMA:
def Apagar():
	print("-------------------------------------------------------------------------------------")
	print("¿¿¿Estas Seguro???")
	print("Una vez apagado se borraran los objetos agregados y el total de todas la unidades...")
	print("-------------------------------------------------------------------------------------")
	print("Presiona 1 para ir al menu o presiona cualquier numero para apagar")
	apagado=int(input(">>> "))
	if apagado == 1:
		Main()
	elif apagado != 1:
		print("Hasta luego. ;)")
		resultado=SumaElem(lista1)
		print("Total de la compra: ",resultado)
		print("Total de objetos comprados: ",len(lista1))
		time.sleep(4)

def SumaElem(lista):
	suma=0
	for elem in lista:
		suma+=elem
	return suma

def Agregar():
	
	apagado2=0

	while apagado2 != 11:
		print("------------------")		
		print("AGREGAR PRODUCTOS")
		print("------------------")
		try:
			numero=int(input("Dime el precio del producto: "))
			unidades=int(input("¿Por cuantas unidades te llevaras?: "))
			resultado=numero*unidades
		except:
			print('intente poner el producto nuevamente')
			continue
		print("En total te daria: ",resultado)
		lista1.append(resultado)
		print("................................")
		print("*****Agregado a la lista*****")
		print("................................")
		print("Presiona 1 para seguir agregando o cualquier numero para ir al menu.")
		resultado=SumaElem(lista1)
		print("-------------------------------------")
		print("Lista actual: ",resultado)
		print("Cantidad de productos: ",(len(lista1)))
		print("-------------------------------------")
		apagado2=int(input(">>> "))
		if apagado2 == 1:
			continue
		elif apagado2 != 1:
			Main()
			break

def ListadoSumado(lista):
	if not lista1:
		print("----------------------")
		print("No hay ningun numero")
		print("----------------------")
		time.sleep(2)
		Main()

	else:
		resultado=SumaElem(lista1)
		print("-------------------------------------")
		print("El total de la lista es: ",resultado)
		print("Productos en total: ",(len(lista1)))
		print("-------------------------------------")
		time.sleep(2)
		Main()

#------------------------------------------------------

def Main():
	apagado=0
	while apagado != 1:
		time.sleep(2)
		print("-----------------------")
		print("Opciones:")
		print("-----------------------")
		time.sleep(1)
		print("1.Agregar unidades")
		time.sleep(1)
		print("2.Sumar Listado.")
		time.sleep(1)
		print("3.Apagar Programa.")
		time.sleep(1)
		print("-----------------------")
		resultado=SumaElem(lista1)
		print("Total de la compra: ",resultado)
		print("Total de objetos comprados: ",len(lista1))
		print("--------------------------------------------")
		user=int(input(">>> "))
		if user == 1:
			Agregar()
			break
		elif user == 2:
			ListadoSumado(lista1)
			break
		elif user == 3:
			Apagar()
			break
#-----------------------------------------------------------
Caratula()
Main()