import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from infrastructure.email.message import MESSAGE

class EmailSender:
    @staticmethod
    def send_email(name, email, password):
        # Informações do servidor SMTP do Gmail
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_email = "saborcomilao@gmail.com"
        from_password = "wqft fwwq plor lspj"

        # Criar a mensagem
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = email
        msg['Subject'] = ""

        message = MESSAGE
        message = message.replace("#nome_usuario#", name)
        message = message.replace("#seu_usuario#", email)
        message = message.replace("#sua_senha#", password)
        
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
