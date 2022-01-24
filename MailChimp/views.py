from urllib.parse import urlencode

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
                                      "redirect_uri": OAUTH_CALLBACK
                                  })))
