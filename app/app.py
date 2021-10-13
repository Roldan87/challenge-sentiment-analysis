import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from PIL import Image

def main():
    st.set_page_config(page_title="Netflix Sentiment Analysis", layout='wide')

    # Title of the page
    st.title('Netflix Sentiment Analysis')

    #Sidebar
    st.sidebar.title('Netflix-Twitter Analysis')
    st.sidebar.write('''45k tweets
                        \nNLP model: TextBlob''')

    show_list = ['Netflix', 'Daredevil', 'Witcher', 'SquidGame', 'Punisher', 'Lucifer', 'Narcos', 'BlackMirror', 'StrangerThings', 'LaCasadePapel']
    user_show = st.multiselect('Choose a Netflix show to see the overall sentiment', show_list, ['Netflix'])
    if user_show is not None:
        st.write('You selected:')
        for i in user_show:
            st.write(i)
        data_load_state = st.text('Loading sentiment analysis...')


        for i in user_show:
            df = pd.read_csv(f'./datasets/{i.lower()}_tweets.csv')
            fig = px.pie(df, values=df.Sentiment.value_counts(), names=df.Sentiment.value_counts().index, title=f'{i} Sentiment Analysis', color_discrete_sequence=px.colors.qualitative.Dark2)
            st.plotly_chart(fig, use_container_width=True)

        for i in user_show:
            show_cover = Image.open(f'./assets/{i.lower()}_netflix.jpg')
            st.sidebar.image(show_cover, use_column_width=True)


if __name__ == "__main__":
    main()