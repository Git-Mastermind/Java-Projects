import openai

openai.api_key = "sk-abcdef1234567890abcdef1234567890abcdef12"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello AI!"}]
)

print(response.choices[0].message["content"])