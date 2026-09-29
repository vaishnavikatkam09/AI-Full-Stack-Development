import ollama
msgs=[
    {
    "role":"system",
    "content":"guide me like iam a beginner in fullstack and teach me from scratch."
    }
]
while True:
    question=input("Ask a question?")
    if question.lower()=="exit":
        break
    
    msgs.append(
        {
            "role":"user",
            "content":question
        }
    )
    response =ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )

    msgs.append(
        {
            "role":"assistant",
            "content":response["message"]["content"]
        }
    )

    print("AI:",response["message"]["content"]) 
print("---Chat History---\n")
for msg in msgs:
    if msg["role"]=="system":
        continue 
    print(msg["role"],":",msg["content"])