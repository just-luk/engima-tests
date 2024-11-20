BLOG_FORMAT = "<h1>{headline}</h1><p>{text}</p>"

def show_blog_post(headline: str, text: str):
    return BLOG_FORMAT.format(headline=headline, text=text)