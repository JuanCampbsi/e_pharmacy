from e_farmacia.Laboratorio import Laboratorio


class Medicamento:
    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio,
                 descricao: str, preco: float):
        self.__nome = nome
        self.__principal_composto = principal_composto
        self.__laboratorio = laboratorio
        self.__descricao = descricao
        self.__preco = preco

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def principal_composto(self) -> str:
        return self.__principal_composto

    @principal_composto.setter
    def principal_composto(self, principal_composto: str):
        self.__principal_composto = principal_composto

    @property
    def laboratorio(self) -> Laboratorio:
        return self.__laboratorio

    @laboratorio.setter
    def laboratorio(self, laboratorio: Laboratorio):
        self.__laboratorio = laboratorio

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço deve ser positivo.")

    def __str__(self) -> str:
        return f"{self.__nome}, {self.__principal_composto}, {self.__laboratorio.nome}, {self.__descricao}"

