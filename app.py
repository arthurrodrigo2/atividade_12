import math

figuras = {
    "1": ("Quadrado", lambda: float(input("Lado: ")) ** 2),
    "2": ("Triângulo", lambda: float(input("Base: ")) * float(input("Altura: ")) / 2),
    "3": ("Círculo", lambda: math.pi * float(input("Raio: ")) ** 2),
    "4": ("Trapézio", lambda: (float(input("Base maior: ")) + float(input("Base menor: "))) * float(input("Altura: ")) / 2)
}

print("Escolha a figura geométrica para calcular a área:")
for key, (nome, _) in figuras.items():
    print(f"{key} - {nome}")

escolha = input("Digite o número da figura desejada: ")

if escolha in figuras:
    nome, calculo = figuras[escolha]
    print(f"\nA área do {nome} é: {calculo():.2f}")
else:
    print("Escolha inválida.")