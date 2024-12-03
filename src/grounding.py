import os
import vertexai
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Tool,
    grounding,
)

vertexai.init(project=os.getenv("PROJECT"), location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")
google_search = Tool.from_google_search_retrieval(grounding.GoogleSearchRetrieval())
response = model.generate_content(
    "アメリカで次に皆既日食が起こるのはいつですか？",
    # tools=[google_search],
    generation_config=GenerationConfig(
        temperature=0.0,
    ),
)
print(response.text)
# アメリカ合衆国で次に皆既日食が見られるのは、2045年8月です。  2024年4月8日には、メキシコからカナダまでアメリカ大陸を横断する皆既日食が見られますが、これは2045年までアメリカ本土で皆既日食が見られないことを意味します。
