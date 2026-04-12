"""
╔══════════════════════════════════════════════════════════════╗
║    PYTHON DO ZERO - NÍVEL 5: Listas e Dicionários           ║
╚══════════════════════════════════════════════════════════════╝

O que você vai aprender aqui:
  - Listas: criação, acesso, métodos
  - Fatiamento (slicing)
  - List comprehension
  - Dicionários: criação, acesso, métodos
  - Conjuntos (sets) e tuplas

Para rodar este arquivo:
  python nivel_5_listas_e_dicionarios.py
"""

# ─────────────────────────────────────────────
# CONCEITO 1: Listas
# Uma lista guarda vários valores em ordem.
# ─────────────────────────────────────────────

print("=== Listas ===")

frutas = ["maçã", "banana", "laranja", "uva", "manga"]
print(f"Lista: {frutas}")
print(f"Tamanho: {len(frutas)}")

# Acessando por índice (começa em 0!)
print(f"Primeira: {frutas[0]}")
print(f"Última:   {frutas[-1]}")   # índice negativo = do fim
print(f"Penúltima:{frutas[-2]}")


# ─────────────────────────────────────────────
# CONCEITO 2: Fatiamento (slicing)
# lista[início:fim:passo]  — fim não incluso
# ─────────────────────────────────────────────

print("\n=== Slicing ===")
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Original:     {numeros}")
print(f"[2:5]:        {numeros[2:5]}")     # índices 2, 3, 4
print(f"[:4]:         {numeros[:4]}")      # do início até 3
print(f"[6:]:         {numeros[6:]}")      # do 6 até o fim
print(f"[::2]:        {numeros[::2]}")     # de 2 em 2 (pares)
print(f"[::-1]:       {numeros[::-1]}")    # invertida!


# ─────────────────────────────────────────────
# CONCEITO 3: Métodos de lista
# ─────────────────────────────────────────────

print("\n=== Métodos de lista ===")
lista = [3, 1, 4, 1, 5, 9, 2, 6]

lista.append(7)          # adiciona no fim
print(f"append(7):  {lista}")

lista.insert(0, 0)       # insere no índice 0
print(f"insert(0,0):{lista}")

lista.remove(1)          # remove PRIMEIRO ocorrência do valor
print(f"remove(1):  {lista}")

removido = lista.pop()   # remove e retorna o último
print(f"pop():      {lista} → removido: {removido}")

lista.sort()             # ordena no lugar
print(f"sort():     {lista}")

lista.reverse()          # inverte no lugar
print(f"reverse():  {lista}")

print(f"count(1):   {lista.count(1)}")    # quantas vezes aparece
print(f"index(9):   {lista.index(9)}")    # em qual posição está


# ─────────────────────────────────────────────
# CONCEITO 4: List Comprehension
# Forma pythônica e elegante de criar listas.
# Sintaxe: [expressão for item in iterável if condição]
# ─────────────────────────────────────────────

print("\n=== List Comprehension ===")

# Jeito longo:
quadrados_longo = []
for i in range(1, 6):
    quadrados_longo.append(i ** 2)

# Jeito pythônico:
quadrados = [i ** 2 for i in range(1, 6)]
print(f"Quadrados: {quadrados}")

# Com filtro:
pares = [i for i in range(20) if i % 2 == 0]
print(f"Pares até 20: {pares}")

# Transformando strings:
nomes = ["ana", "carlos", "beatriz"]
maiusculos = [nome.upper() for nome in nomes]
print(f"Maiúsculos: {maiusculos}")


# ─────────────────────────────────────────────
# CONCEITO 5: Dicionários
# Guarda pares chave → valor.
# ─────────────────────────────────────────────

print("\n=== Dicionários ===")

pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo",
    "ativo": True
}

print(f"Nome:  {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")

# Acessando com .get() — não dá erro se a chave não existe
print(f"Email: {pessoa.get('email', 'não informado')}")

# Adicionando / modificando
pessoa["email"] = "ana@email.com"
pessoa["idade"] = 29
print(f"Depois de modificar: {pessoa}")

# Removendo
del pessoa["ativo"]
removido = pessoa.pop("cidade")
print(f"Removido: {removido}")
print(f"Dicionário final: {pessoa}")


# ─────────────────────────────────────────────
# CONCEITO 6: Iterando dicionários
# ─────────────────────────────────────────────

print("\n=== Iterando dicionário ===")

notas = {"Ana": 9.5, "Bruno": 7.2, "Clara": 8.8, "Diego": 6.0}

print("Chaves:", list(notas.keys()))
print("Valores:", list(notas.values()))

print("\nPares chave-valor:")
for aluno, nota in notas.items():
    status = "aprovado" if nota >= 7 else "reprovado"
    print(f"  {aluno}: {nota} → {status}")


# ─────────────────────────────────────────────
# CONCEITO 7: Tuplas e Sets
# Tupla: como lista, mas imutável (não muda)
# Set: coleção sem duplicatas e sem ordem
# ─────────────────────────────────────────────

print("\n=== Tupla ===")
coordenada = (10.5, -23.4)     # lat, lon
x, y = coordenada               # desempacotamento
print(f"x={x}, y={y}")

print("\n=== Set ===")
letras = {"a", "b", "c", "a", "b", "a"}
print(f"Set (sem duplicatas): {letras}")

lista_com_dup = [1, 2, 2, 3, 3, 3, 4]
sem_duplicatas = list(set(lista_com_dup))
print(f"Removendo duplicatas: {sorted(sem_duplicatas)}")

# Operações de conjunto
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"União:     {a | b}")
print(f"Interseção:{a & b}")
print(f"Diferença: {a - b}")


# ──────────────────────────────────────────────────────────────
# 🏋️  EXERCÍCIOS
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1
# Dado a lista abaixo, use list comprehension para
# criar uma nova lista apenas com números negativos.
numeros_mistos = [5, -3, 8, -1, 0, -7, 4, -2, 9, -6]
# negativos = [...]
# print(negativos)

# EXERCÍCIO 2
# Crie um dicionário que conte a frequência de cada
# caractere em uma string (ignore espaços).
# Ex: "hello" → {'h':1, 'e':1, 'l':2, 'o':1}
texto = "banana"
# frequencia = {}
# for char in texto:
#     ...
# print(frequencia)

# EXERCÍCIO 3
# Crie uma agenda telefônica (dicionário).
# Permita: adicionar contato, buscar contato, listar todos.
# (Implemente as 3 operações)

# EXERCÍCIO 4 (desafio)
# Dada uma lista de palavras, agrupe-as por tamanho.
# Ex: ["oi", "py", "python", "code", "ok"]
# → {2: ["oi", "py", "ok"], 4: ["code"], 6: ["python"]}
palavras = ["oi", "py", "python", "code", "ok", "lua", "rust"]

# ──────────────────────────────────────────────────────────────
# ✅ GABARITO
# ──────────────────────────────────────────────────────────────

"""
# EXERCÍCIO 1
numeros_mistos = [5, -3, 8, -1, 0, -7, 4, -2, 9, -6]
negativos = [n for n in numeros_mistos if n < 0]
print(negativos)  # [-3, -1, -7, -2, -6]

# EXERCÍCIO 2
texto = "banana"
frequencia = {}
for char in texto:
    frequencia[char] = frequencia.get(char, 0) + 1
print(frequencia)  # {'b':1, 'a':3, 'n':2}

# EXERCÍCIO 3
agenda = {}

def adicionar(nome, telefone):
    agenda[nome] = telefone
    print(f"'{nome}' adicionado.")

def buscar(nome):
    return agenda.get(nome, "Contato não encontrado.")

def listar():
    for nome, tel in agenda.items():
        print(f"  {nome}: {tel}")

adicionar("Ana", "(11) 9999-0001")
adicionar("Bruno", "(21) 8888-0002")
print(buscar("Ana"))
listar()

# EXERCÍCIO 4
palavras = ["oi", "py", "python", "code", "ok", "lua", "rust"]
grupos = {}
for palavra in palavras:
    tamanho = len(palavra)
    if tamanho not in grupos:
        grupos[tamanho] = []
    grupos[tamanho].append(palavra)
print(grupos)
"""
