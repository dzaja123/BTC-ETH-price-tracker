import tkinter as tk
import tkinter.font as TkFont
import requests
from datetime import datetime

def trackPrice():
    # definisanje vrednosti za citanje i ispisivanje u GUI-u
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR" 
    response = requests.get(url).json() 
    priceBTC = response["BTC"]["USD"] # citanje vrednosti BTC-a u americkim dolarima
    priceETH = response["ETH"]["USD"] # citanje vrednosti ETH-a u americkim dolarima
    time = datetime.now().strftime("%H:%M:%S") # formatiranje vremena
    
    # defninisanje vrednosti za popunjavanje label-a
    labelPriceBTC.config(text = "Bitcoin price: " + str(priceBTC) + " $") 
    labelPriceETH.config(text = "Ethereum price: " + str(priceETH) + " $") 
    labelTime.config(text = "Last check: " + time) 

    root.after(1000, trackBitcoin) # refresovanje citanja nakon 1 sekunde

# definisanje izgleda glavnog prozora grafickog interfejsa
root = tk.Tk()
root.geometry("700x800") # velicina prozora
root.title("BTC/ETH price tracker") # ime prozora
root.configure(background = '#7AB1FF') # boja pozadine

# definisanje PNG slike koja je na pozadini glavnog prozora
filename = tk.PhotoImage(file = "C:\\Users\\Dzaja-PC\\Desktop\\BTC.png")
background_label = tk.Label(root, image = filename)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# definisanje fontova
font1 = TkFont.Font(family = "Herculanum", size = 24, weight = "bold")
font2 = TkFont.Font(family = "Helvetica", size = 22, weight = "bold")
font3 = TkFont.Font(family = "Helvetica", size = 18, weight = "normal")

# definisanje vrednosti ispisanih na glavnom prozoru
label = tk.Label(root, text = "Live Price Tracker", font = font1)
label.pack(pady = 10)

# label za vrednosti BTC-a
labelPriceBTC = tk.Label(root, font = font2)
labelPriceBTC.pack(pady = 10)

 # label za vrednosti ETH-a
labelPriceETH = tk.Label(root, font = font2) 
labelPriceETH.pack(pady = 10)

# label za vrednosti trenutnog vremena
labelTime = tk.Label(root, font = font3) 
labelTime.pack(pady = 300)

# definisanje main funkcije
if __name__ == "__main__":

    trackPrice()
    root.mainloop()
