import streamlit
import pandas 
import snowflake.connector 
import requests
from urllib.error import URLError

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text('Omega3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard - bolied free range egg') 


# Display the table on the page.
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)  
# create a function
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized 

#New section 
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
   if not fruit_choice:
       streamlit.error('Please select a fruit to get information.')
   else:
       back_from_function=get_fruityvice_data(fruit_choice) 
       streamlit.dataframe(back_from_function)
except URLError as e:
       streamlit.error()


streamlit.write('The user entered ', fruit_choice) 

streamlit.stop()


def get_fruit_load_list():
   with my_cur = my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()
   
# Add a button to fetch fruits 
if streamlit.button('Get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows=get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

# key in your favorutie fruit
add_fruit_to_the_list = streamlit.text_input('What fruit would you like?','Kiwi') 
streamlit.write('Added: ', add_fruit_to_the_list) 
my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('test')")

