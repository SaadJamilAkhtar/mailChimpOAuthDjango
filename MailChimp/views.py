from operator import itemgetter
from urllib.parse import urlencode
import requests
from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, "index.html")


def auth(request):
    oauth_base = "https://login.mailchimp.com/oauth2/authorize?"
    creds = MailChimpCredentials.objects.first()
    return redirect("{}{}".format(oauth_base,
                                  urlencode({
                                      "response_type": "code",
                                      "client_id": creds.client_id,
                                      "redirect_uri": creds.callback
                                  })))


def callback(request):
    code = request.GET['code']
    creds = MailChimpCredentials.objects.first()
    tokenResponse = requests.post("https://login.mailchimp.com/oauth2/token",
                                  data={
                                      'grant_type': 'authorization_code',
                                      'client_id': creds.client_id,
                                      'client_secret': creds.client_secret,
                                      'redirect_uri': creds.callback,
                                      'code': code
                                  })
    access_token = itemgetter('access_token')(tokenResponse.json())
    metadataResponse = requests.get(
        'https://login.mailchimp.com/oauth2/metadata',
        headers={'Authorization': "OAuth {}".format(access_token)})
    dc = itemgetter('dc')(metadataResponse.json())
    user = User.objects.get(username=request.user.username)
    token = MailChimpToken.objects.create(user=user, token=access_token, server=dc)
    data = {
        "token": token.token,
        "server": token.server
    }
    return render(request, 'auth.html', data)
