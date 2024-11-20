USER_POST_FORMAT = "<h1>{headline}</h1><h3>Posted by {poster_name}</h3><div>{text}</div><div>{tags_html}</div>"

def compose_post_html(poster_name: str, headline: str, text: str, hashtags: list):
    tags_html = " ".join([f"<span>{tag}</span>" for tag in hashtags])
    return USER_POST_FORMAT.format(poster_name=poster_name, headline=headline, text=text, tags_html=tags_html)