# ------------------To sent an email---------------------
import smtplib


my_email = "alvin@gmail.com"
password = "" # generate the "App Password" in google security password

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # transport layer security, essentially securing the message if someone intercept it
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="an.vi16@yahoo.com",
                        msg="Subject: Hello \n\n This is the body of my email")


# ------------------DataTime Module------------------------
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

if year == 2024:
    print("Wear a face mask")
print(type(now))
print(day_of_week)

day_of_week = dt.datetime(year=1995, month=8, day=16)
print(day_of_week)