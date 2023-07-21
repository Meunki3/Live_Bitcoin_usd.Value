import customtkinter as ctr
import requests
import os
from bs4 import BeautifulSoup

ctr.set_appearance_mode("dark")
ctr.set_default_color_theme("blue")

root = ctr.CTk()
root.geometry("500x450")
root.title("Live Bitcoin Value")
root.resizable(False,False)


# root.resizable(False,False)


headers = {
        'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
        }
params = {
        "q": "fus ro dah defenition",
        "gl": "us",
        "hl": "en"
        }

URL = "https://www.google.com/finance/quote/BTC-USD"
r = requests.get(URL, headers=headers, params=params)
soup = BeautifulSoup(r.text, "html.parser")
btcPriceCurrent = soup.find('div', class_="YMlKec fxKbKc").text



frame = ctr.CTkFrame(root, width=675, height=450,)
frame.pack(padx=50, pady=50)



livePrice = ctr.CTkLabel(master=frame,text="btcPriceCurrent", text_color="whitesmoke", font=('',25))
livePrice.pack(padx=10, pady=10)

textDescript = '''
Bitcoin Value   

This is a live update of Bitcoin value. 

The Price will auto change when the value 

changes. Data is pulled from Google 

Made With Python
'''
corName = ctr.CTkLabel(master=frame, text=textDescript, font=('',15))
corName.pack(padx=10, pady=10) 


def updateText():
       global btcPriceCurrent
       global soup
       global r
       global params
       global headers
       global URL
       r = requests.get(URL, headers=headers, params=params)
       soup = BeautifulSoup(r.text, "html.parser")
       btcPriceCurrent = soup.find('div', class_="YMlKec fxKbKc").text
       # arrayText = ["bob", "dough", "form", "huge","Amogo"] #Test livePrice.Configure Every two seconds by picking from array
       livePrice.configure(text=btcPriceCurrent + " USD")
       livePrice.after(2000, updateText)

updateText()

root.mainloop()








