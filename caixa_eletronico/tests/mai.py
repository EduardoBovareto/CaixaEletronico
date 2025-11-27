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
name = 'joao'
print(users[name]['salary'])