def generar_archivo():

    while True:
        try:
            cantidad = int(input("Numero de lineas (1-1000): "))

            if 1 <= cantidad <= 1000:
                break

            print("El numero debe estar entre 1 y 1000.")

        except:
            print("Ingrese un numero entero valido.")

    with open("alfabetos.txt", "w") as archivo:

        for i in range(1, cantidad + 1):
            linea = "{:04d} ABCDEFGHIJKLMNOPQRSTUVWXYZ\n".format(i)
            archivo.write(linea)

    print("Archivo alfabetos.txt creado.")
    print("Cantidad de lineas:", cantidad)


generar_archivo()