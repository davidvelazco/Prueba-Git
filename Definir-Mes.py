# Diccionario con los meses
meses = {
    "01": "Enero", "02": "Febrero", "03": "Marzo",
    "04": "Abril", "05": "Mayo", "06": "Junio",
    "07": "Julio", "08": "Agosto", "09": "Septiembre",
    "10": "Octubre", "11": "Noviembre", "12": "Diciembre"
}

# Ingreso de la fecha
fecha_str = input("Introduce la fecha en formato ISO (YYYYMMDD): ")

# Extraer el mes de la cadena
mes = fecha_str[4:6]  # Tomamos los caracteres correspondientes al mes

# Mostrar el resultado
print(f"El mes es: {meses[mes]}")