from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CustomPasswordValidator:
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"

        """ Validate whether the password include at least one digit."""
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _("Password must contain at least %(min_length)d digit.")
                % {"min_length": self.min_length}
            )

        """ Validate whether the password is of a minimum length."""
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                _("Password must contain at least %(min_length)d letter.")
                % {"min_length": self.min_length}
            )

        """ Validate whether the password has at least one special character."""
        if not any(char in special_characters for char in password):
            raise ValidationError(
                _("Password must contain at least %(min_length)d special character.")
                % {"min_length": self.min_length}
            )

        """ Validate whether the password has at least one capital letter.  """
        if not any(char.isupper() for char in password):
            raise ValidationError(
                _("Password must contain at least %(min_length)d capital letter.")
                % {"min_length": self.min_length}
            )

    def get_help_text(self):
        return ""
