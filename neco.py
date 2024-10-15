from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="https://8fd9-91-232-214-241.ngrok-free.app/v1", api_key="lm-studio")

print("Napis co chces ai: ")

role = input()

print("Napis ai: ")

while(1):
  completion = client.chat.completions.create(
    model="model-identifier",
    messages=[
      {"role": "system", "content": role},
      {"role": "user", "content": input()}
    ],
    temperature=0.7,
  )

  print(completion.choices[0].message)