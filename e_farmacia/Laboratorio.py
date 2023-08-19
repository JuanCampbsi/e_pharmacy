class Laboratorio:
    def _init_(self, nome, endereco, telefone, cidade, estado):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

    def _str_(self):
        return f"Laboratorio(nome='{self.nome}', endereco='{self.endereco}', telefone='{self.telefone}', cidade='{self.cidade}', estado='{self.estado}')"