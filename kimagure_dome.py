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



text='''
ドームの建て方
　さて、あなた達が見ているドームの建て方を知りたくないですか。でも結構簡単なんです。ほら、普段野球やバレーを見る時に使うあの小さなドームを大きくしただけです。単純でしょ。え、太陽はどうなんだって？まあ、確かにライトで天井は埋め尽くしてるけど。そんなの普段のドームと変わんないじゃん。………。分かったからもう少し真面目に話すよ。このドームは空気膜構造が使われているんだよ。ほら、中に空気を入れたら膨らむ感じ。そうそう。だから出口が少ないんだよ。それにね……。
（何故かここで終わってしまっている）
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

image_path = "./img/dome.jpg"  # ここに画像のパスを指定します
st.image(image_path, use_column_width=True)