import streamlit as st
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# 1. 성별
# 2. 성격
# 3. 가치관
# 4. 특징
# 5. 취향
st.title("추구미 가이드")

st.write("당신의 성격을 알려주세요")
personality = st.multiselect(
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
)

if personality:
    st.write("당신의 가치관을 알려주세요")
    view = st.multiselect(
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
    )

if view:
    st.write("당신의 특징을 알려주세요")
    character = st.multiselect(
        "",
        [
            "창의적인",
            "감각적인",
            "혁신적인",
            "분석적인",
            "논리적인",
            "객관적인",
            "주관적인",
            "직관적인",
            "열정적인",
            "활동적인",
            "자발적인",
            "계획적인",
            "체계적인",
            "꼼꼼한",
            "집중력 있는",
            "결단력 있는",
            "신뢰할 수 있는",
            "자립적인",
            "적극적인",
            "융통성 있는",
            "적응력 있는",
            "사교적인",
            "이해심 있는",
            "친절한",
            "유머러스한",
            "독창적인",
            "실용적인",
            "헌신적인",
            "목표 지향적인",
            "감정적인",
        ],
        default=None,
        max_selections=5,
        label_visibility="collapsed",
    )

if character:
    st.write("당신의 취향을 알려주세요")
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
    )

if personality and view and character and taste:
    disabled = False
else:
    disabled = True

done = st.button("결과 보기", disabled=disabled)

if done:
    with st.spinner("AI가 당신의 분위기를 찾아주고 있어요! 잠시만 기다려주세요."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "너는 사용자로부터 받은 정보를 바탕으로 다음과 같은 작업을 하게 될 거야. 1. 사용자의 성격/가치관/특징/취향 정보를 확인한다. 2. 1번의 정보를 바탕으로 사용자의 분위기와 어울리는 도시를 찾아준다. 3. 2번의 결과로 나온 도시에 사는 사람 중 감각적인 라이프스타일을 가진 사람들의 물건, 사상, 패션들을 관찰하고 사용자를 위한 맞춤 추천을 큐레이션 해준다.",
                },
                {
                    "role": "system",
                    "content": "그리고 나서 결과로 나온 도시에 사는 사람 중 감각적인 라이프스타일을 가진 사람들의 물건, 사상, 패션들을 관찰하고 사용자를 위한 맞춤 추천을 큐레이션 해줘야 해. 그리고 그 도시를 베이스로 한 유명한 인플루언서 다섯 명과 그들의 인스타 아이디도 함께 줘.",
                },
                {
                    "role": "user",
                    "content": f"성격: {', '.join(personality)} \n 가치관: {', '.join(view)} \n 특징: {', '.join(character)} \n 취향: {', '.join(taste)}",
                },
            ],
            model="gpt-4o",
        )
    st.write(chat_completion.choices[0].message.content)
