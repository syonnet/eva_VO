import smtplib
from email.mime.text import MIMEText

# Configuración del servidor SMTP
smtp_server = 'smtp.gmail.com' 
smtp_port = 587
smtp_user = 'syonnet2@gmail.com'
smtp_password = 'jysl zcfj bykp npvg'

# Contenido del email
email_from = smtp_user
email_to = ['destinatario1@yopmail.com', 'destinatario2@yopmail.com']
email_subject = 'Correo de prueba desde Jenkins'
email_body = 'Este es un correo de prueba enviado desde un script Python en Jenkins'

# Crear mensaje MIME
mimemsg = MIMEText(email_body)
mimemsg['From'] = email_from
mimemsg['To'] = ', '.join(email_to)
mimemsg['Subject'] = email_subject

# Enviar correo
connection = smtplib.SMTP(smtp_server, smtp_port)
connection.ehlo()
connection.starttls()
connection.ehlo()
connection.login(smtp_user, smtp_password)
connection.sendmail(email_from, email_to, mimemsg.as_string())
connection.quit()

print('¡Correo enviado!')