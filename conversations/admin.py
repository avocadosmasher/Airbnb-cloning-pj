from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    pass
