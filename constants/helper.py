def create_link(url):
    """
    Creates an HTML anchor tag <a> given the text and URL.

    :param text: The text to display for the link.
    :param url: The URL to link to.
    :return: A string containing the HTML <a> tag.
    """
    return f'<a href="{url}" color="blue"><u>{url}</u></a>'


def create_link_text(url, text):
    """
    Creates an HTML anchor tag <a> given the text and URL.

    :param text: The text to display for the link.
    :param url: The URL to link to.
    :return: A string containing the HTML <a> tag.
    """
    return f'<a href="{url}" color="blue"><u>{text}</u></a>'
