import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import seaborn as sns

def sidebar():
    st.set_page_config(layout='wide', page_title='title name', page_icon='🎈')

    st.sidebar.title('🎈 Sidebar Title')

    st.sidebar.markdown('---')

    st.sidebar.subheader('🎈 Subheader Title')
    variable = st.sidebar.text_input(label='Text Input', value='default value')


    st.title('🎈 App Name')

if __name__ == '__main__':
    sidebar()
    st.write('Hello world!')
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    # Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, 
            group_labels, 
            bin_size=[.1, .25, .5],
            )

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    fig,ax = plt.subplots()

    # sns.barplot(data = hist_data, ax=ax)
    sns.histplot(data = hist_data, ax=ax)
    st.pyplot(fig)



