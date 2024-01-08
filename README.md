# Sistema de Evaluación - Evaluador de Debilidades

## Descripción
Evaluador de Debilidades es un programa que realiza un análisis y cálculo de notas para un grupo de estudiantes en función de las respuestas proporcionadas en un archivo de entrada. Cada estudiante tiene respuestas a diversas preguntas, y el programa asigna valores a cada pregunta en base al porcentaje de aciertos y errores. Las preguntas con mayores errores reciben valores más altos.

## Proceso de Evaluación
1. Lee un archivo de entrada ("notas.txt") que contiene las respuestas de los estudiantes en forma de números entre 0 y 1, representando la corrección de la respuesta.
2. Calcula los valores asignados a cada pregunta según el porcentaje de aciertos y errores. Las preguntas con mayores errores reciben valores más altos.
3. Normaliza los valores para asegurar que la suma de todos los valores sea igual a 100%.
4. Genera las notas finales para cada estudiante basándose en los valores asignados a sus respuestas.
5. Muestra un resumen de las notas, incluyendo el total de cada estudiante y los valores normalizados de las preguntas.

## Funcionalidades
- Lee un archivo de entrada ("notas.txt") que contiene las respuestas de los estudiantes.
- Calcula los valores de cada pregunta, ponderando las preguntas con mayores errores.
- Normaliza los valores para asegurar una distribución proporcional.
- Genera las notas finales para cada estudiante.
- Muestra un resumen de las notas, incluyendo el total de cada estudiante y los valores normalizados de las preguntas.

## Uso
1. Asegúrate de tener un archivo de entrada llamado "notas.txt" con el formato correcto.
2. Ejecuta el programa.
3. Observa el resumen de notas generado.

## Ejemplo de archivo de entrada
Cada valor de la tabla debe estar separado por un espacio ' ' respectivamente. Y la primer columna representa los identificadores de cada estudiante.

```plaintext
CristoJ. 0 0 0 0 1
Jesus. 0 1/2 1 8/16 1
Dios-15 1 1/2 0 0 0
Zafiro4 1 1/34 1 2/7 1
Juan533 1 1/2 4/7 1 0
SrJesus 1 1/2 1 1 1
Josue1:9 1 1/5 1 1 1
Sami 1 0 1 1 1 1
Sofia0611 1 0 1 0 1
3013 1 1/2 0 1/2 0
```


## Ejemplo de salida
La ultima fila representa los valores asignados a cada pregunta.
```plaintext
Estudiante  1     2     3     4     5     Total     
CristoJ.    -     -     -     -     2.9   2.94      
Jesus.      -     3.6   3.4   2.3   2.9   12.17     
Dios-15     2.0   3.6   -     -     -     5.52      
Zafiro4     2.0   0.2   3.4   1.3   2.9   9.79      
Juan533     2.0   3.6   1.9   4.6   -     12.06     
SrJesus     2.0   3.6   3.4   4.6   2.9   16.44     
Josue1:9    2.0   1.4   3.4   4.6   2.9   14.30     
Sami        2.0   -     3.4   4.6   2.9   12.88     
Sofia0611   2.0   -     3.4   -     2.9   8.26      
3013        2.0   3.6   -     2.3   -     7.83      
Valores     2.0   7.1   3.4   4.6   2.9   20  
```