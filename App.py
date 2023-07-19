import streamlit as st

st.set_page_config(page_title='Bloodborne', page_icon='tada', layout='wide')

# HEADER
with st.container():
    left_column, right_column = st.columns([1, 2])
    with left_column:
        st.title("Hi, It's my App about Bloodborne")
        st.subheader("This site is bloodborne-game project")
        st.write("**Let's explore some main bosses**")
    with right_column:
        st.image('main.jpg', use_column_width=True)

# Father Gascoigne
with st.container():
    st.write('---')
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.image('father.jpg', use_column_width=True)
    with right_column:
        st.header('Father Gascoigne')
        st.subheader('Description')
        st.write("Father Gascoigne is an experienced hunter who has succumbed to the blood-drunkenness of the hunt and, as such, descended into a frenzied killing spree. "
                 "He is armed with the Hunter Axe and a modified version of the Hunter Pistol that acts like the Hunter Blunderbuss, and he also wears his titular Gascoigne's Set.")
        st.subheader('Location')
        st.write('Tomb of Oedon.'
                 'Found past the bridge '
                 'with the flaming boulder in Central Yharnam')

# Cleric Beast
with st.container():
    st.write('---')
    left_column, right_column = st.columns([1, 2])
    with right_column:
        st.image('beast.jpg')
    with left_column:
        st.header('Cleric Beast')
        st.subheader('Description')
        st.write("The Cleric Beast is a massive creature with twisted horns, matted fur, and a malnourished body. Despite appearing emaciated, it has high agility, supernatural strength, and health. It is the first boss encountered in the game and revealed during its development.")
        st.subheader('Location')
        st.write("Great Bridge. At the very end of the Central Yharnam's carriage-filled bridge.")


