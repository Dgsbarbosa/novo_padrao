from gettext import ngettext
import gzip
import os
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MinimumLengthValidator(object):
    """
    Validate whether the password is of a minimum length.
    """
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "A Senha muito curta. A senha deve conter no minimo %(min_length)d caracteres.",
                    "A Senha muito curta. A senha deve conter no minimo %(min_length)d caracteres.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            'Sua senha deve conter pelo menos %(min_length)d caracteres.',
            'Sua senha deve conter pelo menos %(min_length)d caracteres.',
            self.min_length
        ) % {'min_length': self.min_length}
        
     
class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("A senha deve conter pelo menos um digito , 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "A senha deve conter pelo menos um digito , 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("A senha deve conter pelo menos uma letra maiuscula, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "A senha deve conter pelo menos uma letra maiuscula, A-Z."
        )





class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("A senha deve conter pelo menos um simbolo: " +
                  "@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "A senha deve conter pelo meno um simbolo: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )