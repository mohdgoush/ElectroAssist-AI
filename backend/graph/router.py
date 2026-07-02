def looks_like_code(text: str):

    code_patterns = [
        ";",
        "{",
        "}",
        "#include",
        "void ",
        "int ",
        "float ",
        "digitalWrite",
        "analogRead",
        "analogWrite",
        "pinMode",
        "void setup",
        "void loop",
        "always @",
        "module ",
        "endmodule",
        "entity ",
        "architecture",
        "process("
    ]

    matches = sum(
        1
        for pattern in code_patterns
        if pattern.lower() in text.lower()
    )
    return matches >= 2


def route_question(question: str):
    q = question.lower()
    datasheet_keywords = [
        "lm358",
        "lm741",
        "ne555",
        "atmega",
        "datasheet",
        "operating voltage",
        "supply voltage",
        "pinout",
        "maximum rating",
        "electrical characteristics"
    ]

    troubleshooting_keywords = [
        "not working",
        "fault",
        "problem",
        "error",
        "not glowing",
        "not turning on",
        "burnt",
        "damaged",
        "debug",
        "troubleshoot",
        "issue"
    ]

    code_keywords = [
        "arduino code",
        "esp32 code",
        "verilog",
        "vhdl",
        "review code",
        "debug code",
        "fix syntax",
        "syntax error",
        "optimize code",
        "explain code"
    ]
    for keyword in code_keywords:
        if keyword in q:
            return "code_review"
        
    if looks_like_code(question):
        return "code_review"

    for keyword in datasheet_keywords:
        if keyword in q:
            return "datasheet"

    for keyword in troubleshooting_keywords:
        if keyword in q:
            return "troubleshooting"
    return "knowledge"