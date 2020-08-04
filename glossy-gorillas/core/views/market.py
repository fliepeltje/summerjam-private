from django.views.generic.list import ListView
from core.models import Listing


class ListingList(ListView):
    queryset = Listing.objects.filter(item__owner=130)
