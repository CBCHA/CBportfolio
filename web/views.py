from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SkillList, MapBadge, MailBox, BucketList, FactItem, PfItem
from .forms import MailBoxForm
#from django.views import View
import simplejson as json

# Create your views here.
def index(request):
    skillLists = SkillList.objects.all()
    mapBadges = MapBadge.objects.all()
    mailBoxes = MailBox.objects.all()
    bucketLists = BucketList.objects.all()
    factItems = FactItem.objects.all()
    pfItems = PfItem.objects.all() 

    context = { 'mapBadges':mapBadges,
                'skillLists':skillLists,
                'mailBoxes':mailBoxes,
                'bucketLists':bucketLists,
                'factItems':factItems,
                'pfItems':pfItems,
               
    }    

    return render(request, 'web/base.html', context)

def ajax(request):

    if request.method == "POST":
        form = MailBoxForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            val = True
        else: val = False

    else:
        form = MailBoxForm()
        val = False

    context = {
        'postVal': val,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")