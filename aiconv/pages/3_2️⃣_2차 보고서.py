import streamlit as st #플라스크 젠고같은 중교모 프로젝트를 할 것이다. 하드테크닉 할 것이다. 기본적인 아키텍쳐를 알아야한다.
#웹 프레임워크에 대해 할려고 한다. #분석하고 퍼센트 내도록 만든다.
import pandas as pd

st.header('아동용 앱을 위한 AI 이미지 분석 프로젝트')
st.write('인공지능을 이용해 정보화 시대의 문제를 해결해 봅시다. -인공지능융합교육콘텐츠 개발 실습-')

st.markdown('---')
st.subheader('🌱2차 보고서 만들기')
title = 1

st.write('✅1차 보고서의 문제를 인공지능을 활용해 해결할 수 있을까요? 인공지능 기술을 중심으로 해결 방법을 서술해봅시다. \(20점\)')
content1 = st.text_area('활동1: ',height= 170, key=0)
st.write('✅인공지능을 통해 여러 사회 문제를 해결 할 수 있습니다. 인공지능을 활용해 해결할 수 있는 사회 문제에 관해 조사해봅시다. \(20점\)')
content2 = st.text_area('활동2: ', height=170, key=1)

if st.button('제출하기'):
    if title != '':
        if content1 != '' and content2 != '':
            
            #단순 출력
            content1 = content1.replace('\n', '<br>')
            st.write(f'활동1:<br>{content1}', unsafe_allow_html=True)
            content2 = content2.replace('\n', '<br>')
            st.write(f'활동2:<br>{content2}', unsafe_allow_html=True)

            #데이터 저장
            csvdf = pd.read_csv("./data1.csv", encoding='utf-8')
            new_data = {"act2-1":content1,"act2-2":content2}
            csvdf = csvdf.append(new_data, ignore_index=True) 
            csvdf.to_csv("./data1.csv",index = False)
            st.write('<<2차 보고서 파일이 완성되었습니다!>>')
            #------------------------------------------------------
        else:
            st.warning('내용을 입력해주세요.')
    else:
        st.warning('학번과 이름을 입력해주세요.')
#--------------------------------------
