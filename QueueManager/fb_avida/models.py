from django.db import models
import datetime

    
class OrderStage(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    
class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    cel = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    fbid = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    
class Order(models.Model):
    client = models.ForeignKey(Client,
                            on_delete=models.CASCADE,
                            related_name='order')
    stage = models.ForeignKey(OrderStage,
                            on_delete=models.CASCADE,
                            related_name='order')
    created = models.DateTimeField(auto_now_add=True)
    available = models.DateTimeField()
    lts = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.available is None:
            self.available = datetime.datetime.now()
        super(Order, self).save(*args, **kwargs)
    
    def __str__(self):
        return (self.client.name + " - " + self.created.__str__())

    
class DiscardedOrder(Order):
    discarded = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.super() + " - " + self.discarded.__str__())
    
