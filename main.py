import datetime as dt
import smtplib as sm
import random
import os

# Load email credentials from environment variables
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

# Read the quotes from the file
try:
    with open("quotes.txt", "r") as data_file:
        quotes = data_file.readlines()
except FileNotFoundError:
    raise FileNotFoundError("The file 'quotes.txt' was not found.")

# Get the current day of the week
this_week = dt.datetime.now().weekday()

# If today is Thursday (day 3 of the week)
if this_week == 3:
    # Choose a random quote
    quote = random.choice(quotes)

    # Print confirmation to console
    print("Sending quote...")

    # Send the email
    try:
        with sm.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            message = f"Subject: Quote of the Week \n\n{quote}"
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=message)
        print("Quote sent successfully!")
    except sm.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")



