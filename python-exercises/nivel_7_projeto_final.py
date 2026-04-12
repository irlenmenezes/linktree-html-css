"""
╔══════════════════════════════════════════════════════════════╗
║     PYTHON DO ZERO - NÍVEL 7: Projeto Final Integrador      ║
╚══════════════════════════════════════════════════════════════╝

🎯 OBJETIVO: Construir um sistema de gerenciamento de tarefas
             (To-Do List) aplicando TUDO que foi aprendido.

Conceitos utilizados:
  ✓ Variáveis e tipos (Nível 1)
  ✓ Condicionais (Nível 2)
  ✓ Loops (Nível 3)
  ✓ Funções (Nível 4)
  ✓ Listas e dicionários (Nível 5)
  ✓ Classes e herança (Nível 6)

Para rodar este arquivo:
  python nivel_7_projeto_final.py
"""

from datetime import datetime


# ─────────────────────────────────────────────
# CLASSE: Tarefa
# ─────────────────────────────────────────────

class Tarefa:
    _contador = 0   # atributo de classe para gerar IDs únicos

    def __init__(self, titulo, prioridade="media"):
        Tarefa._contador += 1
        self.id = Tarefa._contador
        self.titulo = titulo
        self.prioridade = prioridade.lower()
        self.concluida = False
        self.criada_em = datetime.now().strftime("%d/%m/%Y %H:%M")

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✓" if self.concluida else "○"
        prioridades = {"alta": "(!)", "media": "( )", "baixa": "(.)"}
        icone = prioridades.get(self.prioridade, "( )")
        return f"[{status}] #{self.id:02d} {icone} {self.titulo}"

    def detalhes(self):
        status = "Concluída" if self.concluida else "Pendente"
        return (
            f"  ID:        #{self.id}\n"
            f"  Título:    {self.titulo}\n"
            f"  Prioridade:{self.prioridade}\n"
            f"  Status:    {status}\n"
            f"  Criada em: {self.criada_em}"
        )


# ─────────────────────────────────────────────
# CLASSE: TarefaComPrazo (herda de Tarefa)
# ─────────────────────────────────────────────

class TarefaComPrazo(Tarefa):
    def __init__(self, titulo, prazo, prioridade="media"):
        super().__init__(titulo, prioridade)
        self.prazo = prazo

    def __str__(self):
        base = super().__str__()
        return f"{base} [prazo: {self.prazo}]"


# ─────────────────────────────────────────────
# CLASSE: GerenciadorTarefas
# ─────────────────────────────────────────────

class GerenciadorTarefas:
    def __init__(self, nome_lista="Minhas Tarefas"):
        self.nome = nome_lista
        self._tarefas = []

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)
        print(f"  + Tarefa adicionada: '{tarefa.titulo}'")

    def concluir(self, id_tarefa):
        tarefa = self._buscar_por_id(id_tarefa)
        if tarefa:
            tarefa.concluir()
            print(f"  ✓ Tarefa #{id_tarefa} concluída!")
        else:
            print(f"  Tarefa #{id_tarefa} não encontrada.")

    def remover(self, id_tarefa):
        tarefa = self._buscar_por_id(id_tarefa)
        if tarefa:
            self._tarefas.remove(tarefa)
            print(f"  - Tarefa #{id_tarefa} removida.")
        else:
            print(f"  Tarefa #{id_tarefa} não encontrada.")

    def listar(self, filtro=None):
        """
        filtro: None = todas
                'pendente' = só pendentes
                'concluida' = só concluídas
                'alta' / 'media' / 'baixa' = por prioridade
        """
        tarefas = self._filtrar(filtro)

        if not tarefas:
            print("  Nenhuma tarefa encontrada.")
            return

        titulo_filtro = f"({filtro})" if filtro else "(todas)"
        print(f"\n  === {self.nome} {titulo_filtro} ===")
        for t in tarefas:
            print(f"  {t}")

    def buscar(self, texto):
        texto = texto.lower()
        encontradas = [t for t in self._tarefas if texto in t.titulo.lower()]
        print(f"\n  Busca por '{texto}':")
        if encontradas:
            for t in encontradas:
                print(f"  {t}")
        else:
            print("  Nenhum resultado.")

    def estatisticas(self):
        total = len(self._tarefas)
        concluidas = sum(1 for t in self._tarefas if t.concluida)
        pendentes = total - concluidas
        pct = (concluidas / total * 100) if total > 0 else 0

        print(f"\n  === Estatísticas de '{self.nome}' ===")
        print(f"  Total:     {total}")
        print(f"  Concluídas:{concluidas} ({pct:.0f}%)")
        print(f"  Pendentes: {pendentes}")

        # Barra de progresso
        barra = int(pct / 5)
        print(f"  Progresso: [{'█' * barra}{'░' * (20 - barra)}] {pct:.0f}%")

    def _buscar_por_id(self, id_tarefa):
        for t in self._tarefas:
            if t.id == id_tarefa:
                return t
        return None

    def _filtrar(self, filtro):
        if filtro is None:
            return self._tarefas
        if filtro == "pendente":
            return [t for t in self._tarefas if not t.concluida]
        if filtro == "concluida":
            return [t for t in self._tarefas if t.concluida]
        # filtro por prioridade
        return [t for t in self._tarefas if t.prioridade == filtro]


# ─────────────────────────────────────────────
# DEMONSTRAÇÃO DO SISTEMA
# ─────────────────────────────────────────────

print("╔══════════════════════════════════╗")
print("║   SISTEMA DE TAREFAS - DEMO      ║")
print("╚══════════════════════════════════╝\n")

# Criando o gerenciador
agenda = GerenciadorTarefas("Aprender Python")

# Adicionando tarefas
print("--- Adicionando tarefas ---")
agenda.adicionar(Tarefa("Estudar variáveis e tipos", prioridade="alta"))
agenda.adicionar(Tarefa("Praticar condicionais", prioridade="alta"))
agenda.adicionar(Tarefa("Fazer exercícios de loops", prioridade="media"))
agenda.adicionar(TarefaComPrazo("Criar funções reutilizáveis", prazo="15/04/2026", prioridade="alta"))
agenda.adicionar(Tarefa("Aprender listas e dicionários", prioridade="media"))
agenda.adicionar(TarefaComPrazo("Estudar orientação a objetos", prazo="20/04/2026", prioridade="media"))
agenda.adicionar(Tarefa("Construir projeto final", prioridade="baixa"))

# Listando todas
agenda.listar()

# Concluindo algumas tarefas
print("\n--- Concluindo tarefas ---")
agenda.concluir(1)
agenda.concluir(2)
agenda.concluir(3)

# Listando por filtro
agenda.listar("pendente")
agenda.listar("concluida")
agenda.listar("alta")

# Busca
print("\n--- Busca ---")
agenda.buscar("loops")
agenda.buscar("python")

# Estatísticas
agenda.estatisticas()

# Removendo uma tarefa
print("\n--- Removendo ---")
agenda.remover(7)
agenda.estatisticas()


# ──────────────────────────────────────────────────────────────
# 🏋️  DESAFIO FINAL
# ──────────────────────────────────────────────────────────────

print("\n" + "="*50)
print("DESAFIO FINAL")
print("="*50)
print("""
Expanda o sistema com as seguintes funcionalidades:

1. EDIÇÃO: Adicione um método editar(id, novo_titulo)
   na classe GerenciadorTarefas.

2. SUBCLASSE: Crie uma classe TarefaRecorrente(Tarefa)
   com atributo 'frequencia' ("diaria", "semanal", "mensal")
   e um método proxima_ocorrencia().

3. EXPORTAÇÃO: Crie uma função exportar_csv(gerenciador, arquivo)
   que salva todas as tarefas em um arquivo .csv.
   Dica: use open() e o módulo csv.

4. MENU INTERATIVO: Transforme a demonstração em um menu
   em loop que aceita comandos do usuário:
   [1] Adicionar  [2] Concluir  [3] Remover
   [4] Listar     [5] Buscar    [0] Sair

5. PERSISTÊNCIA (avançado): Salve e carregue as tarefas
   em JSON para não perder os dados ao fechar o programa.
   Use os módulos 'json' e 'os'.
""")
