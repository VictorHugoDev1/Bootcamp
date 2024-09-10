import uuid

class Conta:
    def __init__(self, nome, saldo_inicial=0):
        self.id = uuid.uuid4()
        self.nome = nome
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser positivo.')
    
    def retirar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Retirada de R${valor:.2f} realizada com sucesso.')
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor da retirada deve ser positivo.')

    def visualizar_saldo(self):
        return f'Saldo atual: R${self.saldo:.2f}'

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, nome, saldo_inicial=0):
        conta = Conta(nome, saldo_inicial)
        self.contas[conta.id] = conta
        print(f'Conta criada com sucesso para {nome}.')
        return conta.id

    def transferir(self, id_origem, id_destino, valor):
        if id_origem in self.contas and id_destino in self.contas:
            conta_origem = self.contas[id_origem]
            conta_destino = self.contas[id_destino]
            
            if valor > 0 and valor <= conta_origem.saldo:
                conta_origem.retirar(valor)
                conta_destino.depositar(valor)
                print(f'Transferência de R${valor:.2f} realizada com sucesso.')
            else:
                print('Valor inválido ou saldo insuficiente.')
        else:
            print('Contas informadas não existem.')

banco = Banco()
id_conta1 = banco.criar_conta('Victor', 1000)
id_conta2 = banco.criar_conta('Maria', 500)

conta1 = banco.contas[id_conta1]
conta2 = banco.contas[id_conta2]

conta1.depositar(200)
conta1.retirar(150)
banco.transferir(id_conta1, id_conta2, 100)

print(conta1.visualizar_saldo())
print(conta2.visualizar_saldo())
