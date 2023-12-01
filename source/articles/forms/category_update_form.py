from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from articles.forms import CategoryForm


class CategoryUpdateForm(CategoryForm):
    def clean_parent(self):
        parent = self.cleaned_data.get('parent')
        if self.instance == parent:
            raise ValidationError(_('Category cannot reference itself'))
        return parent
