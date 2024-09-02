import smtplib, random, string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# wqft fwwq plor lspj

def send_email(to_email, subject, message):
    # Informações do servidor SMTP do Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "fulleducaprojeto@gmail.com"
    # from_password = "wqft fwwq plor lspj"
    from_password = "qyki olmw kncx qsfv"

    # Criar a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))

    try:
        # Conectar ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)

        # Enviar o e-mail
        server.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
    finally:
        server.quit()

# Exemplo de uso
to_email = "saborcomilao@gmail.com"
random_password =  "".join(random.sample(list(string.ascii_lowercase + string.ascii_uppercase + string.digits), 20))
subject = "BEM-VINDO AO FULLTIME EDUCA!"
message = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro Concluído</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            text-align: center; /* Centraliza o conteúdo dentro do contêiner */
        }
        h4 {
            color: #333;
        }
        .success {
            color: #28a745;
            font-weight: bold;
        }
        .details {
            margin-top: 20px;
            line-height: 1.6;
        }
        .details strong {
            color: #333;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #777;
            text-align: center;
        }
        .logo {
            max-width: 200px; /* Redimensiona a largura máxima da imagem */
            margin-bottom: 20px; /* Espaçamento inferior */
        }
    </style>
</head>""" 
message += f"""
<body>
    <div class="container">
        <img src="https://fulltime.com.br/wp-content/themes/fulltime-brasil-1/images/logo.png" alt="Logo Fulltime" class="logo">
        <h4 class="success">CADASTRO FEITO COM SUCESSO</h4>
        <p class="details">
            Olá, Seu cadastro foi realizado com sucesso! Aqui estão seus dados de login:
        </p>
        <p class="details">
            Usuário: <strong>{to_email}</strong> <br>
            Senha: <strong>{random_password}</strong>
        </p>
        <p class="footer">
            Se você não realizou este cadastro, por favor, ignore este e-mail.
        </p>
    </div>
</body>
</html>
"""

send_email(to_email, subject, message)


# from app.usecases.teachers_usecase import TeachersUseCase
# from infrastructure.database.mysql.repository.teachers_respository import TeacherRepository
# from infrastructure.database.mysql.repository.users_repository import UsersRepository

# r = TeachersUseCase(
#     users_repository=UsersRepository(),
#     teachers_repository=TeacherRepository()
# ).create_new_teacher(1)

# print(r.content)