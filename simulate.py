from datetime import date, timedelta
from random import randint, choice
from pathlib import Path
from typing import List
from models import Insumo, Consumo

NOMES = [
    'Reagente A', 'Reagente B', 'Kit PCR', 'Pipeta 10ml', 'Pipeta 50ml',
    'Seringa 5ml', 'Tubo 1.5ml', 'Luvas M', 'Luvas G', 'Swab Nasal'
]

def gerar_insumos(n: int = 8, inicio: date = None) -> List[Insumo]:
    inicio = inicio or date.today()
    insumos: List[Insumo] = []
    for i in range(n):
        validade = inicio + timedelta(days=randint(30, 365))
        insumos.append(Insumo(id=i+1, nome=choice(NOMES), validade=validade))
    return insumos

def gerar_consumos(dias: int, insumos: List[Insumo], max_por_dia: int = 5) -> List[Consumo]:
    data_base = date.today() - timedelta(days=dias)
    out: List[Consumo] = []
    for d in range(dias):
        data = data_base + timedelta(days=d+1)
        eventos = randint(1, max_por_dia)
        for _ in range(eventos):
            ins = choice(insumos)
            qtd = randint(1, 50)
            out.append(Consumo(data=data, insumo_id=ins.id, nome=ins.nome, quantidade=qtd, validade=ins.validade))
    return out

def salvar_csv(consumos: List[Consumo], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        f.write('data,insumo_id,nome,quantidade,validade\n')
        for c in consumos:
            f.write(f"{c.data.isoformat()},{c.insumo_id},\"{c.nome}\",{c.quantidade},{c.validade.isoformat()}\n")
