"""
╔══════════════════════════════════════════════════════════════╗
║          PYTHON DO ZERO - NÍVEL 3: Loops                    ║
╚══════════════════════════════════════════════════════════════╝

O que você vai aprender aqui:
  - for com range()
  - while
  - break e continue
  - Iterando sobre strings e listas
  - enumerate() e zip()

Para rodar este arquivo:
  python nivel_3_loops.py
"""

# ─────────────────────────────────────────────
# CONCEITO 1: for com range()
# Repete um bloco N vezes.
# range(início, fim, passo) — fim não é incluído!
# ─────────────────────────────────────────────

print("=== for com range() ===")

# Contando de 0 a 4
for i in range(5):
    print(f"  i = {i}")

print()

# Contando de 1 a 5
for i in range(1, 6):
    print(f"  {i}", end="  ")  # end="" evita quebra de linha

print()

# De 10 a 1 (contagem regressiva)
for i in range(10, 0, -1):
    print(i, end=" ")
print()


# ─────────────────────────────────────────────
# CONCEITO 2: while
# "Enquanto X for verdade, continue."
# Use quando não sabe quantas repetições haverá.
# ─────────────────────────────────────────────

print("\n=== while ===")
contador = 0

while contador < 5:
    print(f"  contador = {contador}")
    contador += 1  # equivale a: contador = contador + 1

print("Loop encerrado!")


# ─────────────────────────────────────────────
# CONCEITO 3: break e continue
# break    → para o loop imediatamente
# continue → pula para a próxima iteração
# ─────────────────────────────────────────────

print("\n=== break ===")
for i in range(10):
    if i == 5:
        print(f"  Encontrei o 5! Parando.")
        break
    print(f"  i = {i}")

print("\n=== continue (pulando pares) ===")
for i in range(10):
    if i % 2 == 0:
        continue  # pula os pares
    print(f"  ímpar: {i}")


# ─────────────────────────────────────────────
# CONCEITO 4: Iterando sobre strings
# Strings são sequências de caracteres!
# ─────────────────────────────────────────────

print("\n=== Iterando string ===")
palavra = "Python"

for letra in palavra:
    print(letra, end="-")
print()

# Contando vogais
vogais = "aeiouAEIOU"
frase = "Aprender Python é incrível"
contagem = 0

for char in frase:
    if char in vogais:
        contagem += 1

print(f"Vogais em '{frase}': {contagem}")


# ─────────────────────────────────────────────
# CONCEITO 5: enumerate()
# Dá o índice + valor ao iterar. Muito útil!
# ─────────────────────────────────────────────

print("\n=== enumerate() ===")
linguagens = ["Python", "JavaScript", "Rust", "Go"]

for indice, linguagem in enumerate(linguagens):
    print(f"  {indice + 1}. {linguagem}")


# ─────────────────────────────────────────────
# CONCEITO 6: Loops aninhados
# Um loop dentro do outro.
# ─────────────────────────────────────────────

print("\n=== Tabuada do 3 ===")
for i in range(1, 11):
    print(f"  3 x {i:2} = {3 * i}")  # :2 formata com 2 casas

print("\n=== Mini tabuada ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()  # quebra de linha após cada linha da tabuada


# ─────────────────────────────────────────────
# CONCEITO 7: while com input (loop de validação)
# Padrão muito comum em programas reais.
# ─────────────────────────────────────────────

print("\n=== Exemplo: loop de validação ===")
# Simula sem input para rodar direto
tentativas = ["0", "7", "5"]  # simula entradas do usuário
for tentativa in tentativas:
    numero = int(tentativa)
    if 1 <= numero <= 10:
        print(f"  '{numero}' é válido! ✓")
        break
    else:
        print(f"  '{numero}' inválido, tente novamente.")


# ──────────────────────────────────────────────────────────────
# 🏋️  EXERCÍCIOS
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1
# Imprima todos os números de 1 a 100 que são
# divisíveis por 3 OU por 5 (mas não por ambos).
# Dica: use % para verificar divisibilidade.

# SEU CÓDIGO AQUI:


# EXERCÍCIO 2
# Calcule a soma de todos os números de 1 a N.
# Peça N ao usuário. Para N=100, a resposta é 5050.

# SEU CÓDIGO AQUI:


# EXERCÍCIO 3
# Crie uma tabuada interativa:
# Peça um número e mostre a tabuada completa (1 a 10).

# SEU CÓDIGO AQUI:


# EXERCÍCIO 4 (desafio)
# Faça um programa que inverte uma string usando loop.
# Ex: "Python" → "nohtyP"
# Dica: construa a string de trás pra frente.

# SEU CÓDIGO AQUI:


# ──────────────────────────────────────────────────────────────
# ✅ GABARITO
# ──────────────────────────────────────────────────────────────

"""
# EXERCÍCIO 1
for n in range(1, 101):
    div3 = n % 3 == 0
    div5 = n % 5 == 0
    if div3 != div5:   # XOR: um ou outro, não ambos
        print(n, end=" ")
print()

# EXERCÍCIO 2
n = int(input("Digite N: "))
soma = 0
for i in range(1, n + 1):
    soma += i
print(f"Soma de 1 a {n} = {soma}")

# EXERCÍCIO 3
numero = int(input("Tabuada de qual número? "))
for i in range(1, 11):
    print(f"{numero} x {i:2} = {numero * i}")

# EXERCÍCIO 4
palavra = input("Digite uma palavra: ")
invertida = ""
for letra in palavra:
    invertida = letra + invertida
print(f"Invertida: {invertida}")
"""
