from pathlib import PureWindowsPath
import streamlit as st

#Text/Title
st.title('Streamlit Tutorials')

#Header
st.header('This is a header')

#Sub header
st.subheader('This is a sub header')

#Text
st.text('Hello streamlit')

#Markdown
st.markdown('### This a Markdown')

#Error/colorful text
st.success('successful')

st.info('information!')

#warning
st.warning('Warning')

#print an error meassage
st.error('This is an error')

#put an exception
st.exception('NameError:Name three not defined')

#Get Help 
st.help(range)

#Writing a Text
st.write('Text with write')
st.write(range(10))

#Images
from PIL import Image
img=Image.open("example.png")
st.image(img,width=300,caption="Simple Image")

#Videos
vid_file=open("Example.mp4","rb").read()
#vid_bytes=vid_file.read()
st.video(vid_file)

#Audio 
audio_file=open("Example.mp3","rb").read()
st.audio(audio_file,format='audio/mp3')

#Widget
#Checkbox
if st.checkbox("Show/Hide"):
    st.text("showing or hiding widget")

#Radio
status=st.radio("what is your status",("Active","Inactive"))
if status == 'Active':
    st.success("you are Active")
else:
    st.warning("Inactive, Activate")    

#SelectBox
occupation = st.selectbox("Your Occupation",["Programmer"
,"Data Scientist"])    
st.write("You Selected This option",occupation)

#MultiSelect
location=st.multiselect("What Do You Work?",("Londan",
"Newyork","Egypt"))
st.write("You Selected ",len(location),"options")

#Slider 
#1 is the lower limit and 5 is the upper limit
level=st.slider("what is your level",1,5)

#Buttons
st.button("Simple Button")
if st.button("About"):
    st.text("Streamlit is Cool")

#Text Input
firstname= st.text_input("Enter Your Firstname","Type Here...")
if st.button("submit"):
    result=firstname.title()
    st.success(result)

#Text Area    
message= st.text_area("Enter Your message","Type Here...")
if st.button("Submit"):
    result=message.title()
    st.success(result)

#Date Input
import datetime 

today=st.date_input("Todat is",datetime.datetime.now())

#Time 
the_time=st.time_input("The time is",datetime.time())

#Display jason
st.text("Display Json")
st.json({"name" :"jesse","age":23})

#Display Row Code
st.text("Display Row Code")
st.code("import numpy as np")

#Display Row Code width
with st.echo():
    #This will also show as a comment
    import pandas as pd
    import numpy as np
    df=pd.DataFrame()

#Progress Bar
import time 
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

#Spinner 
with st.spinner ("waiting.."):
    time.sleep(5)
st.success("Finished!")    

#Ballons
st.balloons()

#SIDEBAPS
st.sidebar.header("About")
st.sidebar.text("This is dtreamlit Tut")

#Functions
#st.cache
def run_function():
    return range(100)

st.write(run_function())

#Plot
#st.pyplot()

#DataFrame
#st.dataframe(df)

#Tbales
#st.table(df)