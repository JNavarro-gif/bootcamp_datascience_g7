import csv
import os

ARCHIVO_CSV = 'empresas.csv'

def cargar_datos():
    datos = {}

    if os.path.exists(ARCHIVO_CSV):
        with open(ARCHIVO_CSV, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                Ruc = fila["Ruc"]
                datos[Ruc] = {
                    "razon_social": fila["razon_social"],
                    "direccion": fila["direccion"]
                }

    return datos

def guardar_datos(datos):
    with open(ARCHIVO_CSV, mode="w", encoding="utf-8", newline="") as archivo:
        campos = ["Ruc", "razon_social", "direccion"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        for Ruc, info in datos.items():
            escritor.writerow({
                "Ruc": Ruc,
                "razon_social": info["razon_social"],
                "direccion": info["direccion"]
            })

empresas = cargar_datos()