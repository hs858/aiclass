import textwrap
import google.generativeai as genai
import streamlit as st

def to_markdown(text):
    text = text.replace('•', '*')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

api_key = "AIzaSyCMNtDW9-Sa8iz0DKEOUaWRMXeD21MXdtY"

# few-shot 프롬프트 구성 함수 수정
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

# Streamlit 앱 구성
st.title("세포 분열 단계 정보")

st.text("만든이:과학쌤")

# Dropdown 메뉴
stages = ["간기", "전기", "중기", "후기", "말기", "세포질 분열"]
selected_stage = st.selectbox("세포 분열 단계를 선택하세요:", stages)

stage_prompts = {
    "간기": "Explain the Interphase stage of cell division, including the differences between mitosis and germ cell division, for third-year middle school students. The author is a science teacher.",
    "전기": "Explain the Prophase stage of cell division, including the differences between mitosis and germ cell division, for third-year middle school students. The author is a science teacher.",
    "중기": "Explain the Metaphase stage of cell division, including the differences between mitosis and germ cell division, for third-year middle school students. The author is a science teacher.",
    "후기": "Explain the Anaphase stage of cell division, including the differences between mitosis and germ cell division, for third-year middle school students. The author is a science teacher.",
    "말기": "Explain the Telophase stage of cell division, including the differences between mitosis and germ cell division, for third-year middle school students. The author is a science teacher.",
    "세포질 분열": "Explain the Cytokinesis stage of cell division, including the differences between mitosis and germ cell division, for third-year middle school students. The author is a science teacher."
}

if selected_stage:
    prompt = stage_prompts[selected_stage]
    explanation = try_generate_content(api_key, prompt)
    
    if explanation:
        translation_prompt = f"Translate the following text to Korean: {explanation}"
        translation = try_generate_content(api_key, translation_prompt)
        if translation:
            st.markdown(to_markdown(translation))
        else:
            st.error("콘텐츠 번역에 실패했습니다. 나중에 다시 시도하세요.")
    else:
        st.error("콘텐츠 생성에 실패했습니다. 나중에 다시 시도하세요.")
