"""
╔══════════════════════════════════════════════════════════════╗
║     PYTHON DO ZERO - NÍVEL 6: Orientação a Objetos          ║
╚══════════════════════════════════════════════════════════════╝

O que você vai aprender aqui:
  - O que é uma classe e um objeto
  - __init__ (construtor)
  - Atributos e métodos
  - self
  - Herança
  - Encapsulamento (privado com __)
  - __str__ e __repr__

Para rodar este arquivo:
  python nivel_6_poo_basico.py
"""

# ─────────────────────────────────────────────
# CONCEITO 1: Classe básica
# Uma classe é um molde. Um objeto é a instância.
# Analogia: Classe = planta de uma casa
#           Objeto = a casa construída
# ─────────────────────────────────────────────

print("=== Classe básica ===")

class Cachorro:
    # __init__ é chamado automaticamente ao criar o objeto
    # 'self' representa a instância em si (o objeto)
    def __init__(self, nome, raca, idade):
        self.nome = nome    # atributo
        self.raca = raca    # atributo
        self.idade = idade  # atributo

    def latir(self):        # método
        return f"{self.nome} diz: Au au!"

    def apresentar(self):
        return f"Eu sou {self.nome}, um {self.raca} de {self.idade} anos."


# Criando objetos (instâncias)
dog1 = Cachorro("Rex", "Pastor Alemão", 3)
dog2 = Cachorro("Bolinha", "Poodle", 5)

print(dog1.latir())
print(dog2.apresentar())
print(f"Nome do dog1: {dog1.nome}")


# ─────────────────────────────────────────────
# CONCEITO 2: __str__ — representação legível
# Chamado quando você usa print(objeto)
# ─────────────────────────────────────────────

print("\n=== __str__ ===")

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"

    def distancia_origem(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


p = Ponto(3, 4)
print(p)                                    # chama __str__
print(f"Distância da origem: {p.distancia_origem()}")


# ─────────────────────────────────────────────
# CONCEITO 3: Atributos de classe vs instância
# Atributo de classe → compartilhado por todos
# Atributo de instância → único de cada objeto
# ─────────────────────────────────────────────

print("\n=== Atributos de classe ===")

class ContaBancaria:
    banco = "Banco Python S/A"      # atributo de CLASSE
    taxa_manutencao = 9.90          # atributo de CLASSE

    def __init__(self, titular, saldo=0):
        self.titular = titular      # atributo de INSTÂNCIA
        self.saldo = saldo          # atributo de INSTÂNCIA

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f}. Saldo: R${self.saldo:.2f}"
        return "Valor inválido."

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= valor
        return f"Saque de R${valor:.2f}. Saldo: R${self.saldo:.2f}"

    def __str__(self):
        return f"Conta de {self.titular} | Saldo: R${self.saldo:.2f}"


conta1 = ContaBancaria("Ana", saldo=1000)
conta2 = ContaBancaria("Bruno")

print(conta1)
print(conta1.depositar(500))
print(conta1.sacar(200))
print(f"Banco: {ContaBancaria.banco}")


# ─────────────────────────────────────────────
# CONCEITO 4: Herança
# Uma classe filha herda atributos e métodos da mãe.
# Use super() para chamar o construtor da mãe.
# ─────────────────────────────────────────────

print("\n=== Herança ===")

class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def falar(self):
        return f"{self.nome} faz: {self.som}!"

    def __str__(self):
        return f"Animal: {self.nome}"


class Gato(Animal):                    # Gato herda de Animal
    def __init__(self, nome, cor):
        super().__init__(nome, "Miau") # chama __init__ do Animal
        self.cor = cor                 # atributo extra

    def ronronar(self):
        return f"{self.nome} ronrona... purrr"

    def __str__(self):
        return f"Gato {self.nome} ({self.cor})"


class Passaro(Animal):
    def __init__(self, nome, pode_voar=True):
        super().__init__(nome, "Piu piu")
        self.pode_voar = pode_voar

    def voar(self):
        if self.pode_voar:
            return f"{self.nome} está voando!"
        return f"{self.nome} não sabe voar."


gato = Gato("Whiskers", "laranja")
passaro = Passaro("Tweety")
pinguim = Passaro("Pinguim", pode_voar=False)

print(gato)
print(gato.falar())        # herdado de Animal
print(gato.ronronar())     # próprio de Gato
print(passaro.voar())
print(pinguim.voar())


# ─────────────────────────────────────────────
# CONCEITO 5: Polimorfismo
# Mesmo método, comportamentos diferentes.
# ─────────────────────────────────────────────

print("\n=== Polimorfismo ===")

animais = [
    Gato("Tom", "cinza"),
    Passaro("Jerry"),
    Gato("Felix", "preto"),
]

for animal in animais:
    print(f"  {animal.falar()}")   # cada um fala do seu jeito


# ─────────────────────────────────────────────
# CONCEITO 6: Encapsulamento
# Atributos com __ são "privados" (convenção).
# ─────────────────────────────────────────────

print("\n=== Encapsulamento ===")

class Cofre:
    def __init__(self, senha):
        self.__senha = senha     # privado: nome vira _Cofre__senha
        self.__saldo = 0

    def depositar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor
            return f"Depositado. Saldo: R${self.__saldo}"
        return "Senha incorreta!"

    def consultar(self, senha):
        if senha == self.__senha:
            return f"Saldo: R${self.__saldo}"
        return "Senha incorreta!"


cofre = Cofre("1234")
print(cofre.depositar(500, "1234"))
print(cofre.depositar(100, "0000"))  # bloqueado
print(cofre.consultar("1234"))
# print(cofre.__senha)  # ← AttributeError!


# ──────────────────────────────────────────────────────────────
# 🏋️  EXERCÍCIOS
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("EXERCÍCIOS")
print("="*50)

# EXERCÍCIO 1
# Crie uma classe 'Retangulo' com atributos largura e altura.
# Métodos: area(), perimetro() e __str__()

# EXERCÍCIO 2
# Crie uma classe 'Pilha' (Stack) com os métodos:
# - push(item): adiciona no topo
# - pop(): remove e retorna do topo
# - peek(): vê o topo sem remover
# - is_empty(): verifica se está vazia
# - __str__(): mostra o estado

# EXERCÍCIO 3 (desafio)
# Crie um sistema de Biblioteca:
# - Classe Livro(titulo, autor, ano)
# - Classe Biblioteca com lista de livros
#   - adicionar(livro)
#   - buscar_por_autor(autor) → retorna lista de livros
#   - livros_por_ano() → retorna ordenados por ano
#   - __str__()

# ──────────────────────────────────────────────────────────────
# ✅ GABARITO
# ──────────────────────────────────────────────────────────────

"""
# EXERCÍCIO 1
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def __str__(self):
        return f"Retângulo {self.largura}x{self.altura} | Área={self.area()} | Perímetro={self.perimetro()}"

r = Retangulo(5, 3)
print(r)

# EXERCÍCIO 2
class Pilha:
    def __init__(self):
        self.__dados = []

    def push(self, item):
        self.__dados.append(item)

    def pop(self):
        if self.is_empty():
            return "Pilha vazia!"
        return self.__dados.pop()

    def peek(self):
        if self.is_empty():
            return "Pilha vazia!"
        return self.__dados[-1]

    def is_empty(self):
        return len(self.__dados) == 0

    def __str__(self):
        return f"Pilha: {self.__dados} (topo → direita)"

p = Pilha()
p.push(1)
p.push(2)
p.push(3)
print(p)
print(p.pop())
print(p.peek())

# EXERCÍCIO 3
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'"{self.titulo}" por {self.autor} ({self.ano})'

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def buscar_por_autor(self, autor):
        return [l for l in self.livros if autor.lower() in l.autor.lower()]

    def livros_por_ano(self):
        return sorted(self.livros, key=lambda l: l.ano)

    def __str__(self):
        return f"Biblioteca '{self.nome}' — {len(self.livros)} livros"

bib = Biblioteca("Minha Biblioteca")
bib.adicionar(Livro("O Senhor dos Anéis", "Tolkien", 1954))
bib.adicionar(Livro("1984", "Orwell", 1949))
bib.adicionar(Livro("A Revolução dos Bichos", "Orwell", 1945))
print(bib)
for livro in bib.buscar_por_autor("Orwell"):
    print(" ", livro)
print("Por ano:")
for livro in bib.livros_por_ano():
    print(" ", livro)
"""
