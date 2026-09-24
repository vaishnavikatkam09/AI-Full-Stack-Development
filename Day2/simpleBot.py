import ollama
while True:
    question = input(input("Ask me a question: "));
    if question.lower()=="exit":
        break
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role":"user",
                "content":"what is prompt engineering in 1 line"
            },
            {
                "role":"user",
                "content":"give the answer only in 2-3 lines."
            }
        ]
    )
    print(response["message"]["content"])
