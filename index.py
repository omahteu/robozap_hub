from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import urllib
import re

news = []
dados_formatados = []
dados_preformatados = []

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)

time.sleep(2)


nova = navegador.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span')

qtd_novas_mensagens = int(nova.text)

nova.click()

time.sleep(2)

msgsAt = navegador.find_element(By.CLASS_NAME, '_3K4-L')
msgt = msgsAt.find_elements(By.TAG_NAME, 'span')

for c in msgt:
    news.append(c.text)

valueToBeRemoved = ''
 
try:
    while True:
        news.remove(valueToBeRemoved)
except ValueError:
    pass
 

def remove_dups(lista):
    # Remove os itens duplicados mantendo a ordem original.
    return list(dict.fromkeys(lista))

def isValidTime(time) :
	
	regexPattern = "(1[012]|[1-9]):"+ "[0-5][0-9]"

	compiledPattern = re.compile(regexPattern)

	if (time == None) :
		return False
	
	if re.search(compiledPattern,time):
		return True
	else :
		return False

pre_formatacao = remove_dups(news)

for item in pre_formatacao:
    if isValidTime(item) == True:
        pass
    else:
        dados_preformatados.append(item)

print('---------------------------------------------------------')
print(dados_preformatados[-qtd_novas_mensagens:])
print('------------------------------------------')

time.sleep(2)

contatos = [{
    'nome': 'matheus',
    'numero': '5585999831355'
}]

for i, msg in enumerate(dados_preformatados):
    try:
        pessoa = contatos[i]['nome']
        numero = contatos[i]['numero']
        txt = urllib.parse.quote(f"Oi {pessoa}! {dados_preformatados[-qtd_novas_mensagens:]}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={txt}"
        navegador.get(link)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10)        
    except IndexError:
        pass

#xpath_edge = '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span'
#xpath_chrome = '//*[@id="pane-side"]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span'
