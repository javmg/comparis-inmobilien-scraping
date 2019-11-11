import json
from urllib.parse import quote


class DoubleQuotedDictionary(dict):
    def __str__(self):
        return json.dumps(self)

    def __repr__(self):
        return json.dumps(self)


def encode_request_object(request_object):
    request_object_as_string = str(DoubleQuotedDictionary(request_object))

    return quote(request_object_as_string)


def filter_in_string(value, function):
    return ''.join(c for c in value if function(c))


def filter_digits_in_string(value):
    return filter_in_string(value, lambda x: x.isdigit())
