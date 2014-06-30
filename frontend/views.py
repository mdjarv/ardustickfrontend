from django.views.generic import TemplateView
from lightcontrol.models import Device


class IndexView(TemplateView):
    template_name = "frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['devices'] = Device.objects.all()
        return context