# Stock-Price-Tracker
A program that logs the real-time stock prices of companies and sends alerts on the right-time for trading shares.

## About
This is a price tracker of shares made for stock traders.
* It logs the stock prices on a csv file and plots them against time for the companies the user wants to track.
* It sends the user e-mail alerts when the stock prices cross the specified value for them depending on whether the user is intending to buy or sell the shares.

### StockTracker.py
* The main function that extracts real-time stock prices of the specified shares using web-scrapping from http://finance.yahoo.com/.
* It logs the prices of the various stocks specified by the user along with the time to a csv file till all the stocks have crossed their specified bounds.
* Alerts are sent through e-mail, regarding the stocks of a company, to user when it crosses the bound that was specified by the user.
* Libraries used:
    * Selenium - load the dynamic website whose content is to be used
    * BeautifulSoup - dynamically scrape the required data from the html file extracted
    * smtplib - send mail to the user
    * ssl - secure the connection to the mail host

Example of the logged values in the csv file:

<p>
  <img src="https://github.com/im-krishna/Stock-price-tracker/blob/main/Screenshot%202021-07-10%20152610.png">
</p>

### Plot.py
Plots the real-time stock prices for each of the given shares against their current time instant. This would help in visualising the market/share scenario for the user, giving the idea of the usual trend.

Example of the plots for stock price variation:

<p align="center">
  <img src="https://github.com/im-krishna/Stock-price-tracker/blob/main/Screenshot%202021-07-10%20152727.png">
</p>
