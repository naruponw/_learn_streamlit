import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Hello world!')

st.write('Hello Boom!')

st.write('Hello Data Rockie community')

st.button("Say hello")

st.sidebar.subheader('Input')
url_input = st.sidebar.text_input('GitHub URL', 'https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')


# st.write('The GitHub URL of your data is: ', url_input)
# st.info(f'The GitHub URL of your data is: {url_input}')

# st.subheader('Output')



if url_input:
    st.subheader('Output')
    #st.warning(f'The GitHub URL of your data is: {url_input}')
    st.success(f'The GitHub URL of your data is: {url_input}')

    df = pd.read_csv(url_input)
    st.write(df)

    target_columns = df.columns[-1]
    st.write(target_columns)

    df2 = df.groupby(target_columns).mean() 
    st.write(df2)
    st.bar_chart(df2)

    st.bar_chart(df[target_columns].value_counts())



else:
    st.subheader('Enter your input')
    st.error(f'👈🏿 Awaiting your input!')


st.header('Sandbox')
X = df.columns[-1]

genre = st.radio(
    "Select your Class value",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")









