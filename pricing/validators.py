from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError

from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile
from django.utils.translation import ugettext_lazy as _


def validate_svg(file: FieldFile):
    target_tag = '{http://www.w3.org/2000/svg}svg'

    try:
        file_tag = ElementTree.fromstring(file.read()).tag
    except ParseError:
        file_tag = None

    if not file_tag == target_tag:
        raise ValidationError(_("The file is not an SVG"))
