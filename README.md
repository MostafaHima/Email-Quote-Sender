# Email Quote Sender

This Python script sends a random quote every Thursday to a specified recipient via email. The quote is selected from a text file called `quotes.txt`.

## Requirements

Before running the script, make sure you have the following:

1. **Python** installed on your machine (version 3.6 or higher).
2. **SMTP Credentials** (Gmail account details) stored as environment variables:
    - `MY_EMAIL`: Your email address.
    - `MY_PASSWORD`: Your email account password (or an app-specific password if two-factor authentication is enabled).
    - `TO_EMAIL`: The email address of the recipient.

3. **quotes.txt**: A text file containing quotes, one per line. The script will pick a random quote from this file to send.

## Setup

1. Clone or download this repository.
2. Create a `.env` file or set the following environment variables:
    - `MY_EMAIL`: Your Gmail address.
    - `MY_PASSWORD`: Your Gmail password or app-specific password.
    - `TO_EMAIL`: The recipient's email address.

3. Ensure the file `quotes.txt` is in the same directory as the script and contains quotes, one per line.

## How to Run

1. Run the script using the following command:

    ```bash
    python main.py
    ```

2. The script will check the current day, and if it's Thursday, it will send a random quote to the recipient via email.

## How It Works

- The script uses the `smtplib` library to send an email via Gmail's SMTP server.
- The quote is randomly selected from the `quotes.txt` file and sent as the body of the email.
- The email is sent with the subject "Quote of the Week".

## Error Handling

- If the `quotes.txt` file is not found, a `FileNotFoundError` will be raised.
- If there is an error while sending the email, an exception message will be printed.

