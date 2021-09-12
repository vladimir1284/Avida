from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sys
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

@login_required
def dashboard(request):
    return render(request, 'index.html')
    
    
# # Function for handling login
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated '\
#                     'successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'avida/login.html', {'form': form})

# Function for sendig messages
def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAMDnjacbrgBAKNPU6qDaj2ASFoIh4mrfu9TH2rI9Qv3WntF8Qe1Txs2c6JWZCpxgifZCi17sZCRBc9k56j3pHIbaW2eVEUuZB1GPhEAdLShBelE6MZB6cqyu41STJFf8i6sAkuKA9DGWQA6HllKZAGZCUW1LHGnZCgOwq1bo9OmQxGEdaLOTjmg' 
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    print(status.json(), file=sys.stderr)

# Class for handling Facebook requests
class AvidaBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'agua':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                
                if 'message' in message:
                    # Print the message to the terminal
                    print(message, file=sys.stderr)   
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly. 
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()
