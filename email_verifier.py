import smtplib

def verify_email(email):
    try:
        domain = email.split('@')[-1]
        mx_check = smtplib.SMTP(timeout=5)
        mx_check.connect("smtp." + domain)
        mx_check.quit()
        return True
    except:
        return False
