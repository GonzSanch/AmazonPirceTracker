import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.es/Nintendo-Switch-Consola-color-Azul/dp/B01N5OPMJW/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=18Y3FPHVPERQQ&keywords=switch&qid=1564226798&s=gateway&sprefix=switch%2Caps%2C161&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2= BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if(converted_price < 250):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gonzalo.sanchezsilva@gmail.com', 'ndbmobtuyadnjowd')

    subject = "Price fell down"
    body = 'Check the amazon link https://www.amazon.es/Nintendo-Switch-Consola-color-Azul/dp/B01N5OPMJW/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=18Y3FPHVPERQQ&keywords=switch&qid=1564226798&s=gateway&sprefix=switch%2Caps%2C161&sr=8-3'

    msg = f"subject: {subject}\n\n{body}"
    
    server.sendmail(
        'gonzalo.sanchezsilva@gmail.com',
        'gonzalocvp@hotmail.com',
        msg)

    print('Email has been sended!')

    server.quit()

check_price()