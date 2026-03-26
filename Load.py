   # --- Paso 3:
        print(f"Cargando {len(processed_data)} registros en la base de datos...")
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Crear tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pais(
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(255) NOT NULL,
                capital VARCHAR(255) NOT NULL,
                region VARCHAR(255),
                poblacion BIGINT
            )
        """)

        # Insertar datos
        sql_insert = "INSERT INTO pais (nombre, capital, region, poblacion) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql_insert, processed_data)
        
        conn.commit()
        print("¡ETL finalizado con éxito!")

    except requests.exceptions.RequestException as e:
        print(f"Error en la extracción (API): {e}")
    except Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    run_etl()