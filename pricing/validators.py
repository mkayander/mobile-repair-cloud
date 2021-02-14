from xml.etree import ElementTree

from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile


def validate_svg(file: FieldFile):
    target_tag = '{http://www.w3.org/2000/svg}svg'
    file_tag = ElementTree.fromstring(file.read()).tag
    if not file_tag == target_tag:
        raise ValidationError("The file is not an SVG")
