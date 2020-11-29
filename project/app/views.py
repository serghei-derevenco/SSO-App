import json

import requests
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect

# Create your views here.

discord_auth_url = "https://discord.com/api/oauth2/authorize?client_id=776804572197945344&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Flogin%2Fdiscord%2Fredirect&response_type=code&scope=identify"
mail_auth_url = "https://oauth.mail.ru/login?client_id=54e80b41d20143ba8333c7ecf350d51e&response_type=code&redirect_uri=http://localhost:8000/login/mail/redirect&scope=userinfo&state=123"
bitbucket_auth_url = "https://bitbucket.org/site/oauth2/authorize?client_id=F2LAWWSxDnRwV2ed3q&response_type=code&redirect_uri=http://localhost:8000/login/bitbucket/redirect&scope=account"


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"msg": "Hello"})

def login(request):
    return render(request, 'login.html')

def discord_login(request: HttpRequest):
    return redirect(discord_auth_url)

def discord_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    user = exchange_discord_code(code)
    return JsonResponse({"user": user})

def exchange_discord_code(code: str):
    data = {
        "client_id": "776804572197945344",
        "client_secret": "2k0GdMQSOu-SSy6XqdUHoZZCk8FOh4TZ",
        'grant_type': 'authorization_code',
        "code": code,
        "redirect_uri": "http://localhost:8000/login/discord/redirect",
        "scope": "identify"
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post("https://discord.com/api/v6/oauth2/token", data=data, headers=headers)
    print(response)
    credentials = response.json()
    print(credentials)
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={'Authorization': 'Bearer %s' % access_token})
    print(response)
    user = response.json()
    print(user)
    return user


def mail_login(request: HttpRequest):
    return redirect(mail_auth_url)

def mail_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    user = exchange_mail_code(code)
    return JsonResponse({"user": user})

def exchange_mail_code(code: str):
    data = {
        "client_id": "54e80b41d20143ba8333c7ecf350d51e",
        "client_secret": "353e046df1364f4fa5d55265a5213ebb",
        'grant_type': 'authorization_code',
        "code": code,
        "redirect_uri": "http://localhost:8000/login/mail/redirect",
        "scope": "userinfo",
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post("https://oauth.mail.ru/token", data=data, headers=headers)
    print(response)
    credentials = response.json()
    print(credentials)
    access_token = credentials['access_token']
    response = requests.get("https://oauth.mail.ru/userinfo?access_token={}".format(access_token))
    print(response)
    user = response.json()
    print(user)
    return user

def bitbucket_login(request: HttpRequest):
    return redirect(bitbucket_auth_url)

def bitbucket_login_redirect(request: HttpRequest):
    code = request.GET.get('code')
    print(code)
    user = exchange_bitbucket_code(code)
    return JsonResponse({"user": user})

def exchange_bitbucket_code(code: str):
    data = {
        "client_id": "F2LAWWSxDnRwV2ed3q",
        "client_secret": "R32dJgm2P7HgttxD4J3GxJE2aTuCd39f",
        'grant_type': 'authorization_code',
        "code": code,
        "redirect_uri": "http://localhost:8000/login/bitbucket/redirect",
        "scope": "account",
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post("https://bitbucket.org/site/oauth2/access_token", data=data, headers=headers)
    print(response)
    credentials = response.json()
    print(credentials)
    access_token = credentials['access_token']
    response = requests.get("https://api.bitbucket.org/2.0/user?access_token={}".format(access_token))
    print(response)
    user = response.json()
    print(user)
    return user