import os
from openai import OpenAI

def get_city_prompt(user_info):
    """
    사용자 정보를 기반으로 도시 추천을 위한 프롬프트를 생성합니다.
    """
    prompt = f"""
    사용자의 선호도와 정보를 바탕으로 가장 적합한 도시를 추천해주세요.
    
    사용자 정보:
    {user_info}
    
    다음 형식으로 답변해주세요:
    {{
        "city": "추천 도시",
        "reason": "추천 이유",
        "style": "추천 스타일",
        "description": "상세 설명"
    }}
    """
    return prompt

def get_style_prompt(user_info, city):
    """
    사용자 정보와 선택된 도시를 기반으로 스타일 추천을 위한 프롬프트를 생성합니다.
    """
    prompt = f"""
    사용자의 선호도와 선택된 도시를 바탕으로 가장 적합한 스타일을 추천해주세요.
    
    사용자 정보:
    {user_info}
    
    선택된 도시:
    {city}
    
    다음 형식으로 답변해주세요:
    {{
        "style": "추천 스타일",
        "reason": "추천 이유",
        "description": "상세 설명"
    }}
    """
    return prompt

def get_ai_response(prompt):
    """
    OpenAI API를 사용하여 AI 응답을 받아옵니다.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that recommends cities and styles based on user preferences."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content 