from pathlib import Path
from typing import List
from models import Consumo
from structures import Queue, Stack
from search import linear_search, binary_search
from sort_algos import merge_sort, quick_sort
from util_algos import min_by, max_by
from simulate import gerar_insumos, gerar_consumos, salvar_csv

DATA_DIR = Path('data')
CSV_PATH = DATA_DIR / 'consumo_amostra.csv'
RELATORIO = Path('relatorio.md')

# AQUI ELE TA CRIANDO OS DADOS E SALVANDO NO CSV

def gerar_dados():
    insumos = gerar_insumos(n=10)
    consumos = gerar_consumos(dias=14, insumos=insumos, max_por_dia=6)
    salvar_csv(consumos, CSV_PATH)
    return consumos

def usar_fila(consumos: List[Consumo]) -> Queue[Consumo]:
    fila = Queue[Consumo]()
    for c in merge_sort(consumos, key=lambda x: x.data):
        fila.enqueue(c)
    return fila

def usar_pilha(consumos: List[Consumo]) -> Stack[Consumo]:
    pilha = Stack[Consumo]()
    for c in consumos:
        pilha.push(c)
    return pilha

def menu():
    consumos = gerar_dados()
    fila = usar_fila(consumos)
    pilha = usar_pilha(consumos)

    while True:
        print('\n=== MENU ===')
        print('1) Próximo consumo da FILA (cronológico)')
        print('2) Consultar último consumo (PILHA)')
        print('3) Buscar por nome (sequencial)')
        print('4) Ordenar por QUANTIDADE (Merge) e listar 10 primeiros')
        print('5) Ordenar por VALIDADE (Quick) e listar 10 primeiros')
        print('6) Buscar por nome (BINÁRIA) — requer ordenar por nome antes')
        print('7) Gerar RELATÓRIO Markdown e sair')
        op = input('> ').strip()

        if op == '1':
            if fila.is_empty():
                print('Fila vazia.')
            else:
                c = fila.dequeue()
                print(f"[FILA] {c.data} | {c.nome} | qtd={c.quantidade} | validade={c.validade}")
        elif op == '2':
            if pilha.is_empty():
                print('Pilha vazia.')
            else:
                c = pilha.pop()
                print(f"[PILHA] {c.data} | {c.nome} | qtd={c.quantidade} | validade={c.validade}")
        elif op == '3':
            termo = input('Nome contém: ').strip().lower()
            idx = linear_search(consumos, lambda x: termo in x.nome.lower())
            if idx is None:
                print('Não encontrado.')
            else:
                c = consumos[idx]
                print(f"[SEQ] {c.data} | {c.nome} | qtd={c.quantidade}")
        elif op == '4':
            ordenado = merge_sort(consumos, key=lambda x: x.quantidade)
            for c in ordenado[:10]:
                print(f"[MERGE] qtd={c.quantidade} | {c.nome} | {c.data}")
        elif op == '5':
            ordenado = quick_sort(consumos, key=lambda x: x.validade)
            for c in ordenado[:10]:
                print(f"[QUICK] validade={c.validade} | {c.nome} | {c.data}")
        elif op == '6':
            ordenado = merge_sort(consumos, key=lambda x: x.nome.lower())
            termo = input('Nome exato (para binária): ').strip().lower()
            idx = binary_search(ordenado, key=lambda x: x.nome.lower(), target=termo)
            if idx is None:
                print('Não encontrado.')
            else:
                c = ordenado[idx]
                print(f"[BIN] {c.nome} | {c.data} | qtd={c.quantidade} | val={c.validade}")
        elif op == '7':
            gerar_relatorio(consumos)
            print('Relatório salvo em relatorio.md')
            break
        else:
            print('Opção inválida.')

def gerar_relatorio(consumos: List[Consumo]) -> None:
    total = len(consumos)
    maior = max_by(consumos, key=lambda x: x.quantidade)
    mais_perto = min_by(consumos, key=lambda x: x.validade)

    md = f"""# Relatório – Consumo de Insumos
Este relatório foi gerado automaticamente pelo `app.py`.

## Resumo Executivo dos Dados Coletados
- Total de registros processados: **{total}** movimentações
- Maior saída individual identificada: **{maior.quantidade}** unidades de **{maior.nome}** registrada em **{maior.data}**
- Insumo com prazo de validade mais crítico: **{mais_perto.nome}** (vencimento em **{mais_perto.validade}**)

## Metodologia de Controle Implementada

### 1. Sistema de Processamento Sequencial (Fila)
O controle cronológico das movimentações permite rastreamento temporal preciso dos consumos. A ordenação por data garante que possamos analisar padrões de uso ao longo do período de coleta, essencial para planejamento de reposição.

### 2. Consulta de Histórico Recente (Pilha)
Para auditoria e verificação rápida, mantemos acesso imediato aos últimos registros inseridos no sistema. Isso facilita a confirmação de lançamentos recentes e correção de eventuais inconsistências.

### 3. Localização de Insumos Específicos
- **Busca por similaridade**: Útil quando há incerteza sobre a nomenclatura exata do produto ou para localizar famílias de insumos relacionados
- **Busca exata otimizada**: Após organização alfabética dos dados, permite localização instantânea de produtos específicos, reduzindo tempo de consulta em grandes volumes de dados

### 4. Organização dos Dados por Critérios Clínicos
- **Por volume de consumo**: Identifica os insumos de maior rotatividade, auxiliando no dimensionamento de estoques
- **Por prazo de validade**: Prioriza produtos próximos ao vencimento, reduzindo perdas por expiração e otimizando o giro de estoque

Esta estrutura de controle permite maior precisão no acompanhamento do consumo diário, reduzindo as discrepâncias identificadas no processo manual anterior.

"""
    RELATORIO.write_text(md, encoding='utf-8')

if __name__ == '__main__':
    menu()
