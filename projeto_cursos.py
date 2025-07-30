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
    if info=="relatórios":
        with open("relatorios.txt","a+") as arquivo:
            print(f"Submenu {info}:\n")
            print("0. Voltar")
            print("1. Lista de cursos realizados")
            print("2. Lista de cursos por data")
            print("3. Lista de cursos realizados por aluno")
            escolha=int(input("Escolha uma opcao:"))  
    else:
        print(f"Submenu {info}:\n")
        print("1. Listar todos")
        print("2. Listar um")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("0. Voltar")
        escolha=int(input("Escolha uma opcao:"))
    return escolha
    
    

def listar(arq):
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
            elif arq=="matriculas.txt":
                print(f"CPF:{elemento[0]}")
                print(f"Código do curso:{elemento[1]}")
                print(f"Data de início:{elemento[2]}")
                print(f"Data de termino:{elemento[3]}")
                print(f"Desconto:{elemento[4]}")
                print("____________________________________")
            else:
                return False
            i+=1
    return True


            

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
                if d==(len(elemento)-1):
                    dado=input("Digite o novo dado:")
                    elemento[d]=dado+"\n"
                    elemento=",".join(elemento)
                    elementos[i]=elemento
                    with open(arq, "w") as arquivo:
                        arquivo.writelines(elementos)
                    return True
                else:
                    dado=input("Digite o novo dado:")
                    elemento[d]=dado
                    elemento=",".join(elemento)
                    elementos[i]=elemento
                    with open(arq, "w") as arquivo:
                        arquivo.writelines(elementos)
                    return True
            i+=1

def excluir_aluno_curso(arq,id,d):
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
            elementos= arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                if id in elemento: 
                    if d==(len(elemento)-1):
                        elemento[d]="---\n"
                        elemento=",".join(elemento)
                        elementos[i]=elemento
                        with open(arq, "w") as arquivo:
                            arquivo.writelines(elementos)
                            return True
                    else:
                        elemento[d]="---"
                        elemento=",".join(elemento)
                        elementos[i]=elemento
                        with open(arq, "w") as arquivo:
                            arquivo.writelines(elementos)
                            return True
                i+=1
# Matriculas
def incluir_matricula(arq,chec1,chec2,id1,id2):
    import os
    if os.path.exists(arq):
        with open(chec1, "r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id1:
                            achou=True
                        j+=1
                    i+=1
        if achou:
            with open(chec2, "r+") as arquivo:
                elementos=arquivo.readlines()
                i=0
                achou=False
                while i<len(elementos) and not achou:
                    elemento=elementos[i]
                    elemento=elemento.split(",")
                    j=0
                    if len(elemento)!=0:
                        j=0
                        while j<1:
                            if elemento[0]==id2:
                                achou=True
                            j+=1
                        i+=1
        else:
            return False
        if achou:
            with open(arq, "r+") as arquivo:
                elementos=arquivo.readlines()
                i=0
                achou=False
                while i<len(elementos) and not achou:
                    elemento=elementos[i]
                    elemento=elemento.split(",")
                    j=0
                    if len(elemento)!=0:
                        j=0
                        while j<1:
                            if elemento[0]==id1 and elemento[1]==id2:
                                achou=True
                            j+=1
                        i+=1
                if achou:
                   return False
                else:
                    data1=input("Digite a data de início:")
                    data2=input("Digite a data de termino:")
                    desconto=input("Digite o desconto:")
                    arquivo.write(id1+","+id2+","+data1+","+data2+","+desconto+"\n")
                    return True
        else:
            return False
            
    else:
        with open(arq,"w") as arquivo:
            data1=input("Digite a data de início:")
            data2=input("Digite a data de termino:")
            desconto=input("Digite o desconto:")
            arquivo.write(id1+","+id2+","+data1+","+data2+","+desconto+"\n")
            return True
def listar_matricula(arq,chec1,chec2,id1,id2):
    with open(chec1, "r") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id1:
                            achou=True
                        j+=1
                    i+=1
    if achou:
        with open(chec2, "r") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id2:
                            achou=True
                        j+=1
                    i+=1
    else:
        return False
    if achou:
            with open(arq, "r") as arquivo:
                elementos=arquivo.readlines()
                i=0
                achou=False
                while i<len(elementos) and not achou:
                    elemento=elementos[i]
                    elemento=elemento.split(",")
                    j=0
                    if len(elemento)!=0:
                        j=0
                        while j<1:
                            if elemento[0]==id1 and elemento[1]==id2:
                                achou=True
                            j+=1
                        i+=1
    if achou:
        print(f"CPF:{elemento[0]}")
        print(f"Código do curso:{elemento[1]}")
        print(f"Data de início:{elemento[2]}")
        print(f"Data de termino:{elemento[3]}")
        print(f"Desconto:{elemento[4]}")
        return True
    else:
        return False
def alterar_matricula(arq,chec1,chec2,id1,id2,d):
    with open(chec1, "r+") as arquivo:
        elementos=arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos) and not achou:
            elemento=elementos[i]
            elemento=elemento.split(",")
            j=0
            if len(elemento)!=0:
                j=0
                while j<1:
                    if elemento[0]==id1:
                        achou=True
                    j+=1
                i+=1
    if achou:
        with open(chec2, "r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id2:
                            achou=True
                        j+=1
                    i+=1
    else:
        return False
    if achou:
        with open(arq, "r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id1 and elemento[1]==id2:
                            if d==(len(elemento)-1):
                                dado=input("Digite o novo dado:")
                                elemento[d]=dado+"\n"
                                elemento=",".join(elemento)
                                elementos[i]=elemento
                                with open(arq, "w") as arquivo:
                                    arquivo.writelines(elementos)
                                return True
                            else:
                                dado=input("Digite o novo dado:")
                                elemento[d]=dado
                                elemento=",".join(elemento)
                                elementos[i]=elemento
                                with open(arq, "w") as arquivo:
                                    arquivo.writelines(elementos)
                                return True
                        j+=1
                    i+=1
    else:
        return False
def excluir_matricula(arq,chec1,chec2,id1,id2,d):
    with open(chec1, "r+") as arquivo:
        elementos=arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos) and not achou:
            elemento=elementos[i]
            elemento=elemento.split(",")
            j=0
            if len(elemento)!=0:
                j=0
                while j<1:
                    if elemento[0]==id1:
                        achou=True
                    j+=1
                i+=1
    if achou:
        with open(chec2, "r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id2:
                            achou=True
                        j+=1
                    i+=1
    else:
        return False
    if achou:
        with open(arq, "r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos) and not achou:
                elemento=elementos[i]
                elemento=elemento.split(",")
                j=0
                if len(elemento)!=0:
                    j=0
                    while j<1:
                        if elemento[0]==id1 and elemento[1]==id2:
                           if d==0 or d==1:
                            del elementos[i]
                            with open(arq, "w") as arquivo:
                                arquivo.writelines(elementos)
                            return True
                           else:
                            if d==(len(elemento)-1):
                                elemento[d]="---\n"
                                elemento=",".join(elemento)
                                elementos[i]=elemento
                                with open(arq, "w") as arquivo:
                                    arquivo.writelines(elementos)
                                return True
                            else:
                                elemento[d]="---"
                                elemento=",".join(elemento)
                                elementos[i]=elemento
                                with open(arq, "w") as arquivo:
                                    arquivo.writelines(elementos)
                                return True
                                
                        j+=1
                    i+=1
    else:
        return False    

def relatorio_curso(arq,chec1,chec3,id):
    lista=[]
    with open(chec3,"r+") as arquivo:
        elementos=arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos):
            elemento=elementos[i]
            elemento=elemento.split(",")
            if id in elemento:
                lista.append(elemento[0])
                achou=True
            i+=1
    if achou:
        lista_elemento=[]
        with open(chec1,"r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos):
                elemento=elementos[i]
                elemento=elemento.split(",")
                if elemento[0] in lista:
                    lista_elemento.append(elemento)
                i+=1
        with open(arq,"a+") as arquivo:
            arquivo.write(f"Relatório sobre alunos que fazem o curso:{id}\n")
            i=0
            while i<len(lista_elemento):
                elemento=lista_elemento[i]
                print(f"CPF:{elemento[0]}")
                print(f"Nome:{elemento[1]}")
                print(f"Email:{elemento[4]}")
                print("______________________________________")
                elemento=",".join(elemento)
                arquivo.write(elemento)
                i+=1
        return True
    else:
        return False



def relatorio_data(arq,id1,id2,chec2,chec3):
    from datetime import datetime
    data1 = datetime.strptime(id1, "%d/%m/%Y")
    data2 = datetime.strptime(id2, "%d/%m/%Y")
    lista=[]

    with open(chec3,"r") as arquivo:
        elementos=arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos):
            elemento=elementos[i]
            elemento=elemento.split(",")
            data3=datetime.strptime(elemento[2], "%d/%m/%Y")
            data4=datetime.strptime(elemento[3], "%d/%m/%Y")
            if data3>=data1 and data4<=data2:
                lista.append(elemento[1])
                achou=True
            i+=1
    if achou:
        print("Cursos encontrados:")
        with open(chec2,"r+") as arquivo:
                elementos=arquivo.readlines()
                i=0
                lista_elemento=[]
                while i<len(elementos):
                    elemento=elementos[i]
                    elemento=elemento.split(",")
                    if elemento[0] in lista:
                        print(f"Código do curso:{elemento[0]}")
                        print(f"Descrição:{elemento[1]}")
                        print(f"Carga horária:{elemento[2]}")
                        print(f"Preço:{elemento[3]}")
                        print("____________________________________")
                        lista_elemento.append(elemento)
                    i+=1
        with open(arq,"a+") as desc:
            desc.write(f"Relatório sobre os cursos oferecidos entre as datas {data1} {data2}\n")
            i=0
            while i<len(lista_elemento):
                elemento=lista_elemento[i]
                elemento=",".join(elemento)
                desc.write(elemento)
                i+=1


        return True
    else:
        return False
def relatorio_aluno(arq,id,chec2,chec3):
    lista=[]
    with open(chec3,"r+") as arquivo:
        elementos=arquivo.readlines()
        i=0
        achou=False
        while i<len(elementos):
            elemento=elementos[i]
            elemento=elemento.split(",")
            if id in elemento:
                lista.append(elemento[1])
                achou=True
            i+=1
    if achou:
        lista_elemento=[]
        with open(chec2,"r+") as arquivo:
            elementos=arquivo.readlines()
            i=0
            achou=False
            while i<len(elementos):
                elemento=elementos[i]
                elemento=elemento.split(",")
                if elemento[0] in lista:
                    lista_elemento.append(elemento)
                i+=1
        with open(arq,"a+") as arquivo:
            arquivo.write(f"Relatório sobre os cursos que o {id} faz:\n")
            i=0
            while i<len(lista_elemento):
                elemento=lista_elemento[i]
                print(f"Código do curso:{elemento[0]}")
                print(f"Descrição:{elemento[1]}")
                print(f"Carga horária:{elemento[2]}")
                print(f"Preço:{elemento[3]}")
                print("______________________________________")
                elemento=",".join(elemento)
                arquivo.write(elemento)
                i+=1
        return True
    else:
        return False








def main():
    opcao=-1
    while opcao!=0:
        opcao=menu()
        if opcao==0:
            print("Encerrando programa...")
        elif opcao == 1:
            informacao="aluno"
            nome_arquivo="alunos.txt"
            escolha=submenu(informacao)
            if escolha==0:
                opcao=10*99 #número aleatório para não cancelar o laço e voltar no menu
            elif escolha == 1:
              print("Listando alunos...")
              if existe_arquivo(nome_arquivo):
                  if not listar(nome_arquivo):
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
                if dado>=0 and dado<=5:
                    chave=input("Digite o CPF do aluno:")
                    if existe_arquivo(nome_arquivo):
                        if alterar_aluno_curso(nome_arquivo,chave,dado):
                            print("Dados alterados com sucesso")
                        else:
                            print("Aluno não cadastrado ou lista vazia")
                    else:
                       print("Arquivo não encontrado") 
                else:
                    print("Insira um dado válido")
            elif escolha==5:
                print("Informe o que deseja excluir:")
                print("0. CPF")
                print("1. Nome")
                print("2. Data de nascimento")
                print("3. Sexo")
                print("4. Emails")
                print("5. Telefone")
                dado=int(input("Dado para excluir:"))
                if dado>=0 and dado<=5:
                    chave=input("Digite o CPF do aluno:")
                    if existe_arquivo(nome_arquivo):
                        if excluir_aluno_curso(nome_arquivo,chave,dado):
                            print("Dados excluidos com sucesso")
                        else:
                            print("Aluno não cadastrado ou lista vazia")
                    else:
                       print("Arquivo não encontrado")
                else:
                    print("Insira um dado válido")
                 
            else:
                print("Opção inválida")
        elif opcao==2:
            informacao="cursos"
            nome_arquivo="cursos.txt"  
            escolha=submenu(informacao) 
            if escolha ==0:
                opcao=10*99
            elif escolha == 1:
              print("Listando cursos...")
              if existe_arquivo(nome_arquivo):
                  listar(nome_arquivo)
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
                if dado>=0 and dado<=3:
                    chave=input("Digite o código do curso:")
                    if existe_arquivo(nome_arquivo):
                        if alterar_aluno_curso(nome_arquivo,chave,dado):
                            print("Dados alterados com sucesso")
                        else:
                            print("Curso não cadastrado ou lista vazia")
                    else:
                       print("Arquivo não encontrado")
            elif escolha==5:
                print("Informe o que deseja excluir:")
                print("0. Código")
                print("1. Descrição")
                print("2. Carga Horária")
                print("3. Preço")
                dado=int(input("Dado para excluir:"))
                if dado>=0 and dado<=3:
                    chave=input("Digite o código do curso:")
                    if existe_arquivo(nome_arquivo):
                        if excluir_aluno_curso(nome_arquivo,chave,dado):
                            print("Dados excluidos com sucesso")
                        else:
                            print("Curso não cadastrado ou lista vazia")
                    else:
                       print("Arquivo não encontrado")
            else:
                print("Opção inválida")
        elif opcao==3:
            informacao="matrículas"
            nome_arquivo="matriculas.txt"
            checador1="alunos.txt"
            checador2="cursos.txt"
            escolha=submenu(informacao)
            if escolha==0:
                opcao=10*99 #número aleatório para não cancelar o laço e voltar no menu
            elif escolha == 1:
              print("Listando Matricula...")
              if existe_arquivo(nome_arquivo):
                  if not listar(nome_arquivo):
                      print("Arquivo não encontrado")
              else:
                  print("Arquivo não encontrado")
            elif escolha==2:
                chave1=input("Digite o CPF do aluno:")
                chave2=input("Digite o código do curso:")
                if existe_arquivo(nome_arquivo):
                    if not listar_matricula(nome_arquivo,checador1,checador2,chave1,chave2):
                        print("Matricula não cadastrada")
                else:
                    print("Arquivo não encontrado")
            elif escolha==3:
                chave1=input("Digite o CPF do aluno:")
                chave2=input("Digite o código do curso:")
                if incluir_matricula(nome_arquivo,checador1,checador2,chave1,chave2):
                    print("Matrícula incluida com sucesso")
                else:
                    print("Aluno ou curso não cadastrado")
            elif escolha==4:
                print("Informe o que deseja alterar:")
                print("0. CPF")
                print("1. Código do curso")
                print("2. Data de início")
                print("3. Data de termino")
                print("4. Desconto")
                dado=int(input("Dado para alterar:"))
                if dado>=0 and dado<=4:
                    chave1=input("Digite o CPF do aluno:")
                    chave2=input("Digite o código do curso:")
                    if existe_arquivo(nome_arquivo):
                        if alterar_matricula(nome_arquivo,checador1,checador2,chave1,chave2,dado):
                            print("Dados alterados com sucesso")
                        else:
                            print("Aluno ou curso não cadastrado ou lista vazia")
                    else:
                       print("Arquivo não encontrado") 
                else:
                    print("Insira um dado válido")
            elif escolha==5:
                print("Informe o que deseja excluir:")
                print("0. CPF")
                print("1. Código do curso")
                print("2. Data de início")
                print("3. Data de termino")
                print("4. Desconto")
                dado=int(input("Dado para alterar:"))
                if dado>=0 and dado<=4:
                    chave1=input("Digite o CPF do aluno:")
                    chave2=input("Digite o código do curso:")
                    if existe_arquivo(nome_arquivo):
                        if excluir_matricula(nome_arquivo,checador1,checador2,chave1,chave2,dado):
                            print("Dados excluidos com sucesso")
                        else:
                            print("Aluno ou curso não cadastrado ou lista vazia")
                    else:
                       print("Arquivo não encontrado") 
                else:
                    print("Insira um dado válido")
            else:
                print("Opção inválida")
        elif opcao==4:
            informacao="relatórios"
            nome_arquivo="relatorios.txt"
            checador1="alunos.txt"
            checador2="cursos.txt"
            checador3="matriculas.txt"
            escolha=submenu(informacao)
            if escolha==0:
                opcao=10*99
            elif escolha==1:
                if existe_arquivo(nome_arquivo):
                    chave1=input("Digite o código do curso:")
                    if relatorio_curso(nome_arquivo,checador1,checador3,chave1):
                        print("Relatóro gerado com sucesso")
                    else:
                        print(f"Nenhum curso encontrado com o código:{chave1}")
                else:
                    print("Arquivo não encontrado")

            elif escolha==2:
                if existe_arquivo(nome_arquivo):
                    data_i=input("Digite a data de inicio do curso:")
                    data_f=input("Digite a data de termino do curso:")
                    if relatorio_data(nome_arquivo,data_i,data_f,checador2,checador3):
                        print("Relatóro gerado com sucesso")
                    else:
                        print(f"Nenhum curso encontrado entre as datas {data_i} {data_f}")
                else:
                    print("Arquivo não encontrado")
            elif escolha==3:
                if existe_arquivo(nome_arquivo):
                    chave1=input("Digite o CPF do aluno:")
                    if relatorio_aluno(nome_arquivo,chave1,checador2,checador3):
                        print("Relatóro gerado com sucesso")
                    else:
                        print(f"Nenhum aluno matriculado com o CPF:{chave1}")
                else:
                    print("Arquivo não encontrado")
            else:
                print("Opção não válida")
        else:
            print("Opção não válida")

main()