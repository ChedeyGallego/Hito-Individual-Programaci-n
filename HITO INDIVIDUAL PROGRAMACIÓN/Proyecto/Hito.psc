Algoritmo Hito
	//registrar cliente
		Definir cliente Como Caracter;
		Escribir "Escriba su nombre: "
		Leer nombre;
		
		Escribir "Escriba su ciudad: "
		Leer ciudad;
		
		Escribir "Diga su facturaci�n: "
		Leer facturaci�n;
	
		Escribir "Se ha guardado [nombre cliente]";
		Escribir "El cliente tiene una facturaci�n de [facturaci�n]";
		
	//mostrar lista de deseos
		Escribir "LISTA DE PRODUCTOS";
		Escribir "1.A�adir producto";
		Escribir "2.Eliminar producto";
		Escribir "3.Muestra lista productos";
		Escribir "4.Realizar compra";
		Escribir "5.Salir";
	//ingresar una opci�n
		Escribir "Elija una opci�n (1-5):"
		Leer option
	//procesar opci�n
		Segun option hacer
			1:
				Escribir "Introduce el producto"
			2:
				Escribir "Introduce el producto"
			3:
				Escribir "Lista de deseos"
			4:
				Escribir "Realizar compra"
			5:
				Escribir "Salir"
			De Otro Modo:
				Escribir "Introduce una opci�n correcta"
		FinSegun
FinAlgoritmo
