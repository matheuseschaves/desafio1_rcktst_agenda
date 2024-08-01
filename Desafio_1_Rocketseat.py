def criar_menu():
    print('########## AGENDA TELEFÔNICA #######')
    print('1. Adicionar contato')
    print('2. Editar Contato')
    print('3. Visualizar Agenda')
    print('4. Visualizar Favoritos')
    print('5. Apagar contato')
    print('6. Sair')
    

# criar classe que representa contato
class Contato:
    def __init__(self,id, nome, telefone, email, favorito = False ):
        self.id = id 
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito
        self.atualizar_nome_fvt()

    def atualizar_nome_fvt(self):
        if self.favorito:
            self.nome = self.nome.strip(" ☆") + " ☆"
        else:
            self.nome = self.nome.strip(" ☆")

class Agenda:
    def __init__(self):
        self.contatos = []
        self.favoritos = []
        self.next_id = 1

    def add_contato(self):
        nome = input('Digite o nome do contato:  ')
        telefone = input('Digite o telefone do contato:  ')
        email = input('Digite o email do contato:  ')
        favorito = input('Deseja colocar como favorito ? S - Sim | N - Não |  ').upper()
        favorito = True if favorito == 'S' else False
        
        
        # criaçao do objeto contato
        contato = Contato(self.next_id, nome, telefone, email, favorito)
        self.contatos.append(contato)

        print(f'\n{contato.nome} foi adicionado com sucesso com ID {contato.id}')
        
        if favorito:
            self.favoritos.append(contato)            
            print(f'{contato.nome} foi adicionado com sucesso a lista de favoritos')
        
        self.next_id += 1
        
        
    def editar_contato(self):
        id = int(input('Digite o ID do contato que deseja editar: '))
        for contato in self.contatos:
            if contato.id == id:                
                novo_nome = input('Se deseja alterar o nome de seu contato, digite um novo nome: ') or contato.nome
                telefone = input('Novo telefone:') or contato.telefone
                email = input('Novo email: ') or contato.email
                favorito = input('Deseja favoritar ? S - Sim | N - Não: ').upper()
                favorito = True if favorito == "S" else False
                
                contato.telefone = telefone
                contato.email = email

                if contato.favorito != favorito:
                    contato.favorito = favorito
                    if favorito:
                        self.favoritos.append(contato)
                    else:
                        self.favoritos.remove(contato)

            contato.atualizar_nome_fvt()
                
        
    def del_contato(self):
        deletado = int(input('Digite o id do contato que deseja apagar: '))
        #tentar remover contato
        contato_removido = None
        for contato in self.contatos:
            if contato.id == deletado:
                contato_removido = contato
                self.contatos.remove(contato)
        
        if contato_removido and contato_removido in self.favoritos:
            self.favoritos.remove(contato_removido)

        if contato_removido:
            print(f'\nContato {contato_removido.nome} excluído com sucesso.')
        else:
            print(f'\nContato com ID {deletado} não encontrado.')

    def visualizar_agenda(self):
        print("Relação de contatos:")
        if not self.contatos:
            print('Não há contatos na agenda nesse momento')
        for contato in agenda.contatos:
            print(f'ID: {contato.id} | Nome : {contato.nome} - Telefone :{contato.telefone} - email:{contato.email}' )
            
    def visualizar_fvts(self):
        print("Relação de favoritos:")
        if not self.favoritos:
            print('Não há favoritos na agenda nesse momento')        
        for contato in agenda.favoritos:
            print(f'{contato.nome} - {contato.telefone} - {contato.email}' )
    
    
    def sair(self):
        print('Saindo...')
        quit()        



agenda = Agenda()
while True:
    criar_menu()
    choice = input("O que deseja fazer ?")

    if choice == '1':
        agenda.add_contato()
    elif choice == '2':
        agenda.editar_contato()    
    elif choice == '3':
        agenda.visualizar_agenda()
    elif choice == '4':
        agenda.visualizar_fvts()
    elif choice == '5':
        agenda.del_contato()
    elif choice == '6':
        agenda.sair()

    #☆