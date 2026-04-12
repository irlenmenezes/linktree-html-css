"""
╔══════════════════════════════════════════════════════════════╗
║        PYTHON DO ZERO - NÍVEL 1: Variáveis e Tipos          ║
╚══════════════════════════════════════════════════════════════╝

O que você vai aprender aqui:
  - O que são variáveis
  - Tipos básicos: int, float, str, bool
  - Como usar print() e input()
  - Conversão de tipos (type casting)

Para rodar este arquivo:
  python nivel_1_variaveis_e_tipos.py
"""

# ─────────────────────────────────────────────
# CONCEITO 1: Variáveis
# Uma variável é uma "caixa" que guarda um valor.
# Você escolhe o nome e Python descobre o tipo.
# ─────────────────────────────────────────────

nome = "Ana"           # str  → texto (sempre entre aspas)
idade = 25             # int  → número inteiro
altura = 1.68          # float → número decimal
estudante = True       # bool → verdadeiro ou falso

print("=== Minhas variáveis ===")
print(nome)
print(idade)
print(altura)
print(estudante)

# type() mostra qual é o tipo da variável
print("\n=== Tipos ===")
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))


# ─────────────────────────────────────────────
# CONCEITO 2: print() com f-string
# f-string é a forma moderna de montar textos.
# Coloque um f antes das aspas e use {} para
# embutir variáveis diretamente no texto.
# ─────────────────────────────────────────────

print("\n=== f-string ===")
print(f"Olá, me chamo {nome}, tenho {idade} anos e {altura}m de altura.")
print(f"Sou estudante? {estudante}")


# ─────────────────────────────────────────────
# CONCEITO 3: Operações básicas
# ─────────────────────────────────────────────

print("\n=== Matemática ===")
a = 10
b = 3

print(f"{a} + {b} = {a + b}")    # soma
print(f"{a} - {b} = {a - b}")    # subtração
print(f"{a} * {b} = {a * b}")    # multiplicação
print(f"{a} / {b} = {a / b}")    # divisão (resultado float)
print(f"{a} // {b} = {a // b}")  # divisão inteira (sem decimais)
print(f"{a} % {b} = {a % b}")    # resto da divisão (módulo)
print(f"{a} ** {b} = {a ** b}")  # potência (10³)


# ─────────────────────────────────────────────
# CONCEITO 4: Conversão de tipos (casting)
# Às vezes você precisa transformar um tipo em outro.
# ─────────────────────────────────────────────

print("\n=== Conversão de tipos ===")
numero_texto = "42"          # isso é uma str, não dá pra somar
numero_real = int(numero_texto)  # convertendo para int
print(f"'{numero_texto}' virou {numero_real}, tipo: {type(numero_real)}")

preco = 9.99
print(f"{preco} como inteiro: {int(preco)}")    # perde os decimais
print(f"42 como float: {float(42)}")
print(f"True como int: {int(True)}")             # True = 1, False = 0


# ──────────────────────────────────────────────────────────────
# 🏋️  EXERCÍCIOS (descomente e complete o código)
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1
# Crie variáveis com seu nome, sua idade e sua cidade.
# Depois imprima uma frase usando f-string.
# Exemplo de saída: "Me chamo João, tenho 30 anos e moro em SP."

# SEU CÓDIGO AQUI:
# meu_nome = "..."
# minha_idade = ...
# minha_cidade = "..."
# print(f"...")


# EXERCÍCIO 2
# Peça ao usuário para digitar dois números inteiros,
# some eles e mostre o resultado.
# Lembre-se: input() sempre retorna str, converta para int!

# SEU CÓDIGO AQUI:
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(f"A soma é: {num1 + num2}")


# EXERCÍCIO 3
# Crie uma variável chamada 'raio' com o valor 5.
# Calcule a área do círculo: area = 3.14159 * raio ** 2
# Mostre: "A área do círculo com raio 5 é 78.53975"

# SEU CÓDIGO AQUI:
# raio = ...
# area = ...
# print(f"...")


# ──────────────────────────────────────────────────────────────
# ✅ GABARITO (só olhe depois de tentar!)
# ──────────────────────────────────────────────────────────────

"""
# EXERCÍCIO 1
meu_nome = "João"
minha_idade = 30
minha_cidade = "São Paulo"
print(f"Me chamo {meu_nome}, tenho {minha_idade} anos e moro em {minha_cidade}.")

# EXERCÍCIO 2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"A soma é: {num1 + num2}")

# EXERCÍCIO 3
raio = 5
area = 3.14159 * raio ** 2
print(f"A área do círculo com raio {raio} é {area}")
"""
