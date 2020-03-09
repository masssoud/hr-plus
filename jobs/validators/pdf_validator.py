import magic

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_pdf(data):
    content_type = magic.from_buffer(data.read(), mime=True)
    data.seek(0)

    if content_type != 'application/pdf':
        raise ValidationError(_("The file is not a valid PDF file."),
                              code='invalid_pdf_file')