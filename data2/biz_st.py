import streamlit as st

"""
# 비즈니스 모델 분석

[네이버](https://www.naver.com/)  
[홍익대학교](https://www.hongik.ac.kr/)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]

```python
import streamlit as st

print("코드 블록")
```
"""
st.caption('캡션(작고 흐린 글씨로 표현됨): st.caption()')

with st.echo():
    #이 블록의 코드와 결과를 출력
    name = 'Sunwoo Lee'
    st.write("Hello, Streamlit", name)

st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"

'#### :orange[이미지: st.image()]'
st.image(".data/python설명.jpeg", caption = "파이썬 로고", width = 300)

'#### :orange[오디오: st.audio()]'
st.audio(".data/waterafromusic.mp3", format = "audio/mpeg", loop = True)

'#### :orange[비디오: st.video()]'
# 'rb' : 바이너리 모드로 파일 열기
video_file = open(".data/소.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider()

'# 콜아웃'
'#### :orange[정보: st.info()]'
st.info(
    icon = "ℹ️",
    body = '''
    **sunglasses: 이것은 정보를 제공하는 콜아웃입니다.**
    - : red[빨간색 텍스트]
        - :blue[파란색 텍스트]
    - :green[초록색 텍스트]
        - :orange[주황색 텍스트]
    '''
)

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon = "⚠️")

'#### :orange[에러: st.error()]'
st.error('This is an error message', icon = "❌")

'#### :orange[성공: st.success()]'
st.success('This is a success message', icon = "✅")

'#### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id': [1, 2, 3], 
     'name': ['Alice', 'Bob', 'Charlie'],
     'age': [24, 34, 45]
     }
)
df

'''
|이름|학번|학과|
|---|---|---|
|홍길동|20230001|컴퓨터공학과|
|김철수|20230002|전자공학과|
|이영희|20230003|기계공학과|
'''

'#### :orange[지표(Metric)]'
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")    

st.divider()