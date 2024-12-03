import os
import vertexai
from vertexai.generative_models import (
    GenerativeModel,
    GenerationConfig,
)

vertexai.init(project=os.getenv("PROJECT"), location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")
response = model.generate_content(
    "円周率を1000桁答えてください。円周率以外は回答に含めないでください。",
    generation_config=GenerationConfig(max_output_tokens=10),
)
print("Pi:", response.text)
# Pi: 3.14159265
