import os
import csv
os.system("cls")

arquivo_csv = "alunos.csv"

def limpar_tela():
    os.system("cls")

print ("seja bem-vindo ao sistema de notas 🤖")

while True:
    opcao = input("[1] - cadastrar aluno e nota\n" \
    "[2] - listar alunos\n" \
    "[3] - listar alunos com a nota maior de 8\n" \
    "[0] - sair\n sua opção: ")

    if opcao == "1":
        nome = input("digite o nome do aluno: ")
        idade = input("digite a idade do aluno: ")
        nota = input("digite a nota do aluno: ")
        with open("alunos.csv","a", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome, idade, nota])

    elif opcao =="2":
        with open("alunos.csv", "r") as arquivo:
            leitor =  csv.reader(arquivo)
            for linha in leitor:
                nome,idade,nota = linha
                print(f"{nome.strip():^15} | {idade.strip():^10} | {nota.strip():^10}")

    elif opcao == "3":
            with open ("alunos.csv","r") as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    nome,idade,nota = linha
                    if float(nota) > 8:
                        print(f"{nome.strip():^15} | {idade.strip():^10} | {nota.strip():^10}")
    elif opcao == "0":
        print("saindo...")
        break
    else:
        print("opção invalida.")
    input("aperte ENTER para continuar")
    limpar_tela()