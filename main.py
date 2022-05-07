from click import style
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import math

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02 + ((100-i)/1000)**8)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問合せ')
expander.write('問合せ内容を書く1')
expander.write('問合せ内容を書く2')
expander.write('問合せ内容を書く3')



# text = st.text_input('あなた趣味を教えてください。')
# condition = st.slider('あなたの今の調子は', 0, 100, 25)
# 'あなたの趣味：', text ,'です。'
# 'コンディション：', condition



# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('show image'):
#     img = Image.open(r'C:\Users\newki\OneDrive\画像\iCloud Photos\Downloads.old\IMG_1559.JPG')
#     st.image(img, caption='Yuna', use_column_width=True)


# df = pd.DataFrame(
#     data={'lat':[34.388046], 'lon':[132.4555706]}
# )

# st.map(df) 
