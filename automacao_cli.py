import os

#os.getcwd() - mostrar a pasta atual
#os.listdir() - lista arquivos e pasta
#os.mkdir("pasta") - cria uma pasta
#os.remove('pasta") - remove uma pasta
#shutil.move("origem", "destino") -  move uma pasta da origem ao destino
#os.system("comando") - executa um comando


print("criador de pastas")
pasta = input("digite o nome da pasta que deseja criar: ")
os.mkdir(f"automacao/teste_cli/{pasta}")