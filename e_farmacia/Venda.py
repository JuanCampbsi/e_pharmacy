class Venda:
    def _init_(self, data, hora, produtos, cliente):
        self.data = data
        self.hora = hora
        self.produtos = produtos
        self.cliente = cliente
        self.valor_total = sum(produto.preco for produto in produtos)

    def _str_(self):
        return f"Venda(data='{self.data}', hora='{self.hora}', produtos='{self.produtos}', cliente='{self.cliente}', valor_total='{self.valor_total}')"


