from src.parse import parse_text

def test_parse_text():
    text = "Email: example@example.com, Phone: (123) 456-7890, Date: 01/01/2023"
    data = parse_text(text)
    assert "emails" in data
    assert len(data["emails"]) == 1
    assert "example@example.com" in data["emails"]
    assert "phone_numbers" in data
    assert len(data["phone_numbers"]) == 1
    assert "(123) 456-7890" in data["phone_numbers"]
    assert "dates" in data
    assert len(data["dates"]) == 1
    assert "01/01/2023" in data["dates"]
