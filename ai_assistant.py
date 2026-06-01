from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

response = client.responses.create(
    model="gpt-5",
    input="Hello"
)

print(response.output_text)
