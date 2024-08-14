import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="chatGPT API 서비스 개발",
)

# 사용자 정의 CSS 추가
st.markdown("""
    <style>
    .st-emotion-cache-13ln4jf {
        max-width: 130rem;
        padding: 1rem 1rem 10rem;
    }
    .viewerBadge_container__1QSob { 
        display: none; 
    }

[data-testid="stIFrame"]{
        height: 1200px;
}
[data-testid="stHeadingWithActionElements"]{
    text-align: center;
}
[data-testid="stHeader"] {
    display: none;
}
[data-testid="stAppViewBlockContainer"]{
  padding-top: 12rem; 
}
 </style>
    """,
    unsafe_allow_html=True
)

st.header("엄이디퓨전")

iframe_code = '<iframe src="https://www.aumlee.co.kr/aumlee/main.php3" width="100%" height="600px" style="border:none; overflow:auto;" scrolling="yes"></iframe>'
iframe_code2 = '<iframe src="http://192.9.201.151:7860/?__theme=dark" width="100%" height="600px" style="border:none; overflow:auto;" scrolling="yes"></iframe>'
iframe_code3 = '<iframe src="http://192.9.201.151:7860/?__theme=dark" width="100%" height="600px" style="border:none; overflow:auto; ;height: 1200px;" ></iframe>'
iframe_code4 = '<iframe src="http://aumlee.biz/intranet/aumlee_calendar/aumlee_schedule.php3?cate=car&code=car0492" width="100%" style="border:none; overflow:auto;height: 1200px;" ></iframe>'

tab1, tab2, tab3, tab4 = st.tabs(["프롬프트 생성기", "프롬프트 분석기", "엄이디퓨전 서버", "서버예약"])

with tab1:
    st.header("b dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    components.html(iframe_code3, height=800)
with tab4:
    components.html(iframe_code4, height=600)
