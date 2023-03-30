# Exericio do DojoPuzzles: https://dojopuzzles.com/problems/caixa-eletronico/


class CaixaEletronico:
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome

    def sacar(self, valor_saque):
        # Comece aqui seu código
        notas_entregues = []
        """
        restante = 0
        nota_cem = 100
        nota_cinquenta = 50
        quantidade_notas_100 = valor_saque // nota_cem
        restante = valor_saque % nota_cem

        if quantidade_notas_100 > 0:
            notas_entregues.append(f'{quantidade_notas_100} notas de R$100,00')

        quantidade_notas_50 = restante // nota_cinquenta
        restante = restante % nota_cinquenta

        if quantidade_notas_50 > 0:
            notas_entregues.append(f'{quantidade_notas_50} notas de R$50,00')
        """
        restante = valor_saque
        for nota in self.notas:
            quantidade_notas = restante // nota
            restante = restante % nota

            if quantidade_notas > 0:
                notas_entregues.append(
                    f'{quantidade_notas} notas de R${nota},00'
                )

        if restante == 0:
            self.imprimir_resultado(notas_entregues)
        else:
            print(f'Não é possível sacar o valor R${valor_saque},00 com as notas disponíveis.')


    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))




if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Ultima Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(100)
