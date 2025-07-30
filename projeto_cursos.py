def existe_arquivo(arq):
    import os
    if os.path.exists(arq):
        return True
    else:
        return False
def menu():
    print("Menu principal:\n")
    print("1. Submenu de Alunos")
    print("2. Submenu de cursos")
    print("3. Submenu de Matriculas")
    print("4. Submenu de Relatórios")
    print("0. Sair")
    opcao = int(input("Escolha uma opção:"))
    return opcao

def submenu(info):
    print(f"Submenu {info}:\n")
    print("1. Listar todos")
    print("2. Listar um")
    print("3. Incluir")
    print("4. Alterar")
    print("5. Excluir")
    print("0. Voltar")
    escolha=int(input("Escolha uma opcao:"))
    return escolha

def listar_alunos_cursos(arq):
    with open(arq, "r") as arquivo:
        elementos= arquivo.readlines()
        i=0
        while i<len(elementos):
            elemento=elementos[i]
            elemento=elemento.split(",")
            if arq=="alunos.txt":
                print(f"CPF:{elemento[0]}")
                print(f"Nome:{elemento[1]}")
                print(f"Data de nascimento:{elemento[2]}")
                print(f"Sexo:{elemento[3]}")
                print(f"Emails:{elemento[4]}")
                print(f"Telefones:{elemento[5]}")
                print("_______________________________")
            elif arq=="cursos.txt":
                print(f"Código do curso:{elemento[0]}")
                print(f"Descrição:{elemento[1]}")
                print(f"Carga horária:{elemento[2]}")
                print(f"Preço:{elemento[3]}")
                print("____________________________________")
            else:
                return False
            i+=1


            

def listar_aluno_curso(arq,id):
    with open(arq, "r") as arquivo:
        elementos= arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos) and not achou:
            elemento=elementos[i]
            elemento=elemento.split(",")
            if id in elemento:
                if arq=="alunos.txt":
                    print(f"CPF:{elemento[0]}")
                    print(f"Nome:{elemento[1]}")
                    print(f"Data de nascimento:{elemento[2]}")
                    print(f"Sexo:{elemento[3]}")
                    print(f"Emails:{elemento[4]}")
                    print(f"Telefones:{elemento[5]}")
                    achou=True
                elif arq=="cursos.txt":
                    print(f"Código do curso:{elemento[0]}")
                    print(f"Descrição:{elemento[1]}")
                    print(f"Carga horária:{elemento[2]}")
                    print(f"Preço:{elemento[3]}")
                    print("____________________________________")
                    achou=True
                else: 
                    return False
            i+=1
        if achou:
            return True
        else:
            return False
            
def incluir_aluno_curso(id,arq): 
    import os 
    if os.path.exists(arq):
        with open(arq, "r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id:
                            achou=True
                        j+=1
                    i+=1
            if achou:
                return False
            else:
                if arq=="alunos.txt":
                    nome=input("Insira o nome do(a) aluno(a):")
                    data=input("Insira da data de nascimento:")
                    sexo=input("Insira o sexo do(a) aluno(a):")
                    emails = input("E-mails (separados por espaço):")
                    telefones = input("Telefones (separados por espaço):")
                    arquivo.write(id+","+nome+","+data+","+sexo+","+emails+","+telefones+"\n")
                    return True
                elif arq=="cursos.txt":
                    nome=input("Digite a descrição do curso:")
                    data=input("Digite a carga horária do curso:")
                    preco=input("Digite o preço do curso:")
                    arquivo.write(id+","+nome+","+data+","+preco+"\n")
                    return True
                else:
                    return False
    else:
        with open(arq,"w") as arquivo:
            if arq=="alunos.txt":
                nome=input("Insira o nome do(a) aluno(a):")
                data=input("Insira da data de nascimento:")
                sexo=input("Insira o sexo do(a) aluno(a):")
                emails = input("E-mails (separados por espaço):")
                telefones = input("Telefones (separados por espaço):")
                arquivo.write(id+","+nome+","+data+","+sexo+","+emails+","+telefones+"\n")
                return True
            elif arq=="cursos.txt":
                nome=input("Digite a descrição do curso:")
                data=input("Digite a carga horária do curso:")
                preco=input("Digite o preço do curso:")
                arquivo.write(id+","+nome+","+data+","+preco+"\n")
                return True
            else:
                return False

        
def alterar_aluno_curso(arq,id,d):
    with open(arq, "r+") as arquivo:
        elementos= arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos) and not achou: # Verificar se o dado a ser alterado a posição existe
            elemento=elementos[i]
            elemento=elemento.split(",")
            if id in elemento:
                dado=input("Digite o novo dado:")
                elemento[d]=dado
                elemento=",".join(elemento)
                elementos[i]=elemento
                with open(arq, "w") as arquivo:
                    arquivo.writelines(elementos)

                return True
            i+=1

def excluir_aluno(arq,id,d):
    if d==0:
        with open(arq, "r+") as arquivo:
            elementos= arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                if id in elemento: 
                    del elementos[i]
                    with open(arq, "w") as arquivo:
                        arquivo.writelines(elementos)
                    return True
                i+=1
    else:
        with open(arq, "r+") as arquivo:
            alunos= arquivo.readlines()
            i=0
            achou=False
            while i<len(alunos) and not achou:
                aluno=alunos[i]
                aluno=aluno.split(",")
                if id in aluno: 
                    aluno[d]="----"
                    aluno=",".join(aluno)
                    alunos[i]=aluno

                    with open(arq, "w") as arquivo:
                        arquivo.writelines(alunos)
                    return True
                i+=1
# cursos



    
    
def main():
    opcao=-1
    while opcao!=0:
        opcao=menu()
        if opcao==0:
            print("Encerrando programa...")
        elif opcao == 1:
            informacao="Aluno"
            nome_arquivo="alunos.txt"
            escolha=submenu(informacao)
            if escolha==0:
                opcao=10*99 #número aleatório para não cancelar o laço e voltar no menu
            elif escolha == 1:
              print("Listando alunos...")
              if existe_arquivo(nome_arquivo):
                  if not listar_alunos_cursos(nome_arquivo):
                      print("Arquivo não encontrado")
              else:
                  print("Arquivo não encontrado")  
                  
            elif escolha == 2:
               chave=input("Digite o CPF do aluno:")
               if existe_arquivo(nome_arquivo):
                  if not listar_aluno_curso(nome_arquivo,chave):
                      print("Aluno não cadastrado")
               else:
                  print("Arquivo não encontrado")
            elif escolha == 3:
               chave=input("Digite o CPF do aluno:")
               if incluir_aluno_curso(chave,nome_arquivo): 
                    print("Aluno cadastrado com sucesso")
               else:
                   print("Aluno já cadastrado")
            elif escolha==4:
                print("Informe o que deseja alterar:")
                print("0. CPF")
                print("1. Nome")
                print("2. Data de nascimento")
                print("3. Sexo")
                print("4. Emails")
                print("5. Telefone")
                dado=int(input("Dado para alterar:"))
                chave=input("Digite o id do aluno:")
                if existe_arquivo(nome_arquivo):
                    if alterar_aluno_curso(nome_arquivo,chave,dado):
                        print("Dados alterados com sucesso")
                    else:
                        print("Aluno não cadastrado ou lista vazia")
                else:
                   print("Arquivo não encontrado") 
            elif escolha==5:
                print("Informe o que deseja excluir:")
                print("0. id")
                print("1. Nome")
                print("2. Data de nascimento")
                print("3. Sexo")
                print("4. Emails")
                print("5. Telefone")
                dado=int(input("Dado para alterar:"))
                chave=input("Digite o id do aluno:")
                if existe_arquivo(nome_arquivo):
                    if excluir_aluno(nome_arquivo,chave,dado):
                        print("Dados excluidos com sucesso")
                    else:
                        print("Aluno não cadastrado ou lista vazia")
                else:
                   print("Arquivo não encontrado") 
            else:
                print("Opção não válida")
        elif opcao==2:
            informacao="cursos"
            nome_arquivo="cursos.txt"  
            escolha=submenu(informacao) 
            if escolha ==0:
                opcao=10*99
            elif escolha == 1:
              print("Listando cursos...")
              if existe_arquivo(nome_arquivo):
                  listar_alunos_cursos(nome_arquivo)
              else:
                  print("Arquivo não encontrado")
            elif escolha == 2:
               chave=input("Código do curso:")
               if existe_arquivo(nome_arquivo):
                  if not listar_aluno_curso(nome_arquivo,chave):
                      print("Curso não cadastrado")
               else:
                  print("Arquivo não encontrado")
            elif escolha ==3:
                chave=input("Digite o Codigo do curso:")
                if incluir_aluno_curso(chave,nome_arquivo): 
                    print("Curso cadastrado com sucesso")
                else:
                   print("Curso já cadastrado")
            elif escolha==4:
                print("Informe o que deseja alterar:")
                print("0. Código")
                print("1. Descrição")
                print("2. Carga Horária")
                print("3. Preço")
                dado=int(input("Dado para alterar:"))
                chave=input("Digite o código do curso:")
                if existe_arquivo(nome_arquivo):
                    if alterar_aluno_curso(nome_arquivo,chave,dado):
                        print("Dados alterados com sucesso")
                    else:
                        print("Aluno não cadastrado ou lista vazia")
                else:
                   print("Arquivo não encontrado")
                


               
        

        # elif opcao == "2":
        #      print("Submenu de cursos")
        #      print("1. Listar cursos")
        #      print("2. Incluir curso")
        #      escolha = input("Escolha uma opção >> ")
        #      if escolha == "1":
        #         listar_elementos(cursos)
        #      elif escolha == "2":
        #         incluir_curso(cursos)

        # elif opcao == "3":
        #      print("Submenu de Matriculas:")
        #      print("1. Listar matriculas")
        #      print("2. Incluir matricula")
        #      if escolha == "1":
        #         listar_elementos(matriculas)
        #      elif escolha == "2":
        #         incluir_matricula(matriculas, alunos, cursos)

        # # elif opcao == "4":
        # #      gerar_relatorio(matriculas, alunos, cursos)

        # elif opcao == "5":
        #      break
main()