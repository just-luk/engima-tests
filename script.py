BLOG_FORMAT = "<h1>{headline}</h1><p>{content}</p>"

def render_article_page(headline: str, content: str):
    return BLOG_FORMAT.format(headline=headline, content=content)