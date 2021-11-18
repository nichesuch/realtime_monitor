from django.shortcuts import render

from django.views.generic import TemplateView
import plotly.graph_objects as go
import random

from django.conf import settings
from app.modules import tail as t
import time

class LineChartsView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(LineChartsView, self).get_context_data(**kwargs)
        context["range"] = settings.MONITOR_RANGE_MSEC
        context["interval"] = settings.MONITOR_INTERVAL_MSEC
        return context

class DataApi(TemplateView):
    template_name = "api.html"

    def data_api(self, request):
        if(settings.SAMPLE_DATA):
            return time.time(), random.random(),random.random(),random.random()
        else:
            seek_pointer = request.session.get('seek_pointer', None)
            data, seek_pointer = t.tail(settings.LOG_FILE_PATH, pointer=seek_pointer)
            request.session['seek_pointer'] = seek_pointer
            return data

    def get_context_data(self, **kwargs):
        context = super(DataApi, self).get_context_data(**kwargs)
        context["data"] = self.data_api(self.request)
        return context