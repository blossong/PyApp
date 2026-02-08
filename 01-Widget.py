import streamlit as st

import os, time

print(f"✅ {os.path.basename(__file__)} 실행됨 {time.strftime('%Y-%m-%d %H:%M:%S')}")

st.title("다양한 widgent들")

# 선택한 값이 model에 입력됨
model = st.selectbox("모델선택",("GPT-3","GPT-4","GPT-5"))

st.markdown(f"model: {model}")


# 입력창이 뜨면서 입력된 값이 name에 입력됨
name = st.text_input("이름이 뭡니까?")

# 색상도 넣을 수 있음(:red)
st.markdown(f"이름: :red[{name}]")


# 기본값: 0부터 100까지 선택 가능
value = st.slider(label="temperature",
            min_value=0.1, max_value=1.0)

st.markdown(f"value: :green[{value}]")

# 사용자 입력에 따라 다르게 구현 가능
if value > 0.4:
    st.write("다양성이 높은 모델")

else:
    st.write("정형화된 답변을 하는 모델")
    st.text_input("질문을 입력해보세요")


# 클릭할 때마다 코드 실행
button= st.button("버튼을 눌러보세요") #리턴값 true(누르면)

if button:
    st.write(":blue[버튼] 이 눌렸습니다. :sparkless:")

st.markdown('---')
num1=st.number_input('숫자 1 입력',
                min_value=10, max_value=100, step=5)


num2=st.number_input('숫자 2 입력',
                min_value=10, max_value=100, step=5)

btn_calc=st.button('계산을 합니다')

if btn_calc:
    st.markdown(f"""   # write는 줄바꿈 안되어서 markdown으로
             {num1}+{num2} = {num1+num2}

             {num1}-{num2} = {num1+num2}
             """)
