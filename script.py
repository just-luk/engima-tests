BLOG_FORMAT = "<h2>{headline}</h2><div>{text}</div>"

def display_blog_entry(headline: str, text: str):
    return BLOG_FORMAT.format(headline=headline, text=text)