from django.contrib.auth import login

from rest_framework.decorators import api_view
from rest_framework.response import Response
from social.apps.django_app.utils import psa

@psa('social:complete')
def ajax_auth(request, backend):
    print(request.backend)
    token = {
        'oauth_token': "123-abc",
        'oauth_token_secret': "123",
    }
    user = request.backend.do_auth(token)
    #now login the user
    return Response("OK")


