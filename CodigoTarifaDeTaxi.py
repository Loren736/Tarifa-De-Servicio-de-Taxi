#valores base
TARIFA_INICIAL = 6300        #  mínima
VALOR_POR_KM = 1200          # Valor aproximado por distancia
RECARGO_AERO = 8000
RECARGO_NOCT_FEST = 3800
# la lista donde voy a guardar todos los registros
registros = []
#para que se pueda usar varias veces en un bucle 
while True:
    print("\n--- INICIO: TAXICONTROL ---")
    print("1. Nuevo servicio")
    print("2. Ver registros")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1": 
            print("\nINGRESO DE DATOS ")
            fecha = input("Ingresa la fecha (DD/MM): ")
            hora = input("Ingresa la hora (HH.MM): ")
            
            print("\nSeleccione el método de pago:")
            print("A. Efectivo | B. Tarjeta | C. Aplicación")
            metodo_pago = input("> ").upper()
            
        
            distancia = float(input("\nDigite la distancia recorrida (en KM): "))
            
            # Tarifa Especial
            print("\n¿Aplica tarifas especiales? (S/N)")
            print("1. Aeropuerto | 2. Nocturno/Festivo | 3. Ninguno")
            especial = input("> ")
            
            costo_total = TARIFA_INICIAL + (distancia * VALOR_POR_KM)
            recargo_aplicado = 0

            match especial:
                case "1":
                    recargo_aplicado = RECARGO_AERO
                case "2":
                    recargo_aplicado = RECARGO_NOCT_FEST
                case _:
                    recargo_aplicado = 0
            
            costo_total += recargo_aplicado

            # se guarda el servicio
            nuevo_servicio = {
                "fecha": fecha,
                "hora": hora,
                "pago": metodo_pago,
                "total": costo_total
            }
            registros.append(nuevo_servicio)

            print(f"\n>>> TOTAL A PAGAR: ${costo_total}")
            print("--- REGISTRO EXITOSO ---")

        case "2": # ver registros
            print("\n--- VISUALIZACIÓN DE REGISTROS ---")
            if not registros:
                print("No hay servicios guardados.")
            else:
                for r in registros:
                    print(f"Fecha: {r['fecha']} | Hora: {r['hora']} | Pago: {r['pago']} | TOTAL: ${r['total']}")

        case "3": 
            print("Cerrando programa...")
            break

        case _:
            print("Opción no válida. Intente de nuevo.")
