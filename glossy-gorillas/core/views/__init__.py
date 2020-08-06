from .market import *  # noqa
from .trader import *  # noqa
from .register import *  # noqa

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "core/pages/home.html"
