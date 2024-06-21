import streamlit as st
import os
from openai import OpenAI
import showPages as show
import prompt as p
import json
import time


os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

st.title("CHUGUMI FOR YOU")

if "current_page" not in st.session_state:
    current_page = st.session_state.current_page = 1

if "info" not in st.session_state:
    st.session_state.info = {}


def move_to_next_page():
    st.session_state.current_page += 1
    st.rerun()


def move_to_previous_page():
    st.session_state.current_page -= 1
    st.rerun()
    
def reset():
    st.session_state.current_page = 1
    st.session_state.info = {}
    st.rerun()


def add_info(item):
    st.session_state.info.update(item)


if st.session_state.current_page == 1:
    show.showPage1()
    if st.button("시작하기"):
        move_to_next_page()
elif st.session_state.current_page == 2:
    character = show.showPage2()
    if st.button("다음", disabled=not character):
        add_info({"character": character})
        move_to_next_page()
elif st.session_state.current_page == 3:
    values = show.showPage3()
    if st.button("다음", disabled=not values):
        add_info({"values": values})
        move_to_next_page()
elif st.session_state.current_page == 4:
    taste = show.showPage4()
    if st.button("다음", disabled=not taste):
        add_info({"taste": taste})
        move_to_next_page()
elif st.session_state.current_page == 5:

    info = st.session_state.info

    with st.spinner("AI가 당신의 분위기를 찾아주고 있어요! 잠시만 기다려주세요."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": p.system_1,
                },
                {
                    "role": "system",
                    "content": p.system_2,
                },
                {
                    "role": "system",
                    "content": p.system_3,
                },
                {
                    "role": "user",
                    "content": f"성격: {', '.join(info["character"])} \n 가치관: {', '.join(info["values"])} \n 취향: {', '.join(info["taste"])}",
                },
            ],
            model="gpt-4o",
            response_format={"type": "json_object"}
        )
    
    result = json.loads(chat_completion.choices[0].message.content)
    pretty_result = json.dumps(result, ensure_ascii=False, indent=4)
    
    st.balloons()
    st.write(pretty_result)
    st.button("처음부터", on_click=reset)
