import smtplib
from datetime import datetime

today = datetime.now()
today_tuple = (today.month, today.day)

my_email = "pythondas1@gmail.com"
paswrd = "ojvzgoofdayhxkvf"





#### BIRTHDAY WISHER #####
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=paswrd)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="brittanychan@ymail.com", msg="Subject:Happy Birthday\n\n Hi Sweetie, this is a python program I wrote to wish you Happy Birthday! So happy birthday from Daddy Das :)")
    
