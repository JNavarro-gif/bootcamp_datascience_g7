# --- PHASE 2: TRANSFORM ---
        print("Transformando datos...")
        processed_data = []
        for country in countries_data:
            # Manejo de datos faltantes para evitar errores
            nombre = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0] # Capital es una lista
            region = country.get('region', 'N/A')
            poblacion = country.get('population', 0)
            
            processed_data.append((nombre, capital, region, poblacion))

     