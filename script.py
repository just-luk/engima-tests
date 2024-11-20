BLOG_FORMAT = "<h1>{headline}</h1><p>{content}</p>"

def format_blog_entry(headline: str, content: str):
    return BLOG_FORMAT.format(headline=headline, content=content)