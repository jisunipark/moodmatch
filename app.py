import streamlit as st
import os
from openai import OpenAI
import prompt as p
import json
import streamlit.components.v1 as components


example_data = """{
	"city": "코펜하겐",
	"lifestyle": {
		"fashion": [{
			"brand": "Acne Studio",
			"explanation": "심플한 디자인과 고급스러운 원단"
		}],
		"values": [{
			"idea": "Hygge",
			"explanation": "소박하고 따뜻한 일상 생활의 즐거움을 추구하는 사상"
		}],
		"items": [{
			"brand": "Hay",
			"explanation": "미니멀한 가구와 소품"
		}]
	},
	"people": [{
		"name": "Pernille Teisbaek",
		"account": "@pernilleteisbaek",
		"accountUrl": "https://www.instagram.com/pernilleteisbaek/",
		"explanation": "패션, 라이프스타일, 미니멀리즘의 아이콘"
	}]
}"""

css = """
<style>
  img {
    margin: 0 auto;
    text-align: center;
  }


  h1 {
    text-align: center;
  }
  
  h3 {
    font-size: 1.5em;
    padding: 0.5rem 0px;
    margin-top: 40px;
  }
  
  h4 {
    font-size: 1.4em;
    color: #ff4b4b;
    padding: 0.5rem 0px;
    margin-bottom: 24px;
  }
  
  h5 {
    text-align: center;
  }

  
  iframe {
    height: 142px;
    border-radius: 8px;
  }
  
  
  .st-emotion-cache-a4hnxu.e1f1d6gn0 {
    border-width: 0px;
    z-index: 1000;
    overflow: hidden;
    position: fixed;
    top: 46px;
    left: 0;
    right: 0;
    display: flex;
    width: 100%;
    height: 100px;
    background-color: white;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin: 0 auto;
    border-radius: 0;
  }
  
  .st-emotion-cache-a4hnxu.e1f1d6gn0 div {
    width: fit-content;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .block-container {
    margin-top: 46px;
    padding:0;
    width: 100vw;
  }
  
  .stProgress {
    position: fixed;
    left: 0;
    right: 0;
    top: 136px;
    width: 100vw;
    z-index: 1000;
  }
  
  .stProgress .st-at {
    background-color: #ff4b4b;
  }
  
  .st-emotion-cache-11lmpti {
    margin-top: 64px;    
    gap: 1.5rem;
  }
  
  .stButton {
    display: flex;
    justify-content: end;
  }

  .st-emotion-cache-r421ms.e1f1d6gn0 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .st-emotion-cache-r421ms.e1f1d6gn0 p {
    text-align: center;
  }


</style>

"""


system_1 = "너는 사용자로부터 받은 정보를 바탕으로 다음과 같은 작업을 하게 될 거야. 1. 사용자의 성격/가치관/특징/취향 정보를 확인한다. 2. 1번의 정보를 바탕으로 사용자의 분위기와 어울리는 도시를 찾아준다. 3. 2번의 결과로 나온 도시에 사는 사람 중 감각적인 라이프스타일을 가진 사람들의 물건, 사상, 패션들을 관찰하고 사용자를 위한 맞춤 추천을 큐레이션 해준다."

system_2 = "그리고 나서 결과로 나온 도시에 사는 사람 중 감각적인 라이프스타일을 가진 사람들의 물건, 가치관, 패션들을 관찰하고 사용자를 위한 맞춤 추천을 큐레이션 해줘야 해. 그리고 그 도시를 베이스로 한 유명한 인플루언서 다섯 명과 그들의 인스타 아이디도 함께 줘."

system_3 = f"결과는 JSON 형식에 맞춰서 줘. 데이터 구조는 다음과 같아: {example_data}. fasion, values, items 배열은 각각 3개의 요소를 가지고 있어야 하고, people 배열은 5개의 요소를 가지고 있어야 해."


st.markdown(css, unsafe_allow_html=True)

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

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


def showLogo():
    with st.container(height=100, border=None):
        st.image("logo.svg", width=250)


MULTISELECT_PLACEHOLDER = "최대 다섯 개까지 고를 수 있어요"


def showPage1():
    st.image("landing-logo.png")
    if st.button("나만의 추구미 찾으러 가기"):
        move_to_next_page()


# 성격 - character
def showPage2():
    showLogo()
    st.progress(0)
    st.subheader("당신은 어떤 사람인가요?")
    st.markdown(":gray[당신의 성격이 가장 잘 나타나는 표현을 골라주세요.]")
    character = st.multiselect(
        "",
        [
            "활발한",
            "친절한",
            "사교적인",
            "외향적인",
            "자신감 있는",
            "낙관적인",
            "긍정적인",
            "창의적인",
            "결단력 있는",
            "진취적인",
            "독립적인",
            "책임감 있는",
            "신중한",
            "침착한",
            "성실한",
            "꼼꼼한",
            "차분한",
            "공감하는",
            "이해심 많은",
            "공손한",
            "정직한",
            "유머러스한",
            "겸손한",
            "용기 있는",
            "인내심 있는",
            "호기심 많은",
            "유연한",
            "체계적인",
            "계획적인",
            "협력적인",
        ],
        default=None,
        max_selections=5,
        label_visibility="collapsed",
        placeholder=MULTISELECT_PLACEHOLDER,
    )
    return ", ".join(character)


# 가치관 - values
def showPage3():
    showLogo()
    st.progress(33)
    st.subheader("당신이 무엇을 중요하게 여기나요?")
    st.markdown(":gray[당신의 가치관이 가장 잘 나타나는 표현을 골라주세요.]")
    values = st.multiselect(
        "",
        [
            "존중하는",
            "공정한",
            "정의로운",
            "평등한",
            "책임감 있는",
            "자율적인",
            "독립적인",
            "창의적인",
            "혁신적인",
            "지속 가능한",
            "친환경적인",
            "도덕적인",
            "정직한",
            "신뢰할 수 있는",
            "투명한",
            "헌신적인",
            "배려하는",
            "자비로운",
            "용서하는",
            "관대한",
            "성실한",
            "희생적인",
            "애국적인",
            "공동체적인",
            "협력적인",
            "교육적인",
            "문화적인",
            "인도적인",
            "균형 잡힌",
            "긍정적인",
        ],
        default=None,
        max_selections=5,
        label_visibility="collapsed",
        placeholder=MULTISELECT_PLACEHOLDER,
    )
    return ", ".join(values)


# 취향 - taste
def showPage4():
    showLogo()
    st.progress(66)
    st.subheader("당신은 어떤 스타일을 좋아하나요?")
    st.markdown(":gray[당신의 취향이 가장 잘 나타나는 표현을 골라주세요.]")
    taste = st.multiselect(
        "",
        [
            "클래식한",
            "현대적인",
            "빈티지한",
            "미니멀한",
            "화려한",
            "단순한",
            "색다른",
            "전통적인",
            "고급스러운",
            "실용적인",
            "감각적인",
            "자연친화적인",
            "독특한",
            "세련된",
            "편안한",
            "모던한",
            "러스틱한",
            "도시적인",
            "시골적인",
            "인더스트리얼한",
            "아트적인",
            "컨템포러리한",
            "복고풍의",
            "스포티한",
            "에코적인",
            "엘레강스한",
            "소박한",
            "다채로운",
            "기능적인",
            "우아한",
        ],
        default=None,
        max_selections=5,
        label_visibility="collapsed",
        placeholder=MULTISELECT_PLACEHOLDER,
    )

    return ", ".join(taste)


if st.session_state.current_page == 1:
    showPage1()
elif st.session_state.current_page == 2:
    character = showPage2()
    if st.button("다 골랐어요!", disabled=not character, type="primary"):
        add_info({"character": character})
        move_to_next_page()
elif st.session_state.current_page == 3:
    values = showPage3()
    if st.button("다 골랐어요!", disabled=not values, type="primary"):
        add_info({"values": values})
        move_to_next_page()
elif st.session_state.current_page == 4:
    taste = showPage4()
    if st.button("다 골랐어요!", disabled=not taste, type="primary"):
        add_info({"taste": taste})
        move_to_next_page()
elif st.session_state.current_page == 5:
    showLogo()
    st.progress(100)
    info = st.session_state.info
    with st.spinner("당신의 분위기에 찰떡인 도시를 찾고 있어요!"):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_1,
                },
                {
                    "role": "system",
                    "content": system_2,
                },
                {
                    "role": "system",
                    "content": system_3,
                },
                {
                    "role": "user",
                    "content": f"성격: {', '.join(info['character'])} \n 가치관: {', '.join(info['values'])} \n 취향: {', '.join(info['taste'])}",
                },
            ],
            model="gpt-4o",
            response_format={"type": "json_object"},
        )

    result = json.loads(chat_completion.choices[0].message.content)

    city = result["city"]
    fashion = result["lifestyle"]["fashion"]
    values = result["lifestyle"]["values"]
    items = result["lifestyle"]["items"]
    people = result["people"]

    st.balloons()
    st.markdown(
        f"<h2 style='text-algin:center;margin-top:120px'>당신은 <span style='color:#ff4b4b'>{city}</span>의 무드와 잘 어울리는군요!</h2>",
        unsafe_allow_html=True,
    )
    st.button("다시 할래요", on_click=reset)

    tab1, tab2 = st.tabs(["☀️ lifestyle", "🙎🏻 spotlight"])

    with tab1:
        st.markdown(
            f"### <span style='color:#ff4b4b'>{city}</span>의 라이프스타일을 분석해보았어요.",
            unsafe_allow_html=True,
        )

        st.markdown("#### 🛍️ 패션")
        col1, col2, col3 = st.columns(3)
        fashion_cols = [col1, col2, col3]
        for col in fashion_cols:
            index = fashion_cols.index(col)
            with col:
                st.markdown(f"##### {fashion[index]['brand']}")
                st.write(fashion[index]["explanation"])

        st.divider()

        st.markdown("#### 👀 가치관")
        col4, col5, col6 = st.columns(3)
        values_cols = [col4, col5, col6]
        for col in values_cols:
            index = values_cols.index(col)
            with col:
                st.markdown(f"##### {values[index]['idea']}")
                st.write(values[index]["explanation"])

        st.divider()

        st.markdown("#### 🔎 아이템")
        col6, col7, col8 = st.columns(3)
        items_cols = [col6, col7, col8]
        for col in items_cols:
            index = items_cols.index(col)
            with col:
                st.markdown(f"##### {items[index]['brand']}")
                st.write(items[index]["explanation"])

    with tab2:
        st.markdown(
            f"### <span style='color:#ff4b4b'>{city}</span>에 사는 감각적인 사람들을 모아봤어요.",
            unsafe_allow_html=True,
        )
        for p in people:
            with st.container():
                st.markdown(f"#### **{p['name']}**")
                st.write(p["explanation"])
                instagram_embed_code = f"""
          <blockquote class="instagram-media" data-instgrm-permalink="{p["accountUrl"]}" data-instgrm-version="12" style="border:none;" >
              <div style="padding:16px;"> <a href="{p["accountUrl"]}" target="_blank"> </a></div>
          </blockquote>
          <script async defer src="//www.instagram.com/embed.js"></script>
          """
                components.html(instagram_embed_code)
                st.divider()
