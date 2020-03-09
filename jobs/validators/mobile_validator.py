from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

def validate_mobile_number(value):
    return RegexValidator(regex=r'^09\d{9}$',
                                 message=_("Phone number must be entered in the format: '09112222222'."))(value)