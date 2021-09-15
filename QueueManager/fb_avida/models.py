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
    created = models.DateTimeField()
    available = models.DateTimeField()
    lts = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = datetime.datetime.now()
        if self.available is None:
            self.available = datetime.datetime.now()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return (self.client.name + "(%iL)" % self.lts + " - " +
                self.created.strftime("%d/%m/%y %H:%M"))


class DiscardedOrder(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name='discarded_order')
    stage = models.ForeignKey(OrderStage,
                              on_delete=models.CASCADE,
                              related_name='discarded_order')
    created = models.DateTimeField(null=True)
    available = models.DateTimeField(null=True)
    lts = models.IntegerField()
    discarded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.client.name + "(%iL)" % self.lts + " - " +
                self.stage.name + " - " +
                self.created.strftime("%d/%m/%y %H:%M") + " - " +
                self.discarded.strftime("%d/%m/%y %H:%M"))
