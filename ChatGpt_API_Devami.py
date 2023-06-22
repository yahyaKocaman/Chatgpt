import openai

openai.api_key = "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"

messages = []
while True:
    message = input("User: ")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.Completion.create(
            engine="davinci",
            prompt=message,
            max_tokens=1024,
            temperature=0.7,
        )
        reply = chat.choices[0].text.strip()
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
