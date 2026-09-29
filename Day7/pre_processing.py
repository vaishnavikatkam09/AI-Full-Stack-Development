with open("Sample.txt","r") as file:
    text=file.read()
print(text)
print("No of characters:",len(text))
count=0
for ch in text:
    if ch==" ":
        count = +1
print(count)