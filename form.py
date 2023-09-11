from selenium import webdriver
import time
import random as rd


for i in range(1, 10):
    web = webdriver.Chrome()
    web.get('')

    time.sleep(2)

    consent = web.find_element("xpath", '/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[2]')
    consent.click()

    Navn = ["Ahmed", "Mohammed", "Georg", "Rasmus", "Emil", "Nicoline", "Monique", "Frida", "Trym Ketil", "Ahre Ketil", "Lillehagen", "Tommy Running", "Stein Hard"]
    FulltNavn = rd.choice(Navn)
    navn2 = web.find_element("xpath", '/html/body/div[2]/div/div/div/div/div[1]/div[2]/form/div/div[1]/input') 
    navn2.send_keys(FulltNavn)

    epost = ["ahmed@gmail.com", "mohammed@gmail.com", "georg@outlook.com", "rasmus@hotmail.no", "emil@bing.com", "trymketil@online.no", "rastafletter@hotmail.no", "ketilhøye@gmail.com", "ahreketil@bing.com"]
    epostadresse = rd.choice(epost)
    epost2 = web.find_element("xpath", '/html/body/div[2]/div/div/div/div/div[1]/div[2]/form/div/div[2]/input')
    epost2.send_keys(epostadresse)

    submit = web.find_element("xpath", '/html/body/div[2]/div/div/div/div/div[2]/input')
    submit.click()


