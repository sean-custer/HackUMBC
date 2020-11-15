# Install yfinance package. 
#!pip install yfinance 
 
# Import yfinance 

import yfinance as yf   
import datetime as dt 
import matplotlib.pyplot as plt 

app = Flask(__name__)
app.route('/')


top_stocks = ["AAPL", "AMZN", "GOOG", "MSFT", "FB"]


# Get the data for the stock Apple by specifying the stock ticker, start date, and end date 
now = dt.date.today().isoformat()
print(now, "\n")
yesterday = (dt.date.today() - dt.timedelta(days=90)).isoformat()
print(yesterday, "\n")
i = 0
while(i < 5):

  data = yf.download(top_stocks[i], yesterday, now) 

  # Plot the close prices 

  ax = plt.figure()

  data.Close.plot(color="lime") 
  plt.gca().set_facecolor('black')
  plt.title(top_stocks[i])
  #plt.show()
  plt.savefig(top_stocks[i] + ".jpg")
  i += 1