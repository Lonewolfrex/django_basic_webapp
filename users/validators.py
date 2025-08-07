# users/validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import MinimumLengthValidator

class CustomMinimumLengthValidator(MinimumLengthValidator):
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Password must be at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )
