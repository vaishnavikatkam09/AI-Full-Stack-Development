import ollama
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"What is prompt engineering in 2 or 3 lines?" 
        }
    ]
)
print(response["message"]["content"])