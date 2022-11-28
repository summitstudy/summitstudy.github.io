import streamlit as st #플라스크 젠고같은 중교모 프로젝트를 할 것이다. 하드테크닉 할 것이다. 기본적인 아키텍쳐를 알아야한다.
#웹 프레임워크에 대해 할려고 한다. #분석하고 퍼센트 내도록 만든다.
import pandas as pd
import pandas as sspd
#일단 1차보고서만 제대로 만들어보기!!!!
st.header('아동용 앱을 위한 AI 이미지 분석 프로젝트')
st.write('인공지능을 이용해 정보화 시대의 문제를 해결해 봅시다. -인공지능융합교육콘텐츠 개발 실습-')

st.markdown('---')
st.subheader('🌱1차 보고서 만들기')
title = 1
col1, col2 = st.columns(2)
with col1:
    st.image('./img5.jpg')
with col2:
    st.write('✅다음 그래프를 통해 알 수 있는 내용은 무엇인가요? 연령대별 특징을 중심으로 알 수 있는 내용을 적어봅시다. \(15점\)')
    content1 = st.text_area('활동1: ', height=170, key=0)

col1, col2 = st.columns(2)
with col1:
    st.video('https://www.youtube.com/watch?v=zAbNVV_05Tg')
with col2:
    st.write('✅왼쪽의 영상에서 발견 할 수 있는 사회 문제는 무엇인가요? 이에 대한 느낀점을 쓰세요. \(15점\)')
    content2 = st.text_area('활동2: ', height=170, key=1)
#title, content1, content2
#---------------------------------------------------------------------



if st.button('제출하기'):
    if title != '':
        if content1 != '' and content2 != '':
            
            #단순 출력
            content1 = content1.replace('\n', '<br>')
            st.write(f'활동1:<br>{content1}', unsafe_allow_html=True)
            content2 = content2.replace('\n', '<br>')
            st.write(f'활동2:<br>{content2}', unsafe_allow_html=True)

            #데이터 저장
            csvdf = pd.read_csv("./data.csv", encoding='utf-8')
            new_data = {"act1-1":content1,"act1-2":content2}
            csvdf = csvdf.append(new_data, ignore_index=True)
            csvdf.to_csv("./data.csv",index = False)
            st.write('<<1차 보고서 파일이 완성되었습니다!>>')
            #------------------------------------------------------
        else:
            st.warning('내용을 입력해주세요.')
    else:
        st.warning('학번과 이름을 입력해주세요.')

