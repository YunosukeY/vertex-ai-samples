from vertexai.preview.tokenization import get_tokenizer_for_model

tokenizer = get_tokenizer_for_model("gemini-1.5-flash-002")
response = tokenizer.count_tokens("hello world")
print("Prompt Token Count:", response.total_tokens)
# Prompt Token Count: 2
