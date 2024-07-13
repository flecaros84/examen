"""
Desarrolle una aplicación en Python utilizando Visual Studio Code como entorno de desarrollo según el siguiente enunciado:
Una empresa necesita analizar los datos de sus trabajadores para generar algunos reportes, y le ha solicitado a usted que
realice un prototipo en Python con los siguientes requerimientos:
La aplicación debe permitir analizar los sueldos de 10 empleados, los cuales para efectos de este prototipo se crearán de
forma aleatoria entre $300.000 y $2.500.000. Utilice la siguiente lista para asignar los sueldos a cada empleado:
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel
Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
La aplicación deberá poseer un menú con las siguientes funcionalidades:
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
Cada función se detalla a continuación:
"""
import random
from statistics import geometric_mean
from statistics import mean

# 1. Asignar sueldos aleatorios
# Para la generación de estos sueldos debe crear una función capaz de generar los 10 sueldos de forma aleatoria los que serán usados posteriormente para la ejecución del programa.

def Sueldos_Aleatorios():
    trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
    #lista auxiliar para almacenar sueldos
    sueldos = []
    #lista para almacenar diccionario con datos que incluya el nombre de cada empleado y su respectivo sueldo asignado
    datos = []
    for i in range(len(trabajadores)):
        sueldo = random.randint(300000,2500000)
        sueldos.append(sueldo)
        datos.append({"nombre": trabajadores[i], "sueldo": sueldos[i] })
    print("Datos de sueldos generados correctamente.")
    return datos

# 2. Clasificar sueldos
# Deberá desarrollar una función que permita mostrar la lista de empleados con su sueldo y su respectiva clasificación según el siguiente esquema:

def Clasificar_Sueldos(datos):

    #Se recorre la datos para clasificar sueldos menores a $ 800.000, almacenando en lista auxiliar "lista"
    contador = 0
    lista = []
    for dato in datos:
        if (dato["sueldo"] < 800000):
            lista.append({"nombre": dato["nombre"], "sueldo": dato["sueldo"]})
            contador += 1
    print(f"Sueldos Menores a $ 800.000 TOTAL: {contador}\n")
    print("Nombre Empleado\tSueldo")
    #Se despliegan solo datos de lista auxiliar
    for dato in lista:
        print(f"{dato["nombre"]}\t${dato["sueldo"]}")   
    
    # Se reinician el contador y la lista para sueldos entre $ 800.000 y $ 2.000.000, repitiendo proceso anterior
    contador = 0
    lista = []
    for dato in datos:
        if (dato["sueldo"] >= 800000 and dato["sueldo"] <= 2000000 ):
            lista.append({"nombre": dato["nombre"], "sueldo": dato["sueldo"]})
            contador += 1
    print(f"\nSueldos entre $ 800.000 y $ 2.000.000 TOTAL: {contador}\n")
    print("Nombre Empleado\tSueldo")
    for dato in lista:
        print(f"{dato["nombre"]}\t${dato["sueldo"]}")

    # Se reinician el contador y la lista para sueldos sobre $ 2.000.000, repitiendo proceso anterior
    contador = 0
    lista = []
    for dato in datos:
        if (dato["sueldo"] > 2000000 ):
            lista.append({"nombre": dato["nombre"], "sueldo": dato["sueldo"]})
            contador += 1
    print(f"\nSueldos superiores a $ 2.000.000 TOTAL: {contador}\n")
    print("Nombre Empleado\tSueldo")
    for dato in lista:
        print(f"{dato["nombre"]}\t${dato["sueldo"]}")  

    # Finalmente se recorre la lista de datos completa para calcular el total de sueldos
    total = 0
    for dato in datos:
        total += dato["sueldo"]
    print(f"\nTOTAL SUELDOS: $ {total}")

# 3. Ver estadísticas
# Crear una función que permita mostrar por pantalla los siguientes datos con respecto a los sueldos:
# - Sueldo más alto
# - Sueldo más bajo
# - Promedio de sueldos
# - Media geométrica

# Se utilizan metodos max, min junto con mean y geometric_mean del modulo statistics
def Ver_Estadisticas(datos):
    lista = []
    for dato in datos:
        lista.append(dato["sueldo"])
    maximo = max(lista)
    minimo = min(lista)
    promedio = mean(lista)
    media_geometrica = round(geometric_mean(lista),1)
    print(f"\nEl sueldo máximo es ${maximo}")
    print(f"El sueldo minimo es ${minimo}")
    print(f"El sueldo promedio es ${promedio}")
    print(f"La media geometrica es ${media_geometrica}")

#4. Reporte de sueldos
#La aplicación deberá poseer una función para mostrar el detalle de los sueldos de los trabajadores, según la siguiente regla de negocio:
# - Descuento salud 7%
# - Descuento AFP 12%
# - Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp.
# Y mostrarse como en la siguiente tabla de ejemplo:


def Reporte_Sueldos(archivo, datos):
    # Se abre archivo asegurandose compatibilidad con utf-8, luego imprimos y escribimos datos en reporte
    archivo = open(archivo, 'w', encoding= 'utf-8')
    print("\nNombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Liquido")
    archivo.write("Nombre empleado,Sueldo Base,Descuento Salud,Descuento AFP,Sueldo Liquido\n")
    for dato in datos:
        salud = round(dato["sueldo"] * 0.07)
        afp = round(dato["sueldo"] * 0.12)
        liquido = dato["sueldo"]-salud-afp
        print(f"{dato["nombre"]}\t${dato["sueldo"]}\t${salud}\t${afp}\t${liquido}")
        archivo.write(f"{dato["nombre"]},{dato["sueldo"]},{salud},{afp},{liquido}\n")
    print("\nEl archivo reporte.csv ha sido generado.")


# Main Program y Menu
datos = None
archivo = 'reporte.csv'
while True:
    print("\nElija su opción:")
    print("1. Asignar Sueldos Aleatorios")
    print("2. Clasificar Sueldos")
    print("3. Ver Estadisticas")
    print("4. Reporte de Sueldos")
    print("5. Salir del programa")
    try:
        opcion = int(input("Ingrese el N° de la Opción Seleccionada: "))
        match opcion:
            case 1:
                datos = Sueldos_Aleatorios()
            case 2:
                #Si lista de datos está vacia, opción no esta disponible. Se puso chequeos adicionales para casos 3 y 4
                if datos == None:
                    print("\nPrimero debe seleccionar la opción 1 para generar datos")
                else:
                    Clasificar_Sueldos(datos)
            case 3:
                if datos == None:
                    print("\nPrimero debe seleccionar la opción 1 para generar datos")
                else:
                    Ver_Estadisticas(datos)
            case 4:
                if datos == None:
                    print("\nPrimero debe seleccionar la opción 1 para generar datos")
                else:
                    Reporte_Sueldos(archivo,datos)
            case 5:
                print("\nFinalizando programa…\nDesarrollado por Fabián Lecaros\nRUT 15.961.836-6")
                break
            #Esta línea permite discrimar cuando se ingresa un entero que no se encuentre entre 1 y 5
            case _:
                 print("\nError. Debe ingresar un entero entre 1 y 5")
    #Excepción para casos en que el usuario ingrese un caracter que no sea un entero
    except ValueError:
        print("\nError. Debe ingresar un entero entre 1 y 5")

