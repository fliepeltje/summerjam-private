from django.views.generic import DetailView
from django.contrib.auth.models import User
from core import models


class UserDashboard(DetailView):
    template_name = "core/dashboard.html"
    model = User

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['trader'] = models.Trader.objects.filter(user__id=self.object.id)
        context['listings'] = models.Listing.objects.filter(item__owner__user_id=self.object.id)
        context['inventory'] = models.InventoryRecord.objects.filter(owner__user_id=self.object.id)
        return self.render_to_response(context)
