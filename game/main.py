import random


def competencia(opciones):
    robot = random.choice(opciones)
    human = int(input('Escoja el número de su elección: '))
    humano = opciones[human-1]
    # print('Opción humano: ', humano)
    print('Opción robot: ', robot)
    if robot == humano:
        return print("Empate")
    elif robot == 'piedra':
        if humano == 'papel':
            return print('Gano el humano!!')
        else:
            return print('Gano el robot!!')
    elif robot == 'papel':
        if humano == 'tijera':
            return print('Gano el humano!!')


if __name__ == '__main__':
    opciones = ['piedra', 'papel', 'tijera']
    print(""""
Piedra la gana a tijera,

Papel le gana a piedra,

Tijera le gana a papel

""")
    print("""
Para hacer su selección, estos son los números de cada elemento:

1- Piedra
2- Papel
3- Tijera
""")

    competencia(opciones)
