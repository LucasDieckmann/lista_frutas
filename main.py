
# frutas = lista de frutas
#fruta recebe o nome da fruta 

#While True, enquando o codigo não der break ele continua rodando 

frutas = []

while True:
    fruta = input('Digite o nome de uma fruta ou "sair" para fechar o codigo: ')

    if fruta.lower() == "sair":
        break
    if fruta.strip() == "":
        print('Tente novamente Nome inválido ')
    else:
        frutas.append(fruta)
            
print("\nFrutas cadastradas:")
for fruta in frutas:
    print(f"- {fruta}")
