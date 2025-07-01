from django.shortcuts import render, redirect 
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        #https://marketstack.com/search

        #We can serach the tikcer symbol to serach a perticular stock from the above URL

        #ticker is the variable which is storing the name of the stock which is being serached in the search bar

        #https://marketstack.com/dashboard
        #Above is the URL to the website from where we have taken the token for our API

        #Access_Key = f8ca281380745c84e43f07d5152ae705

        #http://api.marketstack.com/v2/eod?access_key=f8ca281380745c84e43f07d5152ae705&symbols=AAPL


        api_request = requests.get("http://api.marketstack.com/v2/eod?access_key=f8ca281380745c84e43f07d5152ae705&symbols="+ticker)
        
        try:
            api = json.loads(api_request.content)  #Here we're parsing the response from the API
        except Exception as e:
            api = "An Error..."  

        return render(request, 'home.html', {'api':api})    
    else:
        return render(request, 'home.html', {'ticker':"Enter a ticker symbol.."})    

      

    


def about(request):
    return render(request, 'about.html', {})   


def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None) #Just putting the input from the user in the form variable
        #Using the StockForm from the "forms.py"

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added successfully"))
            return redirect('add_stock')

    else:
        ticker = Stock.objects.all() #Retriving the data from the DB
        output = []

        for ticker_item in ticker:
            api_request = requests.get("http://api.marketstack.com/v2/eod?access_key=f8ca281380745c84e43f07d5152ae705&symbols="+str(ticker_item))

            try:
                api = json.loads(api_request.content)  #Here we're parsing the response from the API
                output.append(api)  #Appending the api value in the output list

            except Exception as e:
                api = "An Error..."  


        
        return render(request, 'add_stock.html', {'ticker':ticker, 'output':output}) 


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id) #Fetching the data from the DB from it's ID

    item.delete() #Deleting the given item
    messages.success(request, ("Stock has been deleted!"))
    return redirect('add_stock')


        
       

