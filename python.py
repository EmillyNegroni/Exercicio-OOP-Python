#--------------- Exercicio orientação á objetos com Python ---------------#

#Minha classe Pessoa 
class Pessoa :
    def __init__ (self, nome , idade): #init meu construtor 
        self .nome = nome 
        self .idade = idade
         
    def get_nome (self): #pgr name and return 
        return self .nome
    def get_idade (self):
        return  self .idade
            
        
class Pet: #minha classe Pet
    def __init__ (self, nome_pet , nome_dono , data_nasc):
        self .nome_pet = nome_pet
        self .data_nasc = data_nasc
        self .nome_dono = nome_dono
        
        
    def get_nome_pet (self):
        return self .nome_pet
    def get_nome_dono (self):
        return self .nome_dono
    def get_data_nasc (self):
        return self .data_nasc
    
    
        
class Pet_shop: #Minha classe pet shop
    def __init__(self, banho_pet , corte_pet):
        self .banho_pet = banho_pet
        self .corte_pet = corte_pet
    
    def get_banho_pet (self):
        return self .banho_pet
    def get_corte_pet (self):
        return self .corte_pet

pessoa = Pessoa ('Emilly' , 19) #minha var pessoa vai receber os atributos da minha class Pessoa
print(pessoa.get_nome(), pessoa.get_idade()) #vou pegar os valores de pessoa e idade
animais = Pet ('Thor' , 'Emilly' , '26/06/2018') #estou atribuindo os parametros da minha class Pet  para minha Var animais
print(animais.get_nome_pet(), animais.get_nome_dono() , animais.get_data_nasc())
pet_shop = Pet_shop ('Banho: 20,00' , 'Corte: 15,00') #Minha var pet_shop  vai receber os atributos da minha classe Pet_Shop
print(pet_shop.get_banho_pet(), pet_shop.get_corte_pet())
print(animais.get_nome_pet(),'Pet vai receber os seguintes tratamentos:' , pet_shop.get_banho_pet())

