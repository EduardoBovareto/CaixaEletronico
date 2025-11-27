from random import randint as rd

def Sake():
    pass

def Balance():
    print('Passou pelo balance')

def Controlbalance():#purchase and Exits
    pass

def Deposit():#deposit
    pass
def Expenses():#Calculate Expenses and statics your count
    pass

def ConfigLead(name, cpf, users):
    print('Passou por aqui')

def Leads(name,cpf):#Data of leads that in future be Database
    users = { 
    "joao":{
            "idade": 30, 
            "email": "joao@gmail.com", 
            "cpf": str(list(rd(0,9) for i in range(0,11)))
           },
    "maria":{
            "idade": 25, 
            "email": "maria@gmail.com",
            "cpf": str(list(rd(0,9) for i in range(0,11)))
            }
    }
    
    if name not in users or cpf not in users:
        registered = ConfigLead(name, cpf, users)
        return registered #new name in bank!

def Main(name, cpf) -> str:#Major Page
    operation = -1 #control variable
    print(f'Hello Sr(a){name}')

    registered = Leads(name, cpf)#Verify lead
    if registered != None:#ainda nao chegou aqui
        operation = int(input('''Write an option under that want to do now:
    1.See balance
    2.Make purchase
    3.Make sake
    4.Make Deposit
    5. Loan
    6.Syndicate
    7.Calculate Expenses
    '''))
    if operation == 1:
        Balance() #see the balance in your count
        
print(f'\nBEM VINDO AO BANCO PAN!\n')
name = input('Write your name for start: ').lower()
cpf = input('\nWrite your number identification: ').strip()
Main(name, cpf)