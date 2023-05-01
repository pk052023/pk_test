import streamlit
import pandas 

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
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"Kiwi")

# write your own comment - using Pandas to normalize the JSON dataset 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - flatten the JSON data
streamlit.dataframe(fruityvice_normalized)

# key in your favorutie fruit
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)



