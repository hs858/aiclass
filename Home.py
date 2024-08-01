import textwrap
import streamlit as st

def to_markdown(text):
    text = text.replace('•', '*')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

st.title("우당탕탕 streamlit앱")
st.subheader("소개")
st.markdown("우당탕탕 Streamlit 앱에 오신 것을 환영합니다! 떠오르는 주제로 우당탕탕 만들었습니다.")
st.subheader("기능")
st.markdown("""
* **코드 예제 1**: 생물을 입력하면 분류체계와 특징을 보여줍니다.
* **코드 예제 2**: 생물을 입력하면 분류체계와 특징을 보여줍니다.
* **코드 예제 3**: 세포분열단계의 특징을 보여줍니다.
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
