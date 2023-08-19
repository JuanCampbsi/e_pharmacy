class Cliente:
    def _init_(self, cpf, nome, data_nasc):
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc

    def _str_(self):
        return f"Cliente(cpf='{self.cpf}', nome='{self.nome}', data_nasc='{self.data_nasc}')".format(self.cpf, self.nome, self.data_nasc)