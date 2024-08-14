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
          padding: 2rem 1rem 10rem;
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
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}
.header-container img {
    margin-right: 10px;
}
.header-container h1 {
    display: inline;
    margin: 0;
}
 </style>
    """,
    unsafe_allow_html=True
)


import base64

def get_image_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_base64 = get_image_as_base64("./images/aumlee_logo.png")
image_html = f'<img src="data:image/png;base64,{image_base64}" width="80">'


# 이미지와 텍스트를 같은 줄에 배치
st.markdown(f"""
<div class="header-container">
    {image_html}
    <h1>엄이디퓨전</h1>
</div>
""", unsafe_allow_html=True)

iframe_code = '<iframe src="https://www.aumlee.co.kr/aumlee/main.php3" width="100%" height="600px" style="border:none; overflow:auto;" scrolling="yes"></iframe>'
iframe_code2 = '<iframe src="http://192.9.201.151:7860/?__theme=dark" width="100%" height="600px" style="border:none; overflow:auto;" scrolling="yes"></iframe>'
iframe_code3 = '<iframe src="http://192.9.201.151:7860/?__theme=dark" width="100%" height="600px" style="border:none; overflow:auto; ;height: 1200px;" ></iframe>'
iframe_code4 = '<iframe src="http://aumlee.biz/intranet/aumlee_calendar/aumlee_schedule.php3?cate=car&code=car0492" width="100%" style="border:none; overflow:auto;height: 1200px;" ></iframe>'

tab1, tab2, tab3, tab4 = st.tabs(["프롬프트 생성기", "프롬프트 분석기", "엄이디퓨전 서버", "서버예약"])

with tab1:
    st.header("b dog1")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    
    st.write("클립보드에 복사할 텍스트:")
    text_to_copy = """((A photography showcase of Fallingrene and timeless))ve 
    "into" the world""".replace("\n", "").replace('"', '\\"')
# 클립보드 복사 버튼 생성
# Custom HTML/JS Component
    components.html(f"""
        <button onclick="copyToClipboard()">클립보드로 복사</button>
        <script>
            function copyToClipboard() {{
                navigator.clipboard.writeText("{text_to_copy}").then(function() {{
                    alert('텍스트가 클립보드에 복사되었습니다.');
                }}, function(err) {{
                    console.error('복사 중 오류 발생:', err);
                }});
            }}
        </script>
    """, height=100)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    components.html(iframe_code3, height=800)
with tab4:
    components.html(iframe_code4, height=600)
