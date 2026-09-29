import ollama
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"Think you are a 5 year old child Give the answers in 2 lines only."
        },
        {
            "role":"user",
            "content":"What is AI?" 
        }
    ]
)
print(response["message"]["content"])