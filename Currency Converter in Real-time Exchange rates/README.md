***Currency Converter in Real Time***
In this Project, users can convert currencies using Real-time Exchange rates.It requires an active internet conectivity to run.

***Project Prerequisites***
tkinter – For User Interface (UI)
requests – To get url with the help of which we can  convert currencies using Real-time Exchange rates.

***Project File Structure***

These are the Steps to Build the Python Project on Currency Converter.

**Real-time Exchange rates**
To get real-time exchange rates, we will use: https://api.exchangerate-api.com/v4/latest/USD.
Here, we can see the data in JSON format, with the following details:
Base – USD: It means we have our base currency USD. which means to convert any currency we have to first convert it to USD then from USD, we will convert it in whichever currency we want.
Date and time: It shows the last updated date and time.
Rates: It is the exchange rate of currencies with base currency USD.

**Import required Libraries**
Import  tkinter and requests library.

**CurrencyConverter Class**
CurrencyConverter class which will get the real time exchange rate and convert the currency and return the converted amount.

Let’s create the constructor of class.requests.get(url) load the page in our python program and then .json() will convert the page into the json file. We store it in a data variable.
Convert() method:This method takes following arguments:
From_currency: currency from which you want to convert.
to _currency: currency in which you want to convert.
Amount: how much amount you want to convert.
And returns the converted amount.

***UI for CurrencyConverter***

To Create UI we will create a class CurrencyConverterUI.
Converter: Currency Converter object which we will use to convert currencies.
First, we set up the frame and add some info in it.
Now let’s create the entry box for the amount and options of currency in the frame. So That users can enter the amount and choose among currencies.
Now Let’s add the CONVERT button which will call the perform function.
Command = self.perform – It means on click it will call perform().

***Main Function***
First, we will create the Converter. Second, Create the UI for Converter




