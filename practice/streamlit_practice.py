import streamlit as st
import pandas as pd

st.header('학생 정보 입력 프로그램')
st.text('띄어쓰기로 구분하여 한줄씩 입력해주세요.')

header = ['학번', '이름', '전공']

with st.form('student_info'):
    info_str = st.text_area('학생 정보', placeholder='학번 이름 전공')
    submit = st.form_submit_button('입력하기')

    if submit:
        text_split_list = info_str.split('\n')
        student_info_list = [ t.split() for t in text_split_list ]
        result = [ dict(zip(header, t)) for t in student_info_list ]
        
        result_df = pd.DataFrame(result)
        st.table(result_df)
