import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import time

# st.header('MS Udalova')
# # st.button('Say hello')
#
# st.write('Above')
# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')
#
# st.write('Under')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

df = pd.DataFrame({
    'first column': ['Все', 'ГМ', 'СМ', 'ВГ', 'ЗМ'],
    'second column': [10, 20, 30, 40, 50]
    })


column_format, column_city, col_devision = st.columns(3)
# You can use a column just like st.sidebar:
with column_format:
     option_f = st.selectbox(
          'Выберете формат',
          df['first column'])
     'You selected: ', option_f

with column_city:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


with col_devision:
     option_dev = st.selectbox(
          'Выберете дивизион',
          df['first column'])
     'You selected: ', option_dev


# latest_iteration = st.empty()
# bar = st.progress(0)
#
# for i in range(100):
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)