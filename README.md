# Desafio – Baixa visibilidade no apontamento de consumo 

Este projeto resolve o desafio proposto nas imagens: simulamos o consumo diário de insumos em unidades de diagnóstico e
organizamos os dados usando **Python**:
- **Fila** e **Pilha**
- **Busca sequencial** e **busca binária** 
- **Ordenação** com **Merge Sort** e **Quick Sort** 
- **Relatório** explicando o uso no contexto do problema


## Como rodar (Python 3.10+)
```bash
python app.py
```

O menu interativo demonstra cada item da rubrica. Gere o **relatório** escolhendo a opção apropriada.

## Estrutura
- `models.py`: `Insumo`, `Consumo` (dataclasses somente)
- `structures.py`: `Queue`, `Stack`
- `search.py`: `linear_search`, `binary_search`
- `sort_algos.py`: `merge_sort`, `quick_sort`
- `util_algos.py`: `min_by`, `max_by` (scans manuais)
- `simulate.py`: geração de dados sintéticos e CSV
- `app.py`: CLI, uso de fila/pilha, buscas, ordenações e geração de `relatorio.md`
- `tests/`: testes unitários simples
