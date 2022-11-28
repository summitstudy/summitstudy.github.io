from colorama import AnsiToWin32
import streamlit as st #플라스크 젠고같은 중교모 프로젝트를 할 것이다. 하드테크닉 할 것이다. 기본적인 아키텍쳐를 알아야한다.
#웹 프레임워크에 대해 할려고 한다. #분석하고 퍼센트 내도록 만든다.
import pandas as pd

st.header('아동용 앱을 위한 AI 이미지 분석 프로젝트')
st.write('인공지능을 이용해 정보화 시대의 문제를 해결해 봅시다. -인공지능융합교육콘텐츠 개발 실습-')
st.markdown('---')
st.subheader('✍️학생평가')
df0 = pd.read_csv("./name.csv", encoding='utf-8')
df1 = pd.read_csv("./data.csv", encoding='utf-8')
df2 = pd.read_csv("./data1.csv", encoding='utf-8')
df3 = pd.read_csv("./pro.csv", encoding='utf-8')

df = pd.concat([df0,df1,df2,df3],axis=1)
if(df.iloc[-1,:6] is None):
    df0.iloc[-1,:1] = (None)
#df.iloc[-1,:6] = ('')
 #데이터프레임 df를 수정할 수는 있으나 개별화된 엑셀 파일이 수정되지 않아
            #다시 웹 페이지를 열면 삭제했다고 생각한 값이 다시 살아난다.

st.write(df)
#st.image('./max.png')
st.write('📌내용 체계와 성취 기준 (2022교육과정 기준)')
st.write('4\) 인공지능 - 인공지능 시스템을 활용하여 해결할 수 있는 문제 발견하기')
st.write('📌활동별 평가 기준')
st.image('./max.png')
#st.write(df2)
