import ollama
msgs=[
<<<<<<< HEAD
    {
    "role":"system",
    "content":"guide me like iam a beginner in fullstack and teach me from scratch."
    }
=======
     {
            "role":"system",
            "content":"Describe Indian traditions explain creatively as if i am a foreigner in 1-2 lines?"
        }
    
>>>>>>> 27d61dd9040b6006c393af38834d28d41273e532
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
<<<<<<< HEAD

    print("AI:",response["message"]["content"]) 
print("---Chat History---\n")
for msg in msgs:
    if msg["role"]=="system":
        continue 
=======
    
    print("AI:",response["message"]["content"])

print("---Chat History---\n")
for msg in msgs:
    if msg["role"]=="system":
        continue
>>>>>>> 27d61dd9040b6006c393af38834d28d41273e532
    print(msg["role"],":",msg["content"])