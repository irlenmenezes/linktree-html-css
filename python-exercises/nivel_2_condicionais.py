"""
╔══════════════════════════════════════════════════════════════╗
║       PYTHON DO ZERO - NÍVEL 2: Condicionais                ║
╚══════════════════════════════════════════════════════════════╝

O que você vai aprender aqui:
  - if, elif, else
  - Operadores de comparação: ==, !=, >, <, >=, <=
  - Operadores lógicos: and, or, not
  - Condicionais aninhadas

Para rodar este arquivo:
  python nivel_2_condicionais.py
"""

# ─────────────────────────────────────────────
# CONCEITO 1: if / else
# "Se isso for verdade, faça X. Senão, faça Y."
# ATENÇÃO: indentação (4 espaços) é obrigatória!
# ─────────────────────────────────────────────

print("=== if / else ===")
temperatura = 35

if temperatura > 30:
    print("Está quente! Beba água.")
else:
    print("Temperatura agradável.")


# ─────────────────────────────────────────────
# CONCEITO 2: elif (else if)
# Quando há mais de duas possibilidades.
# ─────────────────────────────────────────────

print("\n=== if / elif / else ===")
nota = 75

if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
elif nota >= 60:
    conceito = "D"
else:
    conceito = "F"

print(f"Nota {nota} → Conceito {conceito}")


# ─────────────────────────────────────────────
# CONCEITO 3: Operadores de comparação
# ─────────────────────────────────────────────

print("\n=== Comparações ===")
x = 10
y = 20

print(f"x == y → {x == y}")   # igual
print(f"x != y → {x != y}")   # diferente
print(f"x > y  → {x > y}")    # maior
print(f"x < y  → {x < y}")    # menor
print(f"x >= y → {x >= y}")   # maior ou igual
print(f"x <= y → {x <= y}")   # menor ou igual


# ─────────────────────────────────────────────
# CONCEITO 4: Operadores lógicos
# 'and' → ambos devem ser verdadeiros
# 'or'  → pelo menos um deve ser verdadeiro
# 'not' → inverte o valor
# ─────────────────────────────────────────────

print("\n=== Operadores lógicos ===")
tem_cnh = True
tem_carro = False

if tem_cnh and tem_carro:
    print("Pode dirigir!")
elif tem_cnh or tem_carro:
    print("Tem metade do necessário.")
else:
    print("Não pode dirigir.")

# 'not' inverte
print(f"not True  = {not True}")
print(f"not False = {not False}")


# ─────────────────────────────────────────────
# CONCEITO 5: Condicionais com input()
# ─────────────────────────────────────────────

print("\n=== Verificador de par/ímpar ===")
# Descomente para testar interativamente:
# numero = int(input("Digite um número: "))

numero = 7  # valor fixo para o exemplo rodar direto

if numero % 2 == 0:
    print(f"{numero} é PAR")
else:
    print(f"{numero} é ÍMPAR")


# ─────────────────────────────────────────────
# CONCEITO 6: Operador ternário (if em uma linha)
# Útil para atribuições simples.
# ─────────────────────────────────────────────

print("\n=== Operador ternário ===")
idade = 17
status = "maior de idade" if idade >= 18 else "menor de idade"
print(f"Com {idade} anos, você é {status}.")


# ──────────────────────────────────────────────────────────────
# 🏋️  EXERCÍCIOS
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1
# Crie um programa que receba a idade de uma pessoa e diga:
# - "Criança" se < 12
# - "Adolescente" se entre 12 e 17
# - "Adulto" se entre 18 e 59
# - "Idoso" se >= 60

# SEU CÓDIGO AQUI:
# idade = int(input("Qual a sua idade? "))
# if ...:
#     ...


# EXERCÍCIO 2
# Faça um verificador de login simples.
# Defina usuario = "admin" e senha = "1234"
# Se o usuário digitar corretamente, mostre "Acesso permitido!"
# Senão, mostre "Usuário ou senha incorretos."

# SEU CÓDIGO AQUI:
# usuario_correto = "admin"
# senha_correta = "1234"
# usuario = input("Usuário: ")
# senha = input("Senha: ")
# if ...:
#     ...


# EXERCÍCIO 3
# Crie uma calculadora simples.
# Peça dois números e uma operação (+, -, *, /)
# Exiba o resultado. Atenção: divisão por zero!

# SEU CÓDIGO AQUI:
# num1 = float(input("Primeiro número: "))
# op   = input("Operação (+, -, *, /): ")
# num2 = float(input("Segundo número: "))
# if op == "+" :
#     ...


# ──────────────────────────────────────────────────────────────
# ✅ GABARITO
# ──────────────────────────────────────────────────────────────

"""
# EXERCÍCIO 1
idade = int(input("Qual a sua idade? "))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

# EXERCÍCIO 2
usuario_correto = "admin"
senha_correta = "1234"
usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == usuario_correto and senha == senha_correta:
    print("Acesso permitido!")
else:
    print("Usuário ou senha incorretos.")

# EXERCÍCIO 3
num1 = float(input("Primeiro número: "))
op   = input("Operação (+, -, *, /): ")
num2 = float(input("Segundo número: "))
if op == "+":
    print(f"Resultado: {num1 + num2}")
elif op == "-":
    print(f"Resultado: {num1 - num2}")
elif op == "*":
    print(f"Resultado: {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("Erro: divisão por zero!")
    else:
        print(f"Resultado: {num1 / num2}")
else:
    print("Operação inválida.")
"""
