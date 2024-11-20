USER_POST_FORMAT = "<h1>{heading}</h1><h3>Posted by {poster}</h3><div>{body}</div><div>{labels_html}</div>"

def create_forum_post(poster: str, heading: str, body: str, labels: list):
    labels_html = " ".join([f"<span>{label}</span>" for label in labels])
    return USER_POST_FORMAT.format(poster=poster, heading=heading, body=body, labels_html=labels_html)