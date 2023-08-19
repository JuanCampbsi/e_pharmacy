from e_farmacia.e_medicamentos.Medicamento import Medicamento


class MedicamentoFitoterapico(Medicamento):
    def _str_(self):
        return f"MedicamentoFitoterapico({super().__str__()})"
