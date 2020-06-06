from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import UvaSolve


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dataACM = {'address': "https://bit.ly/2MqBV3W", 'head': "ACM", 'title': "ACM Solve",
                   'details': "The International Collegiate Programming Contest, known "
                              + "as the ICPC, is an annual multi-tiered competitive programming competition among the universities "
                              + "of the world.", 'button_name': "acm_button", 'value': "val_acm"}

        dataArduino = {'address': "https://bit.ly/2XUpx1E", 'head': "Arduino", 'title': "Arduino",
                       'details': "Arduino is designed to make electronics more accessible to artists, designers," +
                                  " hobbyists and ayone interested in creating interactive objects or environments.",
                       'button_name': 'arduino_button', 'value': "val_arduino"}

        dataAlgorithm = {'address': "https://bit.ly/2XrGuRP", 'head': "Algorithm", 'title': "Algorithm",
                         'details': "Mathematics and computer science, an algorithm" +
                                    " is a finite sequence of well-defined, computer-implementable instructions,"
                                    + " typically to solve a class of problems or to perform a computation.",
                         'button_name': 'algorithm_button', 'value': "val_algo"}

        lst = list()
        lst.append(dataACM)
        lst.append(dataArduino)
        lst.append(dataAlgorithm)
        context['data'] = lst
        return context

    def get(self, request, *args, **kwargs):
        # get the value of button_acm's
        q = request.GET.get("acm_button")

        if q == 'val_acm':
            # return the whole AcmView class
            return AcmView.as_view()(self.request)
        else:
            # return this class with context
            return render(request, self.template_name, self.get_context_data())


class AcmView(ListView):
    template_name = "AcmView.html"
    model = UvaSolve
    context_object_name = "uva_codes" #it defines the context name what i call in the html

