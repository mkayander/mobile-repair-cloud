import xml.etree.cElementTree as et

from django.core.exceptions import ValidationError


def is_svg(filename):
    tag = None
    with open(filename, "r") as f:
        try:
            for event, el in et.iterparse(f, ('start',)):
                tag = el.tag
                break
        except et.ParseError:
            pass
    return tag == '{http://www.w3.org/2000/svg}svg'


def validate_svg(file, is_valid):
    if not is_svg(file):
        raise ValidationError("The file is not an SVG")
