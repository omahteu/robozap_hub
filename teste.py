from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import urllib
import re

navegador = webdriver.Chrome()

contatos = [{
    'nome': 'matheus',
    'numero': '5585999831355'
}]

mensagem = ['oi', 'túdo bem']


for i, msg in enumerate(mensagem):
    try:
        pessoa = contatos[i]['nome']
        numero = contatos[i]['numero']
        txt = f"Oi {pessoa}! {mensagem}"
        link = f"https://web.whatsapp.com/send?phone={numero}&text={txt}"
        navegador.get(link)
    except IndexError:
        pass
