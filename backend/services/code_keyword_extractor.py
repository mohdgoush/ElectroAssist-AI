def extract_code_keywords(
    code: str
):

    keywords = []

    mappings = {
        "analogRead": "ADC ATmega328P",
        "analogWrite": "PWM ATmega328P",
        "digitalWrite": "GPIO ATmega328P",
        "pinMode": "GPIO ATmega328P",
        "LM358": "LM358 Datasheet",
        "LM741": "LM741 Datasheet",
        "NE555": "NE555 Datasheet",
        "ATmega328P": "ATmega328P",
        "ESP32": "ESP32"
    }

    for key, value in mappings.items():

        if key.lower() in code.lower():

            keywords.append(
                value
            )

    return " ".join(
        keywords
    )