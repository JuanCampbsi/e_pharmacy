class Laboratorio:
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__cidade = cidade
        self.__estado = estado

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def estado(self) -> str:
        return self.__estado

    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    def __str__(self) -> str:
        return f"{self.__nome}, {self.__endereco}, {self.__telefone}, {self.__cidade}, {self.__estado}"
