import os
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project=os.getenv("PROJECT"), location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")
response = model.generate_content("日本で100番目に高い山は何ですか？")
answer = (
    response.text
    if response.candidates[0].avg_logprobs > -0.1
    else "正確な情報を提供できません。"
)
print(f"回答：{answer}")
# 回答：正確な情報を提供できません。
