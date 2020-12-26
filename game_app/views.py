from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from game_app.models import Place


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request):
        if not request.session.get("current_place"):
            request.session["current_place"] = Place.objects.get(pk=1).id
        p = Place.objects.get(pk=request.session['current_place'])
        return render(request,
                      'index.html',
                      {
                          'place': p,
                          'ways': p.outgoing_ways.all()
                      })

@method_decorator(csrf_exempt, name='dispatch')
class GoView(View):
    def post(self, request, way_id):
        pl = Place.objects.get(pk=request.session.get("current_place"))
        for way in pl.outgoing_ways.all():
            if way_id == way.id:
                request.session["current_place"] = way.destination.id
        return redirect('index')


