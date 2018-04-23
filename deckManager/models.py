from django.db import models

class Card(models.Model):
    cmc = models.IntegerField()
    card_type = models.CharField(max_length=50)
    colors = models.CharField(max_length=50)
    cost = models.CharField(max_length=10)
    creature_type = models.CharField(max_length=250)
    losses = models.IntegerField()
    wins = models.IntegerField()
    power = models.IntegerField()
    quantity = models.IntegerField()
    title = models.TextField()
    toughness = models.IntegerField()

class Deck(models.Model):
    colors = models.CharField(max_length=100)
    revision = models.IntegerField()
    losses = models.IntegerField()
    wins = models.IntegerField()
    name = models.CharField(max_length=250)

class Deck_Cards(models.Model):
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    deck_revision_added = models.ForeignKey(Deck, on_delete=models.CASCADE)
    deck_revision_removed = models.ForeignKey(Deck, on_delete=models.CASCADE)
    wins = models.IntegerField()
    losses = models.IntegerField
    is_active = models.BooleanField()

