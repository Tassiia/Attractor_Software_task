from django.db import models
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    category = models.ForeignKey('articles.Category', on_delete=models.RESTRICT, verbose_name=_('Category'))
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.RESTRICT, verbose_name=_('User'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='articles', verbose_name=_('Image'))

    class Meta:
        db_table = 'articles'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title
