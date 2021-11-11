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


def data_api():
    if(settings.SAMPLE_DATA):
        return time.time(), random.random(),random.random(),random.random()
    else:
        return t.tail(settings.LOG_FILE_PATH)
    

class DataApi(TemplateView):
    template_name = "api.html"

    def get_context_data(self, **kwargs):
        context = super(DataApi, self).get_context_data(**kwargs)
        context["time"],context["x"],context["y"],context["z"] = data_api()
        return context