import ollama
import streamlit as st
st.title("*:yellow[AI Smart Tutor😎😉]*")
st.subheader("*:blue[Always ready to explain in a simple way.😁]*")
st.subheader("*:green[Hello,Dear Friend🤗]*")
if st.button("Summarize😝"):
    st.write("In the required simplest way.")
if st.button("Everything from scratch😶"):
    st.write("Explaining from zerooo....")
if st.button("Exam Prep")
with st.sidebar:
    personalities={
        "Kid👶":"Give the answers like you are explaining to a 5 year old kid. Give the answer in 2 lines only.",
        "Professor👨‍🏫":"You are an IIT professor.Explain the topics using correct terminology.Give the answer in 2 lines only.",
        "IT Developer👨‍💻":"You are a software developer.Explain in a technological way.Give answer in 2 lines only."
    }
    personality = st.selectbox("Select a personality",personalities.keys())
    st.header("Chat Settings")
    
    if st.button("Clearchat🗑️"):
        st.session_state.messages=[]
        st.success("Chat cleared successfully.")
    uploaded_file = st.file_uploader("Upload a file...📂")
    try:
        if uploaded_file:
            st.success("File uploaded successfully.✅")
            with st.expander("Preview⬇️"):
                context=uploaded_file.read().decode("utf-8")
                st.text(context)
    except:
        st.error(":red[OOPS!!File type not supported😒]")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question=st.chat_input("Ask a question:🤔")
if question:
    with st.chat_message("user"):
        st.write("user:",question)

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )
    with st.spinner("Wait for a while please..."):
        response =ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role":"system","content":personalities[personality]
                }
            ]+st.session_state.messages
        )


        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":response["message"]["content"]
            }
        )

        with st.chat_message("assistant"):
            st.write("AI:",response["message"]["content"])
