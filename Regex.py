import re

def my_data(text):
    m_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    m_url = r"https?://[^\s]+"
    m_phone = r"(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}"
    m_credit_card = r"\b(?:\d{4}[-\s]?){3}\d{4}\b"

    emails = re.findall(m_email, text)
    urls = re.findall(m_url, text)
    phones = re.findall(m_phone, text)
    credit_cards = re.findall(m_credit_card, text)

    return {
        "emails": emails,
        "urls": urls,
        "phones": phones,
        "credit_cards": credit_cards
    }

my_text = """
Contact us at info@alustudent.com or visit https://www.lydivine.com. 
Call (123) 798-2226 or 321-654-0987. 
Credit card: 1234 5678 9012 3456
"""

results = my_data(my_text)

for data_type, matches in results.items():
    print(f"{data_type.title()}:")
    for match in matches:
        print(f" - {match}")