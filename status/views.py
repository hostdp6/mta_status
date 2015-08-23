from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from status.models import Line, Favorite, LineType
from django.views.generic import View
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from bs4 import BeautifulSoup
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests

def updateLineModel():

    # download line status and write to models
    try:
        r = requests.get('http://web.mta.info/status/serviceStatus.txt')
        soup = BeautifulSoup(r.content, 'xml')
    except Exception as e:
        return False

    for line in soup.find_all('line'):
        name = line.find('name').string
        status = line.find('status').string
        text = line.find('text').string
        date = line.find('Date').string
        time = line.find('Time').string

        try:
            newline = Line.objects.get(name__exact=name)
            newline.status = status
            if isinstance(text, str):
                text = text.strip()
            if isinstance(date, str):
                date = date.strip()
            if isinstance(time, str):
                time = time.strip()
            newline.text = text
            newline.date = date
            newline.time = time
            newline.save()

        except ObjectDoesNotExist as e:

            newline = Line(
                name=name,
                status=status,
                text=text,
                date=date,
                time=time
            )
            newline.save()

    return True

class FavoriteView(View):

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(FavoriteView, self).dispatch(*args, **kwargs)

    def post(self, request):

        try:
            favorite = Favorite.objects.get(
                user__exact=request.user,
                line=Line.objects.get(pk=request.POST.get('line'))
            )
            favorite.delete()
        except ObjectDoesNotExist:
            favorite = Favorite(
                user=request.user,
                line=Line.objects.get(pk=request.POST.get('line'))
            )
            favorite.save()

        favorites = Favorite.objects.filter(user__exact=request.user)
        lines = []
        for line in favorites:
            lines.append(line.line)

       # first get the most up-to-date info and store it in the DB
        if updateLineModel():
            updated = True
        else:
            updated = False

        headercontext = RequestContext(request, {
            'title': 'Favorites',
        })
        bodycontext = Context({
            'lines': lines,
            'favorites': lines,
            'updated': updated,
            'user': request.user
        })

        header = get_template('header.html')
        body = get_template('statuslist.html')
        footer = get_template('footer.html')

        html = (
            header.render(headercontext) +
            body.render(bodycontext) +
            footer.render()
        )
        return HttpResponse(html)

    def get(self, request):

        favorites = Favorite.objects.filter(user__exact=request.user)
        lines = []
        for line in favorites:
            lines.append(line.line)

        # first get the most up-to-date info and store it in the DB
        if updateLineModel():
            updated = True
        else:
            updated = False

        headercontext = RequestContext(request, {
            'title': 'Favorites',
        })
        bodycontext = Context({
            'lines': lines,
            'favorites': lines,
            'updated': updated,
            'user': request.user
        })

        header = get_template('header.html')
        body = get_template('statuslist.html')
        footer = get_template('footer.html')

        html = (
            header.render(headercontext) +
            body.render(bodycontext) +
            footer.render()
        )
        return HttpResponse(html)

class StatusView(View):

    def get(self, request, filter=None):
        '''
        list line statuses
        '''

        # first get the most up-to-date info and store it in the DB
        if updateLineModel():
            updated = True
        else:
            updated = False

        # get the list of lines, apply filter if present
        if filter:
            typefilter = LineType.objects.get(name__exact=filter)
            lines = Line.objects.filter(type__exact=typefilter)
        else:
            lines = Line.objects.all()
        linetypes = LineType.objects.all()

        # get favorites
        favorites = []
        if request.user.is_authenticated():
            list = Favorite.objects.filter(user__exact=request.user)
            for l in list:
                favorites.append(l.line)

        headercontext = RequestContext(request, {
            'title': 'Line Status',
        })
        bodycontext = Context({
            'lines': lines,
            'linetypes': linetypes,
            'updated': updated,
            'favorites': favorites,
            'filter': filter,
            'user': request.user
        })

        header = get_template('header.html')
        body = get_template('statuslist.html')
        footer = get_template('footer.html')

        html = (
            header.render(headercontext) +
            body.render(bodycontext) +
            footer.render()
        )
        return HttpResponse(html)
