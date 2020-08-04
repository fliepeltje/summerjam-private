from django.db.models import QuerySet


class ListingQuerySet(QuerySet):
    def some_query(self):
        return self.first()
