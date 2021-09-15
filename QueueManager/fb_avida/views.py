from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from .models import Client, Order, OrderStage, DiscardedOrder
import json
import sys
import requests

from .forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


@login_required
def dashboard(request):
    return render(request, 'index.html')

@login_required
def update_order(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            id = json_data['id']
            stage = json_data['stage']
        except KeyError:
            HttpResponseServerError("Malformed data!")
        order = Order.objects.get(id=id)
        try:
            order.delete()
            order = DiscardedOrder(client=order.client,
                                   stage=OrderStage.objects.filter(name=stage)[0],
                                   created=order.created,
                                   available=order.available,
                                   lts=order.lts)
            order.save()
            return JsonResponse({'result': 'ok'})
        except Client.DoesNotExist:
            return JsonResponse({'result': 'No existe ese pedido!'})


@login_required
def new_order(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            # print(json_data)
            json_data['client'] = Client.objects.get(id=json_data['client'])
            if ('stage' in json_data):
                json_data['stage'] = OrderStage.objects.filter(
                    name=json_data['stage'])[0]
            else:
                json_data['stage'] = OrderStage.objects.filter(name='queued')[
                    0]
            order = Order(**json_data)
            order.save()
            return JsonResponse({'id': order.id})
        except KeyError:
            HttpResponseServerError("Malformed data!")

@login_required
def get_orders(request):
    orders_qs = Order.objects.all().order_by("-created")
    orders = {}

    for order in orders_qs:
        orders.setdefault(order.id, {
            "id": order.id,
            "client": order.client.id,
            "stage": order.stage.name,
            "created": order.created,
            "available": order.available,
            "lts": order.lts,
        })

    return JsonResponse({'orders': orders})

@login_required
def del_client(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            id = json_data['id']
        except KeyError:
            HttpResponseServerError("Malformed data!")
        client = Client.objects.get(id=id)
        try:
            client.delete()
            return JsonResponse({'result': 'ok'})
        except Client.DoesNotExist:
            return JsonResponse({'result': 'No existe ese cliente!'})


@login_required
def new_client(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            client = Client(**json_data)
            client.save()
            return JsonResponse({'id': client.id})
        except KeyError:
            HttpResponseServerError("Malformed data!")

@login_required
def get_clients(request):
    clients_qs = Client.objects.all()
    clients = {}

    for client in clients_qs:
        clients.setdefault(client.id, {
            "id": client.id,
            "name": client.name,
            "cel": number2str(client.cel),
            "phone": number2str(client.phone),
            "address": client.address,
            "fbid": number2str(client.fbid),
        })

    return JsonResponse({'clients': clients})

# Convert number to string


def number2str(num):
    if (num is not None):
        return str(num)
    else:
        ""


# Function for sendig messages
def post_facebook_message(fbid, recevied_message):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAMDnjacbrgBAKNPU6qDaj2ASFoIh4mrfu9TH2rI9Qv3WntF8Qe1Txs2c6JWZCpxgifZCi17sZCRBc9k56j3pHIbaW2eVEUuZB1GPhEAdLShBelE6MZB6cqyu41STJFf8i6sAkuKA9DGWQA6HllKZAGZCUW1LHGnZCgOwq1bo9OmQxGEdaLOTjmg'
    response_msg = json.dumps(
        {"recipient": {"id": fbid}, "message": {"text": recevied_message}})
    status = requests.post(post_message_url, headers={
                           "Content-Type": "application/json"},
                           data=response_msg)
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
                    # Assuming the sender only sends text. 
                    # Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly.
                    post_facebook_message(
                        message['sender']['id'], message['message']['text'])
        return HttpResponse()
