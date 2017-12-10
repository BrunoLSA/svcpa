from django.db import models


class KindQuerySet(models.QuerySet):
    def money(self):
        return self.filter(kind=self.model.MONEY)
