from .forms.admin.login import *
from django.contrib.admin import AdminSite,ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth.models import *
from .modeladmins import *

class AdminSite(AdminSite):
    site_header = 'Inverdana'
    login_template ='admin/login.html'
    login_form = AuthForm

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['usersCount'] = User.objects.all().count()
        extra_context['treesCount'] = Tree.Tree.objects.all().count()
        extra_context['treesStockCount'] = Stock.Stock.objects.all().count()
        extra_context['eventsCount'] = Event.Event.objects.all().count()
        return super(AdminSite,self).index(request,extra_context)

admin = AdminSite(name='Inverdana')


# Register your models here.
admin.register(Contact.Contact)
admin.register(WorldBorder.WorldBorder)
admin.register(Preference.Preference)
admin.register(Tree.Tree,TreeAdmin)
admin.register(Tree.TreeSpecie)
admin.register(Tree.Share)
admin.register(Photo.Photo)
admin.register(Identifier.QRcode,QrCodeAdmin) 
admin.register(User)
admin.register(Permission)
admin.register(Group)
admin.register(Event.Event,EventAdmin)
admin.register(Tree.HasState)
admin.register(Tree.TreeState)
admin.register(Suggestions.Suggestion)
admin.register(Feed.Post)
admin.register(Stock.Stock)
