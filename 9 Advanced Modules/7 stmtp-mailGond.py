import smtplib
from email.mime.multipart import MIMEMultipart  #mail yapısı
from email.mime.text import MIMEText            #mail'de ne yazacağımız
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "alperen_capar@tarsus.edu.tr"       #kimden
mesaj["To"] = "alperencapar2@gmail.com"             #kime
mesaj["Subject"] = "Smtp ile Mail Gönderme"         #başlık

yazi = """

Bu mail Smtp ile gönderilmiştir,
AE

"""

mesaj_govde = MIMEText(yazi, "plain")           #mesaj yapısına bu mesajı göndermek için MIMEText kullanılıyor
mesaj.attach(mesaj_govde)

#gmail serverlarına bağlanma
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)       #SMTP objesi oluşturdum (bağlanmak istediğim server, port)
    mail.ehlo()
    mail.starttls()
    mail.login("a******@*****.edu.tr","*******")       #mail adresi ve şifresi(gönderen) - güvenlik amaçlı mail adresi ve şifresi silinmiştir 
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("*********************************************************")
    print("Mail Başarılı Bir Şekilde Gönderildi!")
    print("*********************************************************")
    mail.close()

except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()







