import asyncio
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.messages import HumanMessage

load_dotenv()
st.set_page_config(page_title="AI Wedding Planner", page_icon="💍", layout="centered")

st.title("💍 Autonomous Wedding Planner")
st.caption("Orchestrated via Local Ollama + LangGraph State + MCP")

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-end; margin: 10px 0;">
                <div style="background: #392b47; color: white; padding: 10px 15px; border-radius: 14px 14px 2px 14px; max-width: 75%;">
                    {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        with st.chat_message("assistant", avatar="💒"):
            st.markdown(msg["content"])

if prompt := st.chat_input("e.g. I am in London, planning a wedding in Rome for 80 guests, acoustic genre"):
    st.session_state.history.append({"role": "user", "content": prompt})
    st.rerun()