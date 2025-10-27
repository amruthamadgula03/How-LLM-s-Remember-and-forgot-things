import streamlit as st

st.title("🧠 How LLMs Remember and Forget Things")
st.subheader("The concept of context windows explained interactively")

st.markdown("""
When you chat with a Large Language Model (LLM), it doesn't *truly* remember past messages.  
It only keeps track of a **limited number of tokens** — called the **context window**.
""")

context_limit = st.slider("🪄 Set Context Window Size (in tokens)", 3, 10, 5)
st.write(f"💬 The model can remember only the last {context_limit} messages.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💭 Enter a message to the AI:")

if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(user_input)

        # Simulate forgetting: keep only last N messages
        st.session_state.chat_history = st.session_state.chat_history[-context_limit:]

st.markdown("### 🧾 Model's Current Memory")
if st.session_state.chat_history:
    for i, msg in enumerate(st.session_state.chat_history, 1):
        st.write(f"{i}. {msg}")
else:
    st.info("Start typing above to build the context.")

st.markdown("""
---
🧠 **Explanation:**
- The slider above simulates the **context window size**.
- Once you exceed that limit, the oldest messages vanish.
- That’s how an LLM *forgets* older parts of a conversation when the window is full.
""")
