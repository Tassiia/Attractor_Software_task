from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Article title'))
    parent = models.ForeignKey('self', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Article category')
        verbose_name_plural = _('Article categories')

    def __str__(self):
        return self.title
