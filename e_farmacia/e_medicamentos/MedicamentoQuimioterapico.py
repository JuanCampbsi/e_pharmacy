from typing import Type
from e_farmacia.e_medicamentos.Medicamento import Medicamento
from e_farmacia.Laboratorio import Laboratorio


class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio,
                 descricao: str, preco: float, necessita_receita: bool):
        super().__init__(nome, principal_composto, laboratorio, descricao, preco)
        self.__necessita_receita = necessita_receita

    @property
    def necessita_receita(self) -> bool:
        return self.__necessita_receita

    @necessita_receita.setter
    def necessita_receita(self, necessita_receita: bool):
        self.__necessita_receita = necessita_receita

    def __str__(self) -> str:
        necessita_receita_str = 'Sim' if self.__necessita_receita else 'Não'
        base_str = super().__str__()
        return (f"{base_str}, Nome: {self.nome}, Principal Composto: {self.principal_composto}, "
                f"Laboratório: {self.laboratorio.nome}, Descrição: {self.descricao}, Preço: R${self.preco:.2f}, "
                f"Necessita Receita: {necessita_receita_str}")
