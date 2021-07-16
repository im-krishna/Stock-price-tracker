import html5lib
import time
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import smtplib
import ssl
import smtplib
from selenium import webdriver


Code = []
upper_bound = []
lower_bound = []

i = input("Rate your internet connection 2-fast 5-medium 10-slow ")
reciever_email=input("Enter your gmail: ")

no = int(input("Enter no of companies to be tracked: "))
for i in range(1,no+1):
    Code.append(input("Enter the code for company #" + str(i) + " to be tracked: "))
    upper_bound.append(float(input("Enter the upper threshold price for this company: " )))
    lower_bound.append(float(input("Enter the lower threshold price for this company: " )))



def stocks(code):

	url = "https://finance.yahoo.com/quote/" + code
	web_driver = webdriver.Chrome()
	web_driver.get(url)


	time.sleep(i)

	html = web_driver.page_source # requests wala kam

	soup = BeautifulSoup(html,'html5lib') #readable text
	price = soup.find('div',{"class" : "My(6px) Pos(r) smartphone_Mt(6px)"})
	price = price.find("span")
	price = price.text

	index = price.find(',')
	if index!=-1:
		price = price[:index] + price[index+1:] #removing the comma

	return float(price)



sender_email = "we.are.in.the.stocksgame.now@gmail.com"
password = "Stocks_123"


def check_price(prices):

    for indx in range(0, len(prices)):
            if (prices[indx]>upper_bound[indx]): #if prices are greater than certain value send mail
                send_email(indx,1)

    for indx in range(0, len(prices)):
            if (prices[indx]<lower_bound[indx]): #if prices are lower than certain value send mail
                send_email(indx,0)



def send_email(indx,x):
	message=''
	if(x==1):
		message="Hey the price of "+str(Code[indx])+" is risen above the upper threshold it's time to buy the share"
	else:
		message="Hey the price of "+str(Code[indx])+" is dropped below the lower threshold it's time to sell the share"

	print(message)
	#Create a secure ssl context
	context = ssl.create_default_context()
	try:
		server = smtplib.SMTP("smtp.gmail.com",587)
		server.ehlo()  # Can be omitted
		server.starttls(context=context)  # Secure the connection
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

	except:
		print("Invalid Credentials")



firstRow = []
firstRow.append("Time")
for i in range(0,no) :
    firstRow.append(Code[i])

file = open("PriceData.csv","w")
file.truncate()
pd.DataFrame(firstRow).T.to_csv("PriceData.csv",mode='a',header=False)

c = 1
max=100000;
while (c<max):
	row = []
	timeSpan = datetime.datetime.now()
	timeSpan = timeSpan.strftime("%H:%M:%S")

	prices = []  #current prices are appended
	for stock in Code:
		prices.append(stocks(stock))
	row.append(timeSpan)
	row.extend(prices)
	pd.DataFrame(row).T.to_csv("PriceData.csv",mode='a',header=False)
	print(row)
	c=c+1
	check_price(prices)


