from pathlib import Path

def calcular_gravedad(h: float, t: float, h0: float = 10.0) -> float:
    """
    Calcula la gravedad en función de la altura y el tiempo.

    h: Altura inicial (en metros)
    t: Tiempo transcurrido (en segundos)
    h0: Altura final (en metros)
    return: Gravedad calculada (en m/s^2)
    """
    if t <= 0:
        return None  # Evitar división por cero o tiempo negativo
    return (2 * (h0 - h)) / (t ** 2)

def calcular_estadistica (lista_g: list [float], g_ref: float = 9.81) -> dict:
    """
    Calcula estadísticas de una lista de valores de gravedad.

    lista_g: Lista de valores de gravedad (en m/s^2)
     g_ref: Valor de referencia de gravedad (en m/s^2)
    return: Diccionario con estadísticas calculadas
    """
    n = len(lista_g)
    if n == 0:  
        return {}  # Evitar cálculo con lista vacía

    #La media 
    suma_g = sum(lista_g )
    media = suma_g / n

    #La desviación estándar (Potencia 0.5)
    suma_varianza = sum((g - media) ** 2 for g in lista_g)
    desviacion = (suma_varianza / n) ** 0.5

    #Valores Extremos y rango
    valor_max = max(lista_g)
    valor_min = min(lista_g)
    rango = valor_max - valor_min   

    #Errores 
    error_absoluto = abs(media - g_ref)
    error_relativo = (error_absoluto / g_ref) * 100 if g_ref != 0 else None

    return { 
        "n": n,
        "media": media,
        "desviacion": desviacion,
        "valor_max": valor_max,
        "valor_min": valor_min,
        "rango": rango,
        "error_absoluto": error_absoluto,
        "error_relativo": error_relativo
    }

def procesar_experimento(ruta_csv: Path, h0: float = 10.0) -> tuple[list, dict]:
    """
    Procesa  el  archivo CSV con datos de altura y tiempo, calcula la gravedad y estadísticas.

    ruta_csv: Ruta al archivo CSV
    h0: Altura final (en metros)
    return: Tupla con lista de valores de gravedad y diccionario de estadísticas
    """
    if not ruta_csv.exists():
        raise FileNotFoundError(f"El archivo {ruta_csv} no existe.")

    lineas = []
    with open(ruta_csv, mode = "r", encoding="utf-8") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]

    if len (lineas) < 1:
        raise ValueError("El archivo CSV debe contener al menos una línea de datos además del encabezado.")

    encabezado = lineas[0].split(",")
    #asumiendo orden: tiempo_s, altura_m, incertidumebre_m

    filas_validas = []
    lista_g = []
    t_anterior = -1.0  # Inicializar con un valor negativo para la primera comparación

    for idx, linea in enumerate(lineas[1:], start=2):  # Comenzar desde la segunda línea
        campos = linea.split(",")
        if len(campos) < 3:
            raise ValueError(f"Línea {idx}: Se esperaban al menos 3 campos, pero se encontraron {len(campos)}.")

        try:
            t = float(campos[0].strip())
            h = float(campos[1].strip())
            incertidumbre = float(campos[2].strip())
        except ValueError:
            raise ValueError(f"Línea {idx}: Los datos no son númericos finitos.")


        #Validaciones físicas 

        # Validaciones físicas corregidas
        if t < 0 or h < 0 or h > h0 or incertidumbre < 0:
            raise ValueError(f"Línea {idx}: Inválida por límites físicos.")

        if t <= t_anterior:
            raise ValueError(f"Línea {idx}: El tiempo debe ser estrictamente creciente (t={t}, t_anterior={t_anterior}).")
        t_anterior = t

        #Calculando g_i si t>0
        g_i = calcular_gravedad(h, t, h0)
        if g_i is not  None:
            lista_g.append(g_i)
            filas_validas.append((t, h, incertidumbre, g_i))

    estadisticas = calcular_estadistica(lista_g)
    return filas_validas, estadisticas

def imprimir_reporte(filas: list, est: dict):
    """
    Imprime un reporte de los resultados del experimento.

    filas: Lista de tuplas con datos válidos (tiempo, altura, incertidumbre, gravedad)
    est: Diccionario con estadísticas calculadas
    """
    print ("\n" + "=" * 50)
    print (f"{'TABLA DE DATOS CALCULADOS':^50}")
    print ("=" * 50)
    print(f"{'t (s)':<10}{'h (m)':<10}{'Incert (m)':<12}{'g_i (m/s²)':<10}")
    print("-"*50)
    for t, h, inc, g in filas:
        g_str = f"{g:.4f}" if g is not None else "N/A (t=0)"
        print(f"{t:<10.4f}{h:<10.2f}{inc:<12.4f}{g_str:<10}")
    print("="*50)
    
    if est:
        print(f"{'RESUMEN ESTADÍSTICO (g)':^50}")
        print("="*50)
        print(f"Filas procesadas con éxito: {est['n']}")
        print(f"Media muestral de g:         {est['media']:.4f} m/s²")
        print(f"Desviación estándar (pob):   {est['desviacion']:.4f} m/s²")
        print(f"Valor Mínimo:                {est['valor_min']:.4f} m/s²")
        print(f"Valor Máximo:                {est['valor_max']:.4f} m/s²")
        print(f"Rango de estimaciones:       {est['rango']:.4f} m/s²")
        print(f"Diferencia Absoluta (vs 9.81): {est['error_absolute']:.4f} m/s²")
        print(f"Error Relativo:              {est['error_relative']:.4%}")
        print("="*50)