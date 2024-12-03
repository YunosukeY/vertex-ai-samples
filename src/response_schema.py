import os
import vertexai
from vertexai.generative_models import GenerationConfig, GenerativeModel

vertexai.init(project=os.getenv("PROJECT"), location="us-central1")

response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "recipe_name": {
                "type": "string",
            },
        },
        "required": ["recipe_name"],
    },
}
model = GenerativeModel("gemini-1.5-pro-002")
response = model.generate_content(
    "List a few popular cookie recipes",
    generation_config=GenerationConfig(
        response_mime_type="application/json", response_schema=response_schema
    ),
)
print(response.text)
# [{"recipe_name": "Chocolate Chip Cookies"}, {"recipe_name": "Peanut Butter Cookies"}, {"recipe_name": "Oatmeal Raisin Cookies"}, {"recipe_name": "Sugar Cookies"}, {"recipe_name": "Snickerdoodles"}]
