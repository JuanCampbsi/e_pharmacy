from datetime import datetime
from typing import List
from e_farmacia.Cliente import Cliente
from e_farmacia.e_medicamentos.Medicamento import Medicamento
from e_farmacia.e_medicamentos.MedicamentoQuimioterapico import MedicamentoQuimioterapico
from e_farmacia.Venda import Venda
from e_farmacia.Laboratorio import Laboratorio


class Farmacia:
    def __init__(self):
        self.__clientes: List[Cliente] = []
        self.__medicamentos: List[Medicamento] = []
        self.__vendas: List[Venda] = []
        self.__laboratorios: List[Laboratorio] = []

    @property
    def clientes(self) -> List[Cliente]:
        return self.__clientes

    @property
    def medicamentos(self) -> List[Medicamento]:
        return self.__medicamentos

    @property
    def vendas(self) -> List[Venda]:
        return self.__vendas

    @property
    def laboratorios(self) -> List[Laboratorio]:
        return self.__laboratorios
    
    def adicionar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def adicionar_medicamento(self, medicamento: Medicamento):
        self.__medicamentos.append(medicamento)

    def adicionar_venda(self, venda: Venda):
        self.__vendas.append(venda)

    def adicionar_laboratorio(self, laboratorio: Laboratorio):
        self.__laboratorios.append(laboratorio)

    def buscar_cliente_por_cpf(self, cpf: str) -> Cliente:
        return next((cliente for cliente in self.__clientes if cliente.cpf == cpf), None)

    def buscar_medicamento_por_nome(self, nome: str) -> Medicamento:
        return next((medicamento for medicamento in self.__medicamentos if medicamento.nome == nome), None)
    
    @staticmethod
    def calcular_desconto(cliente: Cliente, valor_total: float) -> float:
        if cliente.data_nascimento.year >= 65:
            return valor_total * 0.2
        elif valor_total > 150:
            return valor_total * 0.1
        return 0

    def efetuar_venda(self, cliente_cpf: str, lista_medicamentos: List[Medicamento]) -> None:
        try:
            cliente = self.buscar_cliente_por_cpf(cliente_cpf)
            if not cliente:
                print("Cliente não encontrado!")
                return

            valor_total = sum(medicamento.preco for medicamento in lista_medicamentos)
            desconto = self.calcular_desconto(cliente, valor_total)
            valor_com_desconto = valor_total - desconto

            venda = Venda(datetime.now(), lista_medicamentos, cliente, valor_com_desconto)

            for medicamento in lista_medicamentos:
                if isinstance(medicamento, MedicamentoQuimioterapico) and medicamento.necessita_receita:
                    print(f"ALERTA: Verifique a receita para o medicamento: {medicamento.nome}")

            self.adicionar_venda(venda)
            print(f"Venda efetuada com sucesso! Valor total: R${valor_com_desconto:.2f}")

        except AttributeError:
            print("Erro: Um dos medicamentos na lista não possui um atributo necessário.")
        except Exception as e:
            print(f"Ocorreu um erro durante a venda: {e}")

