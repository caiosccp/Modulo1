class CaixaEletronico:
    
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome

    def sacar(self, valor_saque):
        valor = valor_saque
        resto = -1
        notas_entregues = []
        for valor_nota in self.notas:
            qtd_notas = valor // valor_nota
            resto = valor % valor_nota
            valor = resto
            if qtd_notas > 0:
                notas_entregues.append(f'{qtd_notas} nota de R$ {valor_nota},00')

        if resto == 0:
            self.imprimir_resultado(notas_entregues)
        else:
            print(f'Não é possível sacar o valor R$ {valor_saque},00')
    
    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))

if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Ultima Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(valor)