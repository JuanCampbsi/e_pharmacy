class Medicamento:
    def _init_(self, nome, principio_ativo, laboratorio, descricao):
        self.nome = nome
        self.principio_ativo = principio_ativo
        self.laboratorio = laboratorio
        self.descricao = descricao

    def _str_(self):
        return f"Medicamento(nome='{self.nome}', principio_ativo='{self.principio_ativo}', laboratorio='{self.laboratorio}', descricao='{self.descricao}')"