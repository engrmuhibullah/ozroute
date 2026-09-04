import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client pointed to OmniRoute
client = OpenAI(
    base_url="http://localhost:20128/v1",
    api_key="omniroute-local-key"  # OmniRoute doesn't validate this strictly for local
)

st.set_page_config(page_title="OmniRoute Explorer", page_icon="🚀", layout="centered")

st.title("🚀 OmniRoute AI Explorer")
st.markdown("Connect to 237+ providers and save tokens with OmniRoute's auto-routing.")

# Model selection
model = st.selectbox(
    "Select Routing Strategy:",
    ["auto", "auto/coding", "auto/fast", "auto/offline"]
)

user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Response"):
    if not user_prompt:
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Routing via OmniRoute..."):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful AI assistant."},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=500
                )
                
                reply = response.choices[0].message.content
                st.success("Success!")
                st.markdown("### Response")
                st.write(reply)
                
            except Exception as e:
                st.error("Connection Error. Is OmniRoute running locally on port 20128?")
                st.exception(e)
