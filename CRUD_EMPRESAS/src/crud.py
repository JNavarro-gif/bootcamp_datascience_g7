from time import sleep
from src.datos import empresas,guardar_datos
from src.utils import pausa,titulo,limpiar
from src.decoradores import pantalla

@pantalla("REGISTRAR EMPRESA")
def registrar_empresa():
    RUC = input("INGRESE RUC : ")
    razon_social = input("INGRESE razon_social : ")
    direccion = input("INGRESE direccion : ")
    
    empresas[RUC] = {
        "razon_social" : razon_social,
        "direccion": direccion
    }
    titulo("EMPRESA REGISTRADO EXITOSAMENTE!!!")
    
@pantalla("MOSTRAR EMPRESAS")
def mostrar_empresas():
    for RUC,info in empresas.items():
        print(f"RUC : {RUC}")
        print(f"razon_social : {info['razon_social']}")
        print(f"Direccion : {info['direccion']}")
        print("*" * 50)
        
@pantalla("ACTUALIZAR EMPRESA")
def actualizar_empresa():
    RUC = input("Ingrese RUC de la Empresa : ")

    if RUC in empresas:
        print(f"Empresa encontrado : {empresas[RUC]['razon_social']}")
        print("Ingrese nuevos datos o presione ENTER para conservar los anteriores")

        nuevo_razon_social = input(f"Nuevo Razon_social ({empresas[RUC]['razon_social']}): ")
        nuevo_direccion = input(f"Nuevo direccion ({empresas[RUC]['direccion']}): ")

            
        empresas[RUC]["razon social"] = nuevo_razon_social if nuevo_razon_social else empresas[RUC]["razon_social"]

        if nuevo_direccion != "":
            empresas[RUC]["direccion"] = nuevo_direccion

        print("Empresa actualizada...")
    else:
        print("Empresa no encontrada...")
        
@pantalla("ELIMINAR EMPRESA")
def eliminar_empresas():
    RUC = input("Ingrese RUC de la Empresa : ")

    if RUC in empresas:
        del empresas[RUC]
        print("Empresa eliminada...")
    else:
        print("Empresa no encontrada...")
        
def menu_principal():
    while True:
        limpiar()
        titulo("CRUD DE EMPRESAS")
        print("""
            [1] REGISTRAR EMPRESA
            [2] MOSTRAR EMPRESA
            [3] ACTUALIZAR EMPRESA
            [4] ELIMINAR EMPRESA
            [5] SALIR
        """)
        
        opcion = int(input("INGRESE OPCIÓN : "))
        
        if opcion == 1:
            registrar_empresa()
            pausa()
        elif opcion == 2:
            mostrar_empresas()
            pausa()
        elif opcion == 3:
            actualizar_empresa()
            pausa()
        elif opcion == 4:
            eliminar_empresas()
            pausa()
        elif opcion == 5:
            guardar_datos(empresas)
            limpiar()
            titulo("SALIENDO DEL SISTEMA...")
            print("Datos guardados en empresas.csv")
            sleep(2)
            break
        else:
            print("Opción no válida.")
