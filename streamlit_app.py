import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header ('Breakfast Favorites')
streamlit.text('  🥣  Omega 3 & Blueberry oat dinner')
streamlit.text ('  🥗  Kale, sponach and Rocket smoothie')
streamlit.text ('  🐔  Hard-boiled free range egg')
streamlit.text ('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
