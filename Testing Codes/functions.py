def get_formatted_name(first, last, middle=""):
    """ returns formatted name """
    if middle:
        name=first.title()+" "+middle.title()+" "+last.title()
    else:
        name=first.title()+" "+last.title()
    return name
