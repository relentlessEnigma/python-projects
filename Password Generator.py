#This is a password generator which creates a password and sends it to your personal email so you dont forget it.


#Imports
import smtplib
import getpass
from random import sample, shuffle
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Y","W","X","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","q","s","t","u","v","x","z","y","w"]
symbols = ["!","#","$","%","&","/","(",")","=","'","?","«","»","<",">",";",",",".",":","|"]
numbers = [1,2,3,4,5,6,7,8,9,0]
newPassword = []

print("Welcome to Password Generator v.1.b (BETA)")
print("Select the characters type quantity you want in your password:")
number_letters = int(input("How many letters: "))
number_symbols = int(input("How many symbols: "))
number_numbers = int(input("How many numbers: "))
user_service = input("Service/Site you need this password for: ")
user_email = input("Email or login name: ")

for x in range(number_letters):
    newPassword.append(sample(letters, 1))
for y in range(number_symbols):
    newPassword.append(sample(symbols, 1))
for z in range(number_numbers):
    newPassword.append(sample(numbers, 1))

shuffle(newPassword)
unzipedPassword = ''.join([str(*x) for x in newPassword])

print(f"Service Login: {user_service} ")
print(f"Your Email/Username: {user_email}")
print(f"Your new Password: {unzipedPassword}")

sendEmail = input("Send email with these details ? (y/n)").lower()

#Call HTML file
def getIndexHTML():
    return render_template("index.html", title="Password Generator", user_service=user_service, user_email=user_email, password=unzipedPassword)

#Send through email the data created:
def functiontoSendEmail():
    userSetPassword = input("Root Password: ")

    #Starting Email Server:
    host = "smtp.gmail.com"
    port = "587"
    user = "tasantos.esteves@gmail.com"
    password = userSetPassword

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(user, password)

    emailSendTo = input("Set the email where you want to receive this details: ")

    #Email Type :
    body = getIndexHTML()

    emailMessage = MIMEMultipart()
    emailMessage['From'] = user
    emailMessage['To'] = emailSendTo
    emailMessage['Subject'] = "My Personal Vault: New Service Credentials"
    emailMessage.attach(MIMEText(body, 'html'))

    #Send Email:
    server.sendmail(emailMessage['From'], emailMessage['To'], emailMessage.as_string())
    server.quit() #Ends the login session


if sendEmail == "y":
    functiontoSendEmail()
else:
    exit()
