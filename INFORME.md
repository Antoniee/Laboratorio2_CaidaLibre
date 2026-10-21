#Informe de laboratorio 2: Análisis estadístico de caída libre.

**Autora:**
Desarrollado por: [María Antonia Cardozo Forero]

**Commit Evaluable:**[f64f816]

## Objetivos
*leer y validar un CSV con la biblioteca estándar;
*separar lectura, validación, cálculo y presentación en funciones propias;
*estimar y resumir g con unidades;
*comprobar el programa con casos normales, de frontera e inválidos;
*explicar el alcance físico del resultado.


## 1.Fundamento Teórico

**INTRODUCCIÓN**

La caída de  los cuerpos es un fenómeno de la naturaleza que ha interesado a los pensadores y científicos desde la antigüedad, desde Aristóteles, con sus ideas de dos mundo separados, pasando por Galileo y sus estudios sobre el movimiento y la caída de los cuerpos, llegando finalmente a Newton quien formaliza estos conocimientos logrando formular la ley de gravitación universal, una ley ontológica que define la forma de vida humana. De la caída libre se desprenden otros movimientos y fenómenos interesantes  para la investigación, uno de ellos es  la capacidad  que tienen algunos cuerpos de rebotar en una superficie, e continuación se presentará un ejercicio de caída libre y rebote que busca encontrar una correlación entre estas dos variables. 
 
**MARCO TEÓRICO**

Al acercarse al concepto de Caída Libre se puede identificar a través de la literatura que Uno de los grandes avances de la revolución científica,que se consolida en el siglo XVII con la formulación de la síntesis newtoniana, fue superar esta separación radical entre Cielo y Tierra, cómo lo proponía Aristóteles,  y plantear leyes de carácter universal, como la ley de gravitación y los principios de la dinámica clásica\cite {Sanchez}. Estos planteamientos conllevaron una comprensión profunda del movimiento y del porqué de la caída  de los cuerpos, llegando así a estudiar con detalle la Caída Libre  como  movimiento uniformemente acelerado en una dimensión \cite {Cordova}.

$$h= vt−\frac{1}{2}gt^2+H$$

Donde, $$h$$ es la altura en metros, v  es la velocidad inicial en metros por segundo aplicada al cuerpo, $$g$$ es la aceleración de la gravedad $$9.8 m/s2$$, $$t$$ es el tiempo en segundos desde que inicia el movimiento y $H$ es la altura a la que se deja caer el cuerpo.

**Referencias**

[1] Sánchez, M. A. (2011). Siete cuestiones para divulgar y comprender aspectos de la ca´ıda
libre. Lat Am Phys Educ, 5(3), 623.
[2] Córdova, G. B.(2016) ¿ CUANTO TARDA UNA PELOTA EN DEJAR DE REBOTAR?.Research Gate

**El experimento**

Para nuestro caso específico el experimento modeló una caída libre unidimensional regida por la ecuación:
$$h(t) = h_0 - \frac{g \cdot t^2}{2}$$

Donde los supuestos físicos asumidos son:
1. El cuerpo parte estrictamente desde el reposo absoluto (v₀ = 0).
2. Se desprecia por completo la resistencia del aire. 
3. El campo gravitatorio es perfectamente uniforme y constante durante la trayectoria.


## 2. Resultados 

### Tabla de datos procesados 
* **Altura Inicial (h₀):** 10.00 m
* **Muestra Original:** 15 filas detectadas.

| Tiempo \(t\) (s) | Altura \(h\) (m) | Incertidumbre (m) | Gravedad \(g_i\) (\(\text{m/s}^2\)) | Estado / Observación Física |
| :--- | :--- | :--- | :--- | :--- |
| 0.1000 | 9.94 | 0.0300 | **12.0000** | Inestabilidad crítica por tiempo corto |
| 0.2000 | 9.81 | 0.0300 | 9.5000 | Fluctuación transitoria instrumental |
| 0.3000 | 9.55 | 0.0300 | 10.0000 | Estabilización y convergencia |
| 0.4000 | 9.20 | 0.0300 | 10.0000 | Estabilización y convergencia |
| 0.5000 | 8.77 | 0.0300 | 9.8400 | Alta estabilidad experimental |
| 0.6000 | 8.23 | 0.0300 | 9.8333 | Alta estabilidad experimental |
| 0.7000 | 7.60 | 0.0300 | 9.7959 | Máxima aproximación al valor teórico |
| 0.8000 | 6.85 | 0.0300 | 9.8438 | Comportamiento asintótico estable |
| 0.9000 | 6.01 | 0.0300 | 9.8519 | Comportamiento asintótico estable |
| 1.0000 | 5.06 | 0.0300 | 9.8800 | Comportamiento asintótico estable |
| 1.1000 | 3.99 | 0.0300 | 9.9339 | Incremento leve al final del tramo |
| 1.2000 | 2.82 | 0.0300 | 9.9722 | Incremento leve al final del tramo |
| 1.3000 | 1.52 | 0.0300 | 10.0355 | Zona previa al impacto |
| 1.4000 | 0.38 | 0.0300 | 9.8163 | Retorno preciso a la referencia |

### Métricas Estadísticas Consolidadas
* **Número de mediciones útiles (N):** 14
* **Media Obtenida (ḡ):** 10.0216 m/s²
* **Desviación Estándar (σ):** 0.5631 m/s²
* **Rango Dinámico (Máx - Mín):** 2.5000 m/s² (Desde 9.5000 hasta 12.0000)
* **Diferencia Absoluta:** 0.2116 m/s²
* **Error Relativo Porcentual:** 2.1573%

## 3. Conclusiones y Limitaciones 

### Análisis de Sensibilidad en Tiempos Cortos
El valor anómalo de 12.0000 m/s² en t = 0.1 s se debe a que la variable temporal se encuentra elevada al cuadrado en el denominador de la ecuación despejada: $$g_i = \frac{2(h_0-h_i)}{t_i^2}$$. Al ser un número extremadamente pequeño (0.01 s²), cualquier incertidumbre física en el sensor de altura (los ± 0.03 m informados) se magnifica de forma hiperbólica, afectando los cálculos iniciales.

### Criterio de Compatibilidad 
Considero que el resultado de los cálculos **es compatible** con el valor teórico de referencia (9.81 m/s²) porque dicho valor se encuentra contenido dentro del intervalo de dispersión natural de los datos determinado por la desviación estándar poblacional:
$$[\bar{g} - \sigma, \bar{g} + \sigma] \rightarrow [10.0216 - 0.5631, 10.0216 + 0.5631] \rightarrow [9.4585, 10.5847]\text{ m/s}^2$$

### Limitaciones 
La principal limitación está en la resolución y sensibilidad del instrumento de medición en la primera fracción del movimiento (tramo inicial de la caída). Una validación basada en descartar intervalos de tiempo excesivamente cortos (t < 0.15 s) protegería la consistencia física del resultado global del informe.


## 4. Evidencias

### Registro de Pruebas de Software Realizadas
El programa desarrollado permitió obtener: 

* **Caso Archivo Vacío:** Bloqueado con éxito mediante excepción `ValueError`.
* **Caso Tipo de Dato Inválido:** Identifcado con éxito localizando el índice de la fila no apta de texto.

* **Caso Tiempo No Monótono Creciente:** Detectado inmediatamente al evaluar la condición $$t_i \le t_{i-1}$$.

### Contribución 
* Se diseñó e implementó la función de validación de límites físicos de altura (0 ≤ h ≤ h₀) y la conversión limpia de tipos flotantes. También se  diseñó la lógica de comparación temporal estricta y se estructuró la impresión formateada de tablas.

### Diferencia Conceptual: `return` vs `print`
* **`return`:** Es una instrucción fundamental que finaliza la ejecución de una función y devuelve un valor o dato útil hacia el bloque de código principal. Esto permite que el número calculado sea guardado en una variable o reutilizado en otras fórmulas matemáticas (por ejemplo, pasar el resultado de la gravedad a la función estadística).
* **`print`:** Es un  efecto secundario visual. Muestra caracteres de texto en la pantalla para que una perosna pueda leerlos, pero ese valor no es almacenable ni procesable por ninguna otra función matemática dentro del flujo lógico del programa; para éste, el dato deja de existir.