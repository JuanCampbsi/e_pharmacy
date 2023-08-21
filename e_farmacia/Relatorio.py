from collections import Counter
from datetime import datetime
from typing import List
from e_farmacia.Cliente import Cliente
from e_farmacia.e_medicamentos.Medicamento import Medicamento
from e_farmacia.e_medicamentos.MedicamentoQuimioterapico import MedicamentoQuimioterapico
from e_farmacia.Venda import Venda
from e_farmacia.Laboratorio import Laboratorio
import Farmacia

class Relatorio(Farmacia):
    def __init__(self):
        super().__init__()
    
    def relatorio_cliente_ordem(self,clientes: List[Cliente]):
        clientes_ordenados = sorted(clientes, key=lambda cliente: cliente.nome)
        for cliente in clientes_ordenados:
            print(cliente)
    
    def relatorio_medicamento_ordem(medicamentos):
        mds = medicamentos
        ordem_medicamentos = sorted(mds)
        print(ordem_medicamentos)
        return
    
    def relatorio_quimio_fito():
        return
    
    # Imprimir sempre no fechamento do sistema
    def relatorio_mais_vendido(vendas: List[Venda]) -> tuple:
        medicamento_contador = Counter()
        valor_total_medicamento = {}

        for venda in vendas:
            for medicamento in venda.produtos_vendidos:
                medicamento_contador[medicamento.nome] += 1
                valor_total_medicamento[medicamento.nome] = valor_total_medicamento.get(medicamento.nome, 0) + venda.valor_total

        mais_vendido = medicamento_contador.most_common(1)
        if mais_vendido:
            nome_medicamento, quantidade = mais_vendido[0]
            valor_total = valor_total_medicamento[nome_medicamento]
            return nome_medicamento, quantidade, valor_total
        else:
            return None, 0, 0.0
    #Exemplo de uso
    #vendas = [...]  # Lista de instâncias da classe Venda
    #medicamento, quantidade, valor_total = medicamento_mais_vendido(vendas)
        
    def relatorio_quantidade_atendimento(vendas: List[Venda]) -> int:
        clientes_atendidos = set()

        for venda in vendas:
            clientes_atendidos.add(venda.cliente)

        return len(clientes_atendidos)
    
    def relatorio_quimio_dia():
        return
    
    def relatatorio_fito_dia():
        return