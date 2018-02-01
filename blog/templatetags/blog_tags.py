from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    """
    Register own template filter.
    :param dictionary: expected dict object
    :param key: expected unmutable type, key for dict
    :return: key from dict or None
    """
    return dictionary.get(key)
