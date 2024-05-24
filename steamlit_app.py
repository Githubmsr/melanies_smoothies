# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)
st.title(":cup_with_straw:  Custom Smoothie Order Form!:verified:")
st.write( """orders that need to filled.""")

#import streamlit as st

name_on_order= st.text_input('Name on Smoothie:')
st.write("The name on your Smoothie wiil be:", name_on_order)

#import streamlit as st

#option = st.selectbox(
    #"How would you like to be contacted?",
    #("Email", "Home phone", "Mobile phone"))

#st.write("You selected:", option)
import streamlit as st
from snowflake.snowpark.functions import col
#import streamlit as st

#option= st. selectbox (
#'What is your favorite fruit?', 
#'Banana', 'Strawberries', 'Peaches'))
#st.write ('Your favorite fruit is:', option)

from snowflake.snowpark.functions import col
session = get_active_session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe
)
if ingredients_list: 
   ingredients_string=''
    
   for fruit_chosen in ingredients_list:
       ingredients_string+= fruit_chosen + ''
       
  # st.write(ingredients_list)
 
my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" +ingredients_string+ """')"""

#st.write(my_insert_stmt)
if ingredients_string:
   session.sql(my_insert_stmt).collect()
   st.success('Your Smoothie is ordered!', icon="✅")
    
time_to_insert = st.button('Submit order')
if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!',icon="✅")
    
my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" +ingredients_string+ """','"""+name_on_order+"""')"""

#st.write(my_insert_stmt)
#st.stop()

time_to_insert = st.button('Submit Order')
