from django.forms.utils import ErrorList
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join


class CustomErrorList(ErrorList):
    def as_ul(self):
        if not self.data:
            return ''

        return format_html(
            '<ul class="form__error-list">{}</ul>',
            format_html_join('', '<li>{}</li>', ((force_text(e),) for e in self))
        )
