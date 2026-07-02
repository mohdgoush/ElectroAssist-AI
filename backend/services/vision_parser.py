import json

def parse_vision_response(response_text: str):
    try:
        return json.loads(response_text)
    except Exception:
        return {
            "components": [],
            "circuit_type": "Unknown",
            "possible_issues": []
        }