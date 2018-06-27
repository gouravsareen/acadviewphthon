

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gauravsareen0112@gmail.com", "goruakshu71")

msg = "HEY! HOW ARE YOU"
server.sendmail("gauravsareen0112@gmail.com", "asharam@nexteonsolutions.com", msg)
server.quit()