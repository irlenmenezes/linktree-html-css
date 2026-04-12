"""
╔══════════════════════════════════════════════════════════════╗
║         PYTHON DO ZERO - NÍVEL 4: Funções                   ║
╚══════════════════════════════════════════════════════════════╝

O que você vai aprender aqui:
  - def e return
  - Parâmetros e argumentos
  - Valores padrão (default)
  - Múltiplos retornos
  - Escopo de variáveis
  - *args e **kwargs (introdução)
  - Funções como objetos (lambda)

Para rodar este arquivo:
  python nivel_4_funcoes.py
"""

# ─────────────────────────────────────────────
# CONCEITO 1: Definindo e chamando funções
# "def" define. "()" chama. "return" devolve.
# ─────────────────────────────────────────────

print("=== Função básica ===")

def saudacao():
    print("Olá! Bem-vindo ao Python!")

saudacao()   # chamando a função
saudacao()   # pode chamar quantas vezes quiser


# ─────────────────────────────────────────────
# CONCEITO 2: Parâmetros e return
# ─────────────────────────────────────────────

print("\n=== Parâmetros e return ===")

def somar(a, b):
    resultado = a + b
    return resultado

soma = somar(3, 7)
print(f"3 + 7 = {soma}")
print(f"10 + 25 = {somar(10, 25)}")


def calcular_area_retangulo(largura, altura):
    return largura * altura

area = calcular_area_retangulo(5, 3)
print(f"Área do retângulo 5x3: {area}")


# ─────────────────────────────────────────────
# CONCEITO 3: Parâmetros com valor padrão
# Se não passar o argumento, usa o padrão.
# ─────────────────────────────────────────────

print("\n=== Parâmetros padrão ===")

def cumprimentar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

print(cumprimentar("Ana"))               # usa padrão
print(cumprimentar("Carlos", "Oi"))      # sobrescreve
print(cumprimentar("Maria", "Bom dia"))  # sobrescreve


# ─────────────────────────────────────────────
# CONCEITO 4: Múltiplos retornos
# Python pode retornar vários valores de uma vez!
# ─────────────────────────────────────────────

print("\n=== Múltiplos retornos ===")

def minmax(lista):
    return min(lista), max(lista)  # retorna uma tupla

menor, maior = minmax([4, 1, 9, 2, 7])
print(f"Menor: {menor}, Maior: {maior}")


def dividir(a, b):
    if b == 0:
        return None, "Divisão por zero!"
    return a / b, None

resultado, erro = dividir(10, 3)
if erro:
    print(f"Erro: {erro}")
else:
    print(f"10 / 3 = {resultado:.2f}")  # :.2f = 2 casas decimais


# ─────────────────────────────────────────────
# CONCEITO 5: Escopo de variáveis
# Variáveis dentro da função não existem fora!
# ─────────────────────────────────────────────

print("\n=== Escopo ===")

mensagem_global = "Sou global"

def mostrar_escopo():
    mensagem_local = "Sou local"
    print(f"  Dentro: '{mensagem_local}'")
    print(f"  Global acessível: '{mensagem_global}'")

mostrar_escopo()
print(f"Fora: '{mensagem_global}'")
# print(mensagem_local)  # ← isso daria erro!


# ─────────────────────────────────────────────
# CONCEITO 6: *args — número variável de argumentos
# ─────────────────────────────────────────────

print("\n=== *args ===")

def somar_tudo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar_tudo(1, 2))
print(somar_tudo(1, 2, 3, 4, 5))
print(somar_tudo(10, 20, 30))


# ─────────────────────────────────────────────
# CONCEITO 7: lambda — funções anônimas
# Para funções simples de uma linha.
# ─────────────────────────────────────────────

print("\n=== lambda ===")

dobrar = lambda x: x * 2
quadrado = lambda x: x ** 2
somar_dois = lambda a, b: a + b

print(f"Dobro de 5: {dobrar(5)}")
print(f"Quadrado de 4: {quadrado(4)}")
print(f"3 + 7: {somar_dois(3, 7)}")

# Lambdas brilham com sorted() e map()
nomes = ["Carlos", "Ana", "Beatriz", "Zé"]
nomes_ordenados = sorted(nomes, key=lambda n: len(n))
print(f"Ordenado por tamanho: {nomes_ordenados}")


# ─────────────────────────────────────────────
# CONCEITO 8: Funções que chamam outras funções
# ─────────────────────────────────────────────

print("\n=== Composição de funções ===")

def eh_par(n):
    return n % 2 == 0

def filtrar_pares(lista):
    pares = []
    for n in lista:
        if eh_par(n):
            pares.append(n)
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Pares: {filtrar_pares(numeros)}")


# ──────────────────────────────────────────────────────────────
# 🏋️  EXERCÍCIOS
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1
# Crie uma função 'fatorial(n)' que calcule n!
# Ex: fatorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# Dica: use um loop ou seja recursivo (bonus!)

# SEU CÓDIGO AQUI:


# EXERCÍCIO 2
# Crie uma função 'eh_primo(n)' que retorne True
# se n for primo e False caso contrário.
# Um número é primo se só divide por 1 e por ele mesmo.

# SEU CÓDIGO AQUI:


# EXERCÍCIO 3
# Crie uma função 'celsius_para_fahrenheit(c)'
# e outra 'fahrenheit_para_celsius(f)'.
# Fórmulas:
#   F = C * 9/5 + 32
#   C = (F - 32) * 5/9

# SEU CÓDIGO AQUI:


# EXERCÍCIO 4 (desafio)
# Crie uma função 'contar_palavras(texto)' que
# retorna um dicionário com cada palavra e sua frequência.
# Ex: "oi oi tchau" → {"oi": 2, "tchau": 1}

# SEU CÓDIGO AQUI:


# ──────────────────────────────────────────────────────────────
# ✅ GABARITO
# ──────────────────────────────────────────────────────────────

"""
# EXERCÍCIO 1
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(fatorial(5))  # 120

# EXERCÍCIO 2
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(2, 20):
    if eh_primo(n):
        print(n, end=" ")

# EXERCÍCIO 3
def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

print(celsius_para_fahrenheit(100))  # 212.0
print(fahrenheit_para_celsius(32))   # 0.0

# EXERCÍCIO 4
def contar_palavras(texto):
    contagem = {}
    for palavra in texto.lower().split():
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

print(contar_palavras("oi oi tchau oi tchau"))
"""
