from random import randint as rd
users = { 
    "joao":{
            "year": 30, 
            "email": "joao@gmail.com", 
            "cpf": str(list(rd(0,9) for i in range(0,11))),
            "salary": rd(1300,19990)
           },
    "maria":{
            "idade": 25, 
            "email": "maria@gmail.com",
            "cpf": str(list(rd(0,9) for i in range(0,11))),
            "salary": rd(1100,20090)
            },

    "jose":{
            "idade": 34,
            "email": "jose@tudonauta.com",
            "cpf": "12345678990",
            "salary": rd(900, 5000)
            }
    }

def Sake():
    pass

def Balance(name):#Show the salary
    salary = users[name]['salary']
    print(f'The value of salary is: R${salary:.2f}')


def Controlbalance(name):#purchase and Exits
    purchase = float(input('Write the value your buy: '))
    balance =  users[name]['salary']
    flag = ''
    if balance <= purchase:
        flag = input('will operation use total balance! You want really do buy? y/n').lower()
    
    if flag == 'y':
        balance -= purchase
        print(f'The value actually {balance}')

    else:
        print('Action not doing')

def Deposit():#deposit
    pass
def Expenses():#Calculate Expenses and statics your count
    pass

def ConfigLead(name):
    cpf = input('\nWrite your number identification CPF: ').strip()
    print('Passou por aqui')

def Leads(name):#Data of leads that in future be Database
    wish = ''
    if name not in users:
        print("You don't register in our Bank!\n")
        wish = input('You want register in bank? ').lower()
        if wish == 's':
            registered = ConfigLead(name,users)
            return registered #new name in bank!
        else:
            return None
    else:
        return name

def Main(name) -> str:#Major Page
    operation = -1 #control variable
    print(f"Hello Sr(a) {name}")

    registered = Leads(name)#Verify lead
    if registered != None:
        operation = int(input('''Write an option under that want to do now:
    1.See balance
    2.Make purchase
    3.Make sake
    4.Make Deposit
    5. Loan
    6.Syndicate
    7.Calculate Expenses
    8. EXIT
    9.Back Menu
    '''))
        while True:

            if operation == 8 or registered == None:
                break

            elif operation == 1:
                Balance(name) #see the balance in your count
            
            elif operation == 2:
                result = Controlbalance(name)

            operation = int(input('Select with menu your next operation: '))

print(f'\nBEM VINDO AO BANCO PAN!\n')
name = input('Write your name for start: ').lower()
Main(name)