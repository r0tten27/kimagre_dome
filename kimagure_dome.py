import streamlit as st
import time
import html

# ページの設定
st.set_page_config(page_title="きまぐれドーム　test")

# カスタムCSSの適用
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Gothic';
        src: local('Yu Gothic'), local('游ゴシック'), local('MS Gothic'), local('Hiragino Kaku Gothic ProN'), sans-serif;
    }
    body, p {
        background-color: black;
        color: white;
        font-family: 'Gothic', sans-serif;
        margin: 0;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True
)

text = '''
4月1日



４月になってしまった。だらだらと準備をしたりしながら過ごしていると３月が終わった。出遅れていて、ドームを出ようと言うのだから急いだほうがいいのは分かっているのだが体が思うように動かずゆっくりしている。

'''

# テキスト表示のプレースホルダー
placeholder = st.empty()
display_text = ''

# 起動後に1秒待機
time.sleep(1)

# テキストを一文字ずつ表示
for char in text:
    display_text += char
    # 特殊文字をエスケープ
    escaped_text = html.escape(display_text)
    html_text = f'<p>{escaped_text}</p>'
    placeholder.markdown(html_text, unsafe_allow_html=True)
    time.sleep(0.2)