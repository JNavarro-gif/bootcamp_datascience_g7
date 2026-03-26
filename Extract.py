  # --- PHASE 1: EXTRACT ---
        print("Extrayendo datos de la API...")
        response = requests.get(API_URL)
        response.raise_for_status()
        countries_data = response.json()

        