import streamlit as st

st.title("안녕하세요 Streamlit")

st.header("헤더를 입력할 수 있어요 :sunglasses")

st.subheader("이것은 subheader 입니다.")

st.text("일반적인 텍스트 출력")

st.caption("캡션을 넣어봅니다")

sample_code ='''
def function:
    print('hello world')
    '''
st.text(sample_code)
st.code(sample_code)