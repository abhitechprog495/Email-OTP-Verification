#Import necessary modules and libraries
import os,math
import random,sys
import smtplib

#Here the mail_id stored the entered email id
mail_id=sys.argv[1]

#Here,the OTP is generated
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]

#Message which is shown in the mail
msg='Your OTP Verification for app is '+OTP+'Note - Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid!'

#The generated OTP stored in the text file
file2=open("OTP.txt","w")
file2.write(OTP)
file2.close()

#your_EmailID - Here fill your email id where you want to send OTP
#your_email_app_password - Here fill the email app password
#Note - App Password is just like a authenticator password but it is temporary.
#It is used where 2-Factor Authentication is not working.
#To send OTP on email, make sure your 2-Factor Authentication is ON.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('your_EmailID','your_email_app_password')
print(msg)
s.sendmail('your_EmailID',mail_id,msg)
os.system('python verify_screen.py')