import re

def parse_text(text):
    """
    Parses text to extract structured information such as emails, phone numbers, dates, addresses, URLs, and more.
    """
    patterns = {
        "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "phone_numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
        "dates": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        "urls": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        "ip_addresses": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "addresses": r"\d{1,5}\s\w+(?:\s\w+)*,\s\w+(?:\s\w+)*,\s[A-Z]{2}\s\d{5}",  # US-style addresses
        "names": r"\b[A-Z][a-z]+\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b"  # Capitalized first and last names
    }

    parsed_data = {key: re.findall(pattern, text) for key, pattern in patterns.items()}
    parsed_data["raw_text"] = text

    return parsed_data
