import re
import json
from pathlib import Path

# Load FAQ dataset
BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "sample_faq.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

# FAQ keyword patterns
faq_patterns = {
    0: r'\b(hours?|operation|timings?|open|close)\b',
    1: r'\b(submit|submission|internship|project|github|repository)\b',
    2: r'\b(certificate|certificates|receive|issued)\b'
}

# Normalize user input
def normalize_input(user_input):
    user_input = user_input.lower().strip()
    user_input = re.sub(r'[^\w\s]', '', user_input)
    return user_input

# Check greetings
def is_greeting(user_input):
    message = normalize_input(user_input)

    for greeting in faq_data["greetings"]:
        pattern = r'\b' + re.escape(greeting) + r'\b'

        if re.search(pattern, message):
            return True

    return False

# Recognize multiple intents
def recognize_intents(user_input):
    message = normalize_input(user_input)
    matched_faqs = []

    for index, pattern in faq_patterns.items():
        if re.search(pattern, message):
            matched_faqs.append(index)

    return matched_faqs

# Generate chatbot responses
def get_response(user_input):
    responses = []

    if is_greeting(user_input):
        responses.append(
            "Hello! Welcome to Student Support Assistant. How can I help you?"
        )

    matched_faqs = recognize_intents(user_input)

    for index in matched_faqs:
        answer = faq_data["faqs"][index]["answer"]
        responses.append(answer)

    if not responses:
        return (
            "Sorry, I didn't understand your question. "
            "Please ask about business hours, internship submission, "
            "or certificates."
        )

    return "\n\n".join(responses)