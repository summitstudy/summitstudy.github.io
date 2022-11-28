from colorama import AnsiToWin32
import streamlit as st #플라스크 젠고같은 중교모 프로젝트를 할 것이다. 하드테크닉 할 것이다. 기본적인 아키텍쳐를 알아야한다.
#웹 프레임워크에 대해 할려고 한다. #분석하고 퍼센트 내도록 만든다.
import pandas as pd

st.header('아동용 앱을 위한 AI 이미지 분석 프로젝트')
st.write('인공지능을 이용해 정보화 시대의 문제를 해결해 봅시다. -인공지능융합교육콘텐츠 개발 실습-')

st.markdown('---')
st.subheader('🚩수행과제\(프로젝트 만들기\)')

st.write('아동용 앱을 이용하는 어린이들을 위해 인공지능을 활용한 이미지 분류\(차단\) 프로그램을 만들어 봅시다.')
st.write('참고할 사이트:')
st.write('https://teachablemachine.withgoogle.com/')
#--------------------------------------
st.markdown('---')
st.subheader('🧱프로젝트 샘플')
st.write('이미지의 폭력성, 선정성 정도를 분석하는 AI 이미지 분석기 입니다.')
file = st.file_uploader('이미지를 올려주세요.', type=['jpg','png'])
if file is None:
    st.warning('이미지가 업로드 되지 않았습니다.')
else:
    st.image(file)
st.write('🚩프로그램 제작 과정을 요약하여 보고서를 작성해주세요.\(30점\)')
content1 = st.text_area('Project Report: ',height= 170, key=0)
if st.button('제출하기'):
    if content1 != '':
            
          
        content1 = content1.replace('\n', '<br>')
        st.write(f'Project Report:<br>{content1}', unsafe_allow_html=True)
        #데이터 저장
        csvdf = pd.read_csv("./pro.csv", encoding='utf-8')
        new_data = {"project":content1}
        csvdf = csvdf.append(new_data, ignore_index=True)
        csvdf.to_csv("./pro.csv",index = False)
        st.write('<<프로젝트 보고서가 완성되었습니다!>>')
        #------------------------------------------------------
    else:
        st.warning('내용을 입력해주세요.')

