import textwrap
import streamlit as st

def to_markdown(text):
    text = text.replace('•', '*')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

st.title("교육용 Streamlit 앱")
st.subheader("소개")
st.markdown("이 교육용 Streamlit 앱에 오신 것을 환영합니다! 이 앱은 학생들이 Google Generative AI를 사용하여 코딩을 인터랙티브하게 배울 수 있도록 설계되었습니다. 🌟")

st.subheader("기능")
st.markdown("""
* **코드 예제 1**: Generative AI 모델을 사용하는 예제입니다.
* **코드 예제 2**: AI 통합의 또 다른 측면을 보여줍니다.
* **코드 예제 3**: 다양한 AI 모델 구성을 처리하는 방법을 보여줍니다.
""")

st.subheader("탐색")
option = st.selectbox(
    "탐색할 코드 예제를 선택하세요:",
    ("옵션을 선택하세요", "코드 예제 1", "코드 예제 2", "코드 예제 3")
)

if option == "코드 예제 1":
    st.write("코드 예제 1을 선택했습니다.")
    # 여기에서 코드 예제 1의 내용을 불러오거나 보여줍니다.
elif option == "코드 예제 2":
    st.write("코드 예제 2을 선택했습니다.")
    # 여기에서 코드 예제 2의 내용을 불러오거나 보여줍니다.
elif option == "코드 예제 3":
    st.write("코드 예제 3을 선택했습니다.")
    # 여기에서 코드 예제 3의 내용을 불러오거나 보여줍니다.
else:
    st.write("옵션을 선택하세요.")
