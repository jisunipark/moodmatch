import streamlit as st
import os
from openai import OpenAI
import showPages as show
import prompt as p
import css
import json
import streamlit.components.v1 as components


st.markdown(css.css, unsafe_allow_html=True)

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
    if st.button("나만의 추구미 찾으러 가기"):
        move_to_next_page()
elif st.session_state.current_page == 2:
    character = show.showPage2()
    if st.button("다 골랐어요!", disabled=not character):
        add_info({"character": character})
        move_to_next_page()
elif st.session_state.current_page == 3:
    values = show.showPage3()
    if st.button("다 골랐어요!", disabled=not values):
        add_info({"values": values})
        move_to_next_page()
elif st.session_state.current_page == 4:
    taste = show.showPage4()
    if st.button("다 골랐어요!", disabled=not taste):
        add_info({"taste": taste})
        move_to_next_page()
elif st.session_state.current_page == 5:

    info = st.session_state.info

    with st.spinner("당신의 분위기에 찰떡인 도시를 찾고 있어요!"):
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
    
    city = result["city"]
    fashion = result["lifestyle"]['fashion']
    values = result["lifestyle"]['values']
    items = result["lifestyle"]['items']
    people = result["people"]
    
    st.balloons()
    st.subheader(f"당신은 {city}의 무드와 잘 어울리는군요!")
    st.button("다시 할래요", on_click=reset)
    
    tab1, tab2 = st.tabs(["lifestyle", "spotlight"])

    with tab1:
      st.subheader(f"{city}에서 감각적으로 사는 사람들의 라이프스타일을 분석해보았어요.")
      st.markdown("#### 패션")
      for f in fashion:
          with st.container(border=True):
            st.markdown(f"##### {f["brand"]}")
            st.write(f["explanation"])
      st.markdown("#### 가치관") 
      for v in values:
          with st.container(border=True):
            st.markdown(f"##### {v["idea"]}")
            st.write(v["explanation"])
      st.markdown("#### 아이템")
      for i in items:
        with st.container(border=True):
            st.markdown(f"##### {i["brand"]}")
            st.write(i["explanation"])

    with tab2:
      st.subheader(f"{city}에 사는 감각적인 사람들을 모아봤어요.")
      for p in people:
        with st.container(border=True):
          st.markdown(f"#### **{p['name']}**")
          st.write(p["explanation"])
          instagram_embed_code = f"""
          <blockquote class="instagram-media" data-instgrm-permalink="{p["accountUrl"]}" data-instgrm-version="12" style="border:none;" >
              <div style="padding:16px;"> <a href="{p["accountUrl"]}" target="_blank"> </a></div>
          </blockquote>
          <script async defer src="//www.instagram.com/embed.js"></script>
          """
          components.html(instagram_embed_code)
          
