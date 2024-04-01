
import smtplib
import email.message
import pyotp

# Chave secreta para gerar o código de autenticação
chave = 'VDRMJE2MWPRNFO72ON3WMPQ73EU7HI4C'

# Gerar o código de autenticação
codigo = pyotp.TOTP(chave)
codigo_user = input('Digite o código de autenticação: ')
autenticado = codigo.verify(codigo_user)

if autenticado:
    print('Autenticação bem-sucedida!')
    email_enviador = 'seu email' 
    senha_enviador = 'sua senha'  
    assunto = 'Código de Autenticação'
    mensagem = f'Seu código de autenticação é: {codigo.now()}'

    # Configuração do servidor SMTP do Gmail
    servidor_smtp = 'smtp.gmail.com'
    porta_smtp = 587

    # Configurar a mensagem
    msg = email.message.Message()
    msg['From'] = email_enviador
    msg['To'] = email_enviador
    msg['Subject'] = assunto
    msg.set_payload(mensagem)

    # Iniciar a conexão SMTP
    try:
        s = smtplib.SMTP(servidor_smtp, porta_smtp)
        s.starttls()
        # Autenticar-se com o servidor SMTP
        s.login(email_enviador, senha_enviador)
        # Enviar o email
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar email: {e}')
    finally:
        s.quit()
else:
    print('Código de autenticação incorreto. Tente novamente.')

