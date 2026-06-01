from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

news = """
NVIDIA reported strong quarterly earnings driven by AI demand.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"""
Summarize this financial news and explain the impact to investors:

{news}
"""
)

print(response.output_text)
