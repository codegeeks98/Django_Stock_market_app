from django.shortcuts import render

def home(request):
    import requests
    import json

    #https://marketstack.com/dashboard
    #Above is the URL to the website from where we have taken the token for our API

    #Access_Key = f8ca281380745c84e43f07d5152ae705

    #http://api.marketstack.com/v2/eod?access_key=f8ca281380745c84e43f07d5152ae705&symbols=AAPL


    api_request = requests.get("http://api.marketstack.com/v2/eod?access_key=f8ca281380745c84e43f07d5152ae705&symbols=AAPL")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "An Error has occured..."    

    return render(request, 'home.html', {'api':api})


def about(request):
    return render(request, 'about.html', {})    
