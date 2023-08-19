from typing import List
from datetime import datetime
from e_farmacia.Cliente import Cliente
from e_farmacia.e_medicamentos.Medicamento import Medicamento


class Venda:
    def __init__(self, data_hora: datetime, produtos: List[Medicamento], cliente: Cliente, valor_total: float):
        self.__data_hora_venda = data_hora
        self.__produtos_vendidos = produtos
        self.__cliente = cliente
        self.__valor_total = valor_total

    @property
    def data_hora_venda(self) -> datetime:
        return self.__data_hora_venda

    @property
    def produtos_vendidos(self) -> List[Medicamento]:
        return self.__produtos_vendidos

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def valor_total(self) -> float:
        return self.__valor_total

    def adicionar_medicamento(self, medicamento: Medicamento, valor: float):
        self.__produtos_vendidos.append(medicamento)
        self.__valor_total += valor

    def aplicar_desconto(self):
        if self.__cliente.is_idoso():
            desconto = 0.20
        elif self.__valor_total > 150:
            desconto = 0.10
        else:
            desconto = 0
        self.__valor_total *= (1 - desconto)

    def __str__(self) -> str:
        return f"Data/Hora: {self.__data_hora_venda}, Cliente: {self.__cliente.nome}, Valor Total: {self.__valor_total}"
