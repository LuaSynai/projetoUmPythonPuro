import __init__
from views.view import SubscriptionSevice
from models.database import engine
from models.model import Subscription
from datetime import Datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionSevice(engine)


def start(self):
    while True:
        print('''
        [1] -> Adicionar assinatura
        [2] -> Remover assinatura
        [3] -> Valor total
        [4] -> Gastos últimos 12 meses
        [5] -> Sair
        ''')

        choice = int(input('Escolha uma opção: '))

        if choice == 1:
            self.add_subscription()
        elif choice == 2:
            self.delete_subscription()
        elif choice == 3:
            self.total_value()
        elif choice == 4:
            self.subscription_service.gen_chart()
            #TODO:chamar o metodo pay na interface
        else:
            break
    
    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data de Assinatura: '),'%d/%m/%Y')
        valor = Decimal(input('Valor: '))
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscription_sevice.create(subscription)
        
        
    def delete_subscription(self):
        subscriptions = self.subscription_sevice.list.all()
        #TODO: Quando excluir a assinatura, excluir os pagamentos dela.
        
        print('Escolha qual assinatura deseja excluir')
        
        for i in subscription:
            print(f'[{i.id}] -> {i.empresa}')
            
            choice = int(input('Escolha a assinatura: '))
            self.subscription_sevice.delet(choice)
            print('Assinatura excluida com sucesso')
    
    def total_value(self):
        print(f'Seu valor total mensal em assinatura é: {self.subscription_sevice.total_value()}')
        
        
UI().start()
        
        
        