import textwrap
import google.generativeai as genai
import streamlit as st
import requests

def to_markdown(text):
    text = text.replace('•', '*')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

api_key = "AIzaSyCMNtDW9-Sa8iz0DKEOUaWRMXeD21MXdtY"
unsplash_access_key = "Unsplash API key를 입력하세요"

# Few-shot 프롬프트 구성 함수 수정
def try_generate_content(api_key, prompt):
    # API 키를 설정
    genai.configure(api_key=api_key)
   
    # 설정된 모델 변경
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config={
                                      "temperature": 0.9,
                                      "top_p": 1,
                                      "top_k": 1,
                                      "max_output_tokens": 2048,
                                  },
                                  safety_settings=[
                                      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                  ])
    try:
        # 콘텐츠 생성 시도
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # 예외 발생시 None 반환
        print(f"API 호출 실패: {e}")
        return None

def get_image_url(creature_name, access_key):
    url = f"https://api.unsplash.com/search/photos?query={creature_name}&client_id={access_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"][0]["urls"]["regular"]
    return None

# Streamlit 앱 구성
st.title("생물 분류 및 특성 시스템")
st.write("생물의 이름을 입력하면 해당 생물이 속하는 분류와 특성을 알려줍니다.")

st.text("만든이:HS")

creature_name = st.text_input("생물의 이름을 입력하세요:")

if st.button("확인"):
    if creature_name:
        prompt = f"다음 생물을 분류하고 문 단계까지의 분류 체계와 특성을 한국어로 제공해주세요: {creature_name}."
        result = try_generate_content(api_key, prompt)
        
        if result:
            st.markdown(to_markdown(result))
            image_url = get_image_url(creature_name, unsplash_access_key)
            if image_url:
                st.image(image_url, caption=f"{creature_name}의 이미지", use_column_width=True)
            else:
                st.warning("이미지를 찾을 수 없습니다.")
        else:
            st.error("생물 분류 및 특성 정보를 가져오는 데 실패했습니다.")
    else:
        st.warning("생물의 이름을 입력하세요.")
