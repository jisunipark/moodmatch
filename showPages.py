import streamlit as st


MULTISELECT_PLACEHOLDER = "최대 다섯 개까지 고를 수 있어요"


def showLogo():
    with st.container(height=100, border=None):
        st.image("logo.svg", width=250)


def showPage1():
    st.image("logo.svg", width=400)
    st.subheader("나만의 분위기를 만들고 싶다면")
    st.subheader("CHUGUMI FOR YOU에서")
    st.subheader("나만의 라이프스타일 추구미를 발견해보세요")


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
