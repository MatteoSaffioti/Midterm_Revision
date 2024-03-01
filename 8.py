def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):
        # Check if there is at least one dot (.) after "http://" or "https://"
        if "." in url[url.index("//")+2:]:
            return True
    return False