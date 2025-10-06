# https://streamlit.io/

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("Streamlit Practice")

st.write("Progress bar")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

"Done!!!"

st.write("DataFrame")
df = pd.DataFrame({
    "1 row": [1,2,3,4,],
    "2 row": [10,20,30,40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.dataframe(df.style.highlight_max(axis=1), width=300, height=300)

st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
# comment



df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a','b','c']
)

df

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)
st.map(df)


st.write("Display Image")


if st.checkbox("Show image"):
    img = Image.open("sample.png")
    st.image(img, caption="caption", use_column_width=True)


option = st.selectbox(
    "number",
    list(range(1,11))
)
"あなたの好きな数字は", option, "です"


st.write("Interactive Widgets")
text = st.text_input("あなたの趣味を教えてください")
st.write(f"あなたの趣味は {text} です")


condition= st.slider("調子は？", 0,100,50)
"調子",condition


st.write("サイドバー")
textSidebar = st.sidebar.text_input("あなたの趣味を教えてください",key="sidebar_text")
conditionSidebar = st.sidebar.slider("調子は？", 0, 100, 50, key="sidebar_condition")

"あなたの趣味は", textSidebar, "です"
"あなたの調子は",conditionSidebar, "です"


left_column, right_column = st.columns(2)

button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("This is 右カラム")


expander = st.expander("問い合わせ")
expander.write("内容を書く")

expander2 = st.expander("問い合わせ2")
user_input = expander2.text_input("ここに入力してください")
expander2.write(f"入力内容: {user_input}")




