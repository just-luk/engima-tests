FORUM_POST_FORMAT = "<h2>{subject}</h2><p>{text}</p>{highlights}"

def compile_post(subject: str, text: str, highlights: list[str]):
    formatted_highlights = "<ul>" + "".join([f"<li>{highlight}</li>" for highlight in highlights]) + "</ul>"
    return FORUM_POST_FORMAT.format(subject=subject, text=text, highlights=formatted_highlights)