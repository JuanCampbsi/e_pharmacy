from e_farmacia.e_medicamentos.Medicamento import Medicamento
class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome, principio_ativo, laboratorio, descricao, precisa_receita):
        super().__init__(nome, principio_ativo, laboratorio, descricao)
        self.precisa_receita = precisa_receita


    # def _str_(self):
    #     return f"MedicamentoQuimioterapico({super()._str_()}, precisa_receita={self.precisa_receita})"
    #     {}', laboratorio='{}', descricao='{}', precisa_receita='{}')".format(self.nome, self.principio_ativo, self.laboratorio, self.descricao, self.precisa_receita)