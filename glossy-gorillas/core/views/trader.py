from django.views.generic import DetailView
from core import models


class TraderDashboard(DetailView):
    template_name = "core/dashboard.html"
    model = models.Trader

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["listings"] = (
            models.InventoryRecord.objects.filter(owner=self.object)
            .exclude(listing__status=models.ListingStatus.FINALIZED)
            .values(
                "product__name",
                "quantity",
                "quantity_type",
                "listing__silver_per_unit",
                "listing__barter_product",
                "listing__barter_qty_per_unit",
                "listing__allow_offers",
            )
        )
        context["inventory"] = models.InventoryRecord.objects.filter(
            owner=self.object
        ).values("product__name", "quantity", "quantity_type",)

        return context
