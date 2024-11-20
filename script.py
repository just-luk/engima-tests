BLOG_FORMAT = "<h1>{heading}</h1><p>{content}</p>"

def display_blog_entry(heading: str, content: str):
    return BLOG_FORMAT.format(heading=heading, content=content)