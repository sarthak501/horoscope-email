import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup

def horoscope():
    url = "https://www.bhaskar.com/rashifal/1/today/"
    text = ''
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="a6b3d8fe")
    
    content_paragraphs = content.find_all("p")
    for paragraph in content_paragraphs:
        for element in paragraph:
            if element.name == 'br':
                text += '\n'
            else:
                text += element.text
        text = text.strip() + '\n'
    return text

def e():
    email = "sarthakrana501@gmail.com"
    receiver_email = "sarthakr274@gmail.com"
    subject = "Today's Horoscope"
    message = horoscope()

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach message body
    body = message
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "gzhu msuj seka iabq")
    server.sendmail(email, receiver_email, msg.as_string())
    print("Email sent successfully!")

e()
    