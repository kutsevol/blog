from django.utils.translation import gettext_lazy as _
from model_utils import Choices


STATUS = Choices(
    (0, 'draft', _('draft')),
    (1, 'published', _('published'))
)
