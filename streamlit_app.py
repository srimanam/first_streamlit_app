import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents new healthy diner')
streamlit.header ('Breakfast Favorites')
streamlit.text('  🥣  Omega 3 & Blueberry oat dinner')
streamlit.text ('  🥗  Kale, sponach and Rocket smoothie')
streamlit.text ('  🐔  Hard-boiled free range egg')
streamlit.text ('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
# Display the table on the page
streamlit.dataframe(my_fruit_list)
 
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Display table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error("Please select a fruit to get information.")
 else:
      back_from_function= get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
#streamlit.write('The user entered ', fruit_choice)

  #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# write your own comment -what does the next line do? 
 # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?

  #streamlit.dataframe(fruityvice_normalized)
                                     
except URLError as e:
 streamlit.stop()

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * FROM fruit_load_list")
#my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contains")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM fruit_load_list")
         return my_cur.fetchall()
 # Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
#add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")


