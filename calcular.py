width_identificador = 12 # este valor reprensenta el ancho de la columna 
                         # asignada a los identificadores, se puede incrementar
                         # para usar identificadores mas largos.

def main():
    with open('notas.txt') as file:
        tabla = [line.rstrip().split(' ') for line in file]

    tablaStringToNumbers(tabla)
    valores = calcular_valores(tabla)
    notas = generar_notas(tabla, valores)
    mostrar_notas(tabla, valores, notas)


def mostrar_notas(tabla, valores, notas):
    print(f'{"Estudiante":<{width_identificador}}', end='')

    for i in range(1, len(tabla[0])):
        print(f'{i:<6}', end='')

    print(f'{"Total":<10}')

    for columna in range(len(tabla)):
        print(f'{tabla[columna][0]:<{width_identificador}}', end='')

        for fila in range(1, len(tabla[0])):
            if tabla[columna][fila] == 0:
                print(f'{"-":<6}', end='')
            else:
                print(f'{(tabla[columna][fila] * ((valores[fila - 1] * 20) / 100)):<6.1f}', end='')

        print(f'{((notas[columna] * 20) / 100):<10.2f}')


    print(f'{"Valores":<{width_identificador}}', end='')
    
    # mostrar cada valor
    valor_total = 0
    
    for fila in range(len(tabla[0]) - 1):
        valor_total += ((valores[fila] * 20) / 100)
        if(valores[fila] == 0):
            print(f'{"-":6}', end='')
        else:
            print(f'{((valores[fila] * 20) / 100):<6.1f}', end='')

    print(f'{valor_total:<10.0f}')


def generar_notas(tabla, valores):
    return [sum(tabla[columna][fila] * valores[fila - 1] for fila in range(1, len(tabla[0]))) for columna in range(len(tabla))]


def tablaStringToNumbers(tabla):
    for columna in range(len(tabla)):
        for fila in range(1, len(tabla[0])):
            tabla[columna][fila] = eval(tabla[columna][fila])


def calcular_valores(tabla):
    preguntas_cantidad = len(tabla[0]) - 1
    estudiantes_cantidad = len(tabla)

    acumulador = 0
    acumulador_de_porcentaje = 0
    valores = []

    for i in range(preguntas_cantidad):
        valores.append(0)

    for columna in range(1, preguntas_cantidad + 1):
        for fila in range(estudiantes_cantidad):
            acumulador += tabla[fila][columna]

        valores[columna - 1] = 100 - ((acumulador * 100) / estudiantes_cantidad)
        acumulador_de_porcentaje += valores[columna - 1]
        acumulador = 0

    for i in range(len(valores)):
        valores[i] = (valores[i] * 100) / acumulador_de_porcentaje

    return valores

main()