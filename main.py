import datetime
import yfinance as yf
import time
from plyer import notification

zomato= yf.Ticker("ZOMATO.NS")
data=zomato.info
while True:
    notification.notify(
        title="Zomato update".format(datetime.date.today()),
        message="Current Price={cp} \nDayLow={dl} \nDayHigh= {dh}".format(
            cp=data["currentPrice"],
            dl=data["regularMarketDayLow"],
            dh=data["regularMarketDayHigh"]
        ),
        app_icon="icon.ico",
        timeout=10
    )
    time.sleep(60*60)