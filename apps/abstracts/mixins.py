from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.template import (
    loader,
    backends,
)
from django.http import HttpResponse


class HttpResponseMixin:
    """Mixins for handling HTTP response rendering."""

    CONTENT_TYPE = 'text/html'

    def get_http_response(
        self,
        request: WSGIRequest,
        template_name: str,
        context: dict = {}
    ) -> HttpResponse:
        """ Get HTTP response."""

        template: backends.django.Template =\
            loader.get_template(
                template_name
            )
        return HttpResponse(
            template.render(
                context,
                request
            ),
            content_type=self.CONTENT_TYPE
        )

        