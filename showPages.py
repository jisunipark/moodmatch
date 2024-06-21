import streamlit as st


def showPage1():
    st.progress(0)
    st.write(
        "당신의 캐릭터를 바탕으로 당신의 분위기에 어울리는 도시를 추천해주고 당신만을 위한 라이프스타일 큐레이션을 제공합니다."
    )


# 성격 - character
def showPage2():
    st.progress(33)
    st.write("당신의 성격을 알려주세요")
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
    )
    return ", ".join(character)


# 가치관 - values
def showPage3():
    st.progress(66)
    st.write("당신의 가치관을 알려주세요")
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
    )
    return ", ".join(values)


# 취향 - taste
def showPage4():
    st.progress(100)
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

    return ", ".join(taste)
