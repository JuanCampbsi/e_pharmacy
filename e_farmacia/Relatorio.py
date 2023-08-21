from collections import Counter
from typing import List
from e_farmacia.e_medicamentos.MedicamentoQuimioterapico import MedicamentoQuimioterapico
from e_farmacia.e_medicamentos.Medicamento import Medicamento
from datetime import datetime
from e_farmacia.Farmacia import Farmacia


class Relatorio:
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def relatorio_cliente_ordem(clientes: List[Farmacia.clientes]):
        hoje = datetime.now()
        if not clientes:
            print("Não existem clientes cadastrados.")
            return

        clientes_ordenados = sorted(clientes, key=lambda cliente: cliente.nome)
        for cliente in clientes_ordenados:
            idade = hoje.year - cliente.data_nascimento.year
            print(f"Nome: {cliente.nome} | CPF: {cliente.cpf} | Idade: {idade}")

    @staticmethod
    def relatorio_medicamento_ordem(medicamentos: List[Medicamento]):
        if not medicamentos:
            print("Não existem medicamentos cadastrados.")
            return

        medicamentos_ordenados = sorted(medicamentos, key=lambda med: med.nome)
        for medicamento in medicamentos_ordenados:
            print(f"Nome do medicamento: {medicamento.nome}\nPreço:  R$ {medicamento.preco:.2f}\n"
                  f"Principal composto: {medicamento.principal_composto}\nDescrição: {medicamento.descricao}\n"
                  f"Laboratorio: {medicamento.laboratorio} \n")

    @staticmethod
    def relatorio_quimio_fito(medicamentos:  List[Medicamento]):
        if not medicamentos:
            print("Não existem medicamentos cadastrados.")
            return

        quimioterapicos = [med for med in medicamentos if isinstance(med, MedicamentoQuimioterapico)]
        fitoterapicos = [med for med in medicamentos if not isinstance(med, MedicamentoQuimioterapico)]

        print("Medicamentos Quimioterápicos:")
        for med in quimioterapicos:
            print(f"Nome do medicamento: {med.nome}\nPreço:  R$ {med.preco:.2f}\n"
                  f"Principal composto: {med.principal_composto}\nDescrição: {med.descricao}\n"
                  f"Laboratorio: {med.laboratorio}\n Necessita receita: {med.necessita_receita}")

        print("\nMedicamentos Fitoterápicos:")
        for med in fitoterapicos:
            print(med)
    
    # Imprimir sempre no fechamento do sistema
    @staticmethod
    def relatorio_mais_vendido(vendas: List[Farmacia.vendas]) -> tuple:
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

    @staticmethod
    def relatorio_quantidade_atendimento(vendas: List[Farmacia.vendas]) -> int:
        clientes_atendidos = set()

        for venda in vendas:
            clientes_atendidos.add(venda.cliente)

        return len(clientes_atendidos)

    @staticmethod
    def relatorio_quimio_dia(vendas: List[Farmacia.vendas]) -> str:
        count = 0
        valor = 0.0
        for venda in vendas:
            for medicamento in venda.produtos_vendidos:
                if isinstance(medicamento, MedicamentoQuimioterapico):
                    count += 1
                    valor += medicamento.preco

        return f"\n-Total de remédios Quimioterápicos vendidos: {count}\nValor total: R$ {valor:.2f}"

    @staticmethod
    def relatorio_fito_dia(vendas: List[Farmacia.vendas]) -> str:
        count = 0
        valor = 0.0
        for venda in vendas:
            for medicamento in venda.produtos_vendidos:
                if not isinstance(medicamento, MedicamentoQuimioterapico):
                    count += 1
                    valor += medicamento.preco

        return f"\n-Total de remédios Fitoterápicos vendidos: {count}\nValor total: R$ {valor:.2f}"
