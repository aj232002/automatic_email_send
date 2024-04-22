import smtplib

fromaddr = '************'
toaddrs = '************'
msg = ("subject: Hello\n\n This is the body of my email")

username = '************'
# This the app password which you can set up in your email settings
password = '************'

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login(username, password)
connection.sendmail(fromaddr, toaddrs, msg)
connection.quit()