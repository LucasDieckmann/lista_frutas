
#Uso do laço while
#Condicionais com if e else
#Armazenamento de dados em lista
#Validação de entrada (não aceitar strings vazias)
#Encerramento do loop com uma palavra-chave

#if else 
#if == 'sair' ele fecha o codigo 
#if fruta == '' ele fala q é inválido 
#Caso ele não caia em nenhuma das condições, adiciona a fruta para a lista.     
#lower CASO ESTEJA EM MAIÚSCULO .lower coloca em minúsculo. 
#append adiciona na lista 
#strip remove espaços em branco do início e do fim de uma string
#for  Para cada item na lista 'frutas', ele mostra um item da lista 


import tkinter as tk

def adicionar_fruta():
    fruta = entry.get()  #get pegar 
    if fruta.lower() == "sair":
        janela.quit()  #break 
    if fruta.strip() == "":#retira todos os espaços 
        mensagem.config(text="Nome inválido! Tente novamente.", fg="red") #fg da a cor vermelha 
    else:
        frutas.append(fruta)
        lista_frutas.config(text="\n".join(frutas))  
        entry.delete(0, tk.END)   #limpa o entry 
        
        
janela = tk.Tk()
janela.title("Cadastro de Itens em uma Lista")
frutas = []


janela.geometry("600x400")
janela.config(background="gray")

label = tk.Label(janela, text="Bom dia!", font=("Arial", 16), background="gray")
label.pack(pady=10)

label_instrucao = tk.Label(janela, text="Digite o nome de uma fruta ou 'sair' para fechar", font=("Arial", 12), background="gray")
label_instrucao.pack(pady=6)

entry = tk.Entry(janela, font=("Arial", 14), width=30)
entry.pack(pady=6)

botao_adicionar = tk.Button(janela, text="Adicionar Fruta", font=("Arial", 12), command=adicionar_fruta)
botao_adicionar.pack(pady=10)

lista_frutas = tk.Label(janela, text="", font=("Arial", 12), background="gray")
lista_frutas.pack(pady=10)

mensagem = tk.Label(janela, text="", font=("Arial", 12), background="gray")
mensagem.pack(pady=6)

janela.mainloop()
