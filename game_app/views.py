from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from game_app.models import Place


@method_decorator(csrf_exempt, name='dispatch')
class IndexView(View):
    def get(self, request):
        if not request.session.get("current_place"):
            request.session["current_place"] = int(Place.objects.get(pk=1).id)
        p = Place.objects.get(pk=request.session['current_place'])
        return render(request,
                      'index.html',
                      {
                          'place': p,
                          'ways': p.outgoing_ways.all()
                      })
