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


st.markdown('streamlit은 **마크다운 문법** 지원 합니다.')

st.table([
['이름','나이'],
['홍길동','43'],
['뽀로로','23'],
])

st.metric(label='삼성전자', value='151,200원', delta="+1200원")

st.title('write()')
st.write("hello")
st.write(10,20,30)
st.write([1,2,3,4])
st.write({"x":100, "y":3.14})

[100,200,300,400]   # 알아서 해석해서 출력