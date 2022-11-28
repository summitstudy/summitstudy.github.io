import streamlit as st #플라스크 젠고같은 중교모 프로젝트를 할 것이다. 하드테크닉 할 것이다. 기본적인 아키텍쳐를 알아야한다.
#웹 프레임워크에 대해 할려고 한다. #분석하고 퍼센트 내도록 만든다.
import pandas as pd
col1, col2 = st.columns(2)
with col1:
    st.write('')
with col2:
    st.write('')
st.title('정보윤리교육개론')
st.header('아동용 앱을 위한 AI 이미지 분석 프로젝트')
st.write('📌내용 체계와 성취 기준 (2022교육과정 기준)')
st.write('4\) 인공지능 - 인공지능 시스템을 활용하여 해결할 수 있는 문제 발견하기')

df0 = pd.read_csv("./name.csv", encoding='utf-8')
df1 = pd.read_csv("./data.csv", encoding='utf-8')
df2 = pd.read_csv("./data1.csv", encoding='utf-8')
df3 = pd.read_csv("./pro.csv", encoding='utf-8')
df = pd.concat([df0,df1,df2,df3],axis=1)

st.markdown('---')
title = st.text_input('✔️학번과 이름을 적어주세요.')
title = title.replace('\n', '<br>')
if st.button('제출하기'):
    if title != '':
        df.iloc[1,:1] = ('1')
        if(df.iloc[:,:6] is None):
            df.iloc[-1,:5] = ('1')

        st.write(f'학습자 정보: {title}')
        csvdf = pd.read_csv("./name.csv")
        new_data = {"inf":title}
        csvdf = csvdf.append(new_data, ignore_index=True)
        csvdf.to_csv("./name.csv",index = False)
        st.write('<<학번과 이름이 저장되었습니다!>>')
    else:
        st.warning('학번과 이름을 입력해주세요.')

