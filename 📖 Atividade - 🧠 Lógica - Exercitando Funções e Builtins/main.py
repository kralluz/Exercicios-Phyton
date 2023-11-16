import math
""" 📖 Atividade - 🧠 Lógica - Exercitando Funções e Builtins """


def delta(a: int, b: int, c: int) -> int:
    return b**2 - (4 * a * c)


def bhaskara(a: int, b: int, c: int) -> float:
    dr = delta(a, b, c)
    if dr < 0:
        return 'Delta Negativo'
    x1 = (-b + math.sqrt(dr)) / (2*a)
    x2 = (-b - math.sqrt(dr)) / (2*a)
    return "{:.2f}".format(x1), "{:.2f}".format(x2)


print(bhaskara(7, 3, 4))
# Delta Negativo

print(bhaskara(1, 5, 2))
# x1=-0.44, x2=-4.56

print(bhaskara(3, 10, 2))
# x1=-0.21, x2=-3.12

