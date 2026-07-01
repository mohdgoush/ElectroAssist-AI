import google.generativeai as genai
from PIL import Image

from backend.core.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def analyze_circuit_image(
    image_path: str
):

    image = Image.open(
        image_path
    )

    prompt = """
You are an Electronics Engineer.

Analyze the image and return ONLY valid JSON.

Format:

{
  "components": [
    "component1",
    "component2"
  ],
  "circuit_type": "circuit name",
  "possible_issues": [
    "issue1",
    "issue2"
  ]
}

Rules:
- Return JSON only.
- No markdown.
- No explanations.
- No extra text.
"""

    response = model.generate_content(
        [prompt, image]
    )

    return response.text