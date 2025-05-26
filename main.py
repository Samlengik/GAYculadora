import random

print("===Bem vindo à GAYculadora===/Bora calcular o quão colorido você é.")
nome = input("Qual  seu nome? ")
nome = nome.strip()

if nome == "":
    nome: sem_nome

print()
print(f"Beleza {nome}, bora calcular seus níveis de açúcar...")
print()
print("Analisando seu olhar.../*Não tape a câmera!")
print()

numero_aleatorio = random.randint(1, 10)

if numero_aleatorio == 1:
    resultado = "0% gay"
    descricao = "É hétero (que pena), tem que se esforçar mais..."

elif numero_aleatorio == 2:
    resultado = "10% gay"
    descricao = "super hétero, só gosta de amizades e coisas relacionadas ao gènero né?"

elif numero_aleatorio == 3:
    resultado = "20% gay"
    descricao = "Um pouco suspeito... tô de olho ein."

elif numero_aleatorio == 3:
    resultado = "30% gay"
    descricao = "tá com aquela ''curiosidade'' né?"

elif numero_aleatorio == 4:
    resultado = "40% gay"
    descricao = "talvez seja bi...?"

elif numero_aleatorio == 5:
    resultado = "50% gay"
    descricao = "Bi ou pan... não importa. O que impoirta é que mamãe ensinou a não ter frescura com nada."

elif numero_aleatorio == 6:
    resultado = "60% gay"
    descricao = "Bi com preferências né?"

elif numero_aleatorio == 7:
    resultado = "70% gay"
    descricao = "uma pessoa do vale que é sempre confundida com hétero."

elif numero_aleatorio == 8:
    resultado = "80% gay"
    descricao = "sai desse armário porque já ta muito óbvio."

elif numero_aleatorio == 9:
    resultado = "90% gay"
    descricao = "mais um pouco e você domina o vale."

elif numero_aleatorio == 10:
    resultado = "100% gay"
    descricao = "Mais gay que isso impossível, tu é o arco-íris todo mana!"

print("Resultado calculado:")
print()
print(f"nome: {nome}")
print(f"Nível de arco-íris> {numero_aleatorio}/10")
print(f"{resultado}")
print(f"{descricao}")
print()

print("Medidor de açúcar:")

for i in range(1, 11):
    if i <= numero_aleatorio:
        print("🏳️‍🌈", end="")
else:
            print("🤍", end="")
print()
if numero_aleatorio <=3:
    print("Resulado: Você ainda tem um longo caminho pela frente, eu acredito em você. se esforce mais.")
elif numero_aleatorio <= 6:
    print("você tá quase lá, continue assim mana.")
else:
    print("cadê a coroa dessa rainha do vale?")

print()
resposta = input("Quer calcular outro nome? (s/n): ")
if resposta.lower() == "s" or resposta.lower() == "sim":
    print("Reinicie o programa para calcular novamente.")
else:
    print("Ok. Obrigada por usar a GAYculadora! :)")

input("Pressine Enter para encerrar...")