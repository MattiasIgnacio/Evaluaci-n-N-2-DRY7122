import requests

def obtener_datos_viaje(origen, destino, api_key):
    url = f'http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={origen}&to={destino}&locale=es_ES&unit=k'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def convertir_tiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def main():
    api_key = 'ySMnqIJKO9uosKM0JcQ6JwQF3fXtvt2m'  # API Key generada

    while True:
        origen = input("Ciudad de Origen (o 'q' para salir): ")
        if origen.lower() == 'q':
            break
        
        destino = input("Ciudad de Destino (o 'q' para salir): ")
        if destino.lower() == 'q':
            break
        
        datos_viaje = obtener_datos_viaje(origen, destino, api_key)
        
        if datos_viaje and datos_viaje.get('info').get('statuscode') == 0:
            ruta = datos_viaje.get('route')
            distancia_km = ruta.get('distance')
            duracion_segundos = ruta.get('time')
            horas, minutos, segundos = convertir_tiempo(duracion_segundos)
            combustible_litros = distancia_km / 12  # Consumo aproximado de combustible: 12 km/L

            print(f"Datos del viaje desde {origen} hasta {destino}:")
            print(f"Distancia: {distancia_km:.2f} km")
            print(f"Duración: {horas:.0f} horas, {minutos:.0f} minutos, {segundos:.0f} segundos")
            print(f"Combustible requerido: {combustible_litros:.2f} litros")
            print("Narrativa del viaje:")
            for idx, paso in enumerate(ruta.get('legs')[0].get('maneuvers'), start=1):
                narrative = paso.get('narrative')
                if 'millas' in narrative:  # Reemplazar "millas" por "km"
                    narrative = narrative.replace('millas', 'kilómetros')
                if 'yardas' in narrative:  # Reemplazar "yardas" por "metros"
                    narrative = narrative.replace('yardas', 'metros')
                print(f"{idx}. {narrative}")
            print()

if __name__ == "__main__":
    main()
