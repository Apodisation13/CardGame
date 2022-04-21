from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.utils import set_unlocked_cards


class CustomUser(AbstractUser):
    email = models.EmailField("email", blank=False, unique=True)
    cards = models.ManyToManyField("cards.Card",
                                   related_name="user_cards",
                                   through="cards.UserCard")
    leaders = models.ManyToManyField("cards.Leader",
                                     related_name="user_leaders",
                                     through="cards.UserLeader")
    decks = models.ManyToManyField("cards.Deck",
                                   related_name="user_decks",
                                   through="cards.UserDeck")
    levels = models.ManyToManyField("enemies.Level",
                                    related_name="user_levels",
                                    through="enemies.UserLevel")
    resource = models.IntegerField(default=1000, blank=False, null=False)

    def save(self, *args, **kwargs):
        # если юзер создаётся первый раз, то self.if=None, то открываем ему все карты
        if not self.id:
            super(CustomUser, self).save(*args, **kwargs)
            set_unlocked_cards(self)
            return

        super(CustomUser, self).save(*args, **kwargs)
