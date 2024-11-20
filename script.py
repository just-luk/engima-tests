BLOG_FORMAT = "<h1>{heading}</h1><p>{description}</p>"

def display_blog(heading: str, description: str):
    return BLOG_FORMAT.format(heading=heading, description=description)