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

## Ejemplo de Archivo de Entrada

```plaintext
CristoJ. 0 0 0 0 1 1 1 1 1 1 0 0 1/2 0 2/3 1/2 4/5 3/6
Jesus. 0 1/2 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 4/6
Dios-15 1 1/2 0 0 0 1 1 1 1 0 1 1 0 0 1/3 1/2 0 0
Zafiro4 1 1 1 1 1 1 1 1 0 0 1 1 1 0 1 1 1 4/6
Juan533 1 1/2 0 1 0 1/3 1 1 0 1 0 0 0 0 0 0 2/5 4/6
SrJesus 1 1/2 1 1 1 1/3 1 1 0 0 1 1 1 1 0 1/2 3/5 2/6
Josue1:9 1 1/2 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 4/6
Sami 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2/5 4/6
Sofia0611 1 0 1 0 1 1/2 1 1/2 1 1 1 1 0 1 1/3 1 3/5 1/6
3013 0 0 0 0 0 2/3 1 0 1 1 0 1 0 1 1/3 1/2 3/5 0