from datetime import date


class Cliente:
    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        self.__data_nascimento = data_nascimento

    def is_idoso(self) -> bool:
        return (date.today().year - self.__data_nascimento.year) >= 65

    def __str__(self) -> str:
        return f"CPF: {self.__cpf}, Nome: {self.__nome}, Data de Nascimento: {self.__data_nascimento}"

