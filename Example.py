import streamlit as st
import urllib.request
from PIL import Image
import time

def videoUserDefined(src: str, width="100%", height=315):
    """An extension of the video widget
    Arguments:
        src {str} -- url of the video Eg:- https://www.youtube.com/embed/B2iAodr0fOo
    Keyword Arguments:
        width {str} -- video width(By default: {"100%"})
        height {int} -- video height (By default: {315})
    """
    st.write(
        f'<iframe width="{width}" height="{height}" src="{src}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )

def main():

    # Test/Title
    st.title('StreamLit basic Concepts')

    # Header/Subheader
    st.header("To Create Header")
    st.subheader("To Create subheader")    

    st.subheader("Do you want to build the GUI using web app")
    st.code('pip install streamlit')

    #text
    st.text("hello Streamlit")

    #Markdown
    st.markdown("### This is a Markdown")

    #Will be used for displaying the Error Messages in a colourful format
    st.success("Successful")
    st.info("Information!")
    st.warning('this is a warning')
    st.error("this is an error Danger")
    
    # Exception handling
    st.exception("IndexError('list out of index')")

    #help of the function
    st.help(range)

    st.write("Text with write")

    st.write(range(10))

    #Image opening
    img = Image.open("download.jfif") #open the image stored in specified location
    #img = Image.open(urllib.request.urlopen("https://mms.businesswire.com/media/20200616005364/en/798639/22/Streamlit_Logo_%281%29.jpg")) # Opens the image from the url
    st.image(img, width=300, caption="Simple Image")

    # Video playing
    #vid_file = open("sample-mp4-file.mp4","rb").read() #play the video stored in specified location
    #st.video(vid_file)
    videoUserDefined("https://www.youtube.com/embed/B2iAodr0fOo")

    #widgets
    if st.checkbox("Show/hide"):
        st.text("Showing or Hiding Widget")

    # Radio
    status = st.radio("What is your status",("Married","Single"))
    if status == 'Married':
        st.success("You are Married")

    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'Navigation',
        ('Home', 'About', 'Help')
    )

    if add_selectbox == 'About':
        st.write('You have selected about page')
    elif add_selectbox == 'Home':
        st.write('you have selected Home page')
    else:
        st.write('you have selected help page')

    # Sample Progress bar
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    st.balloons()

    
##########################################################################
# @brief Entry point of the python
##########################################################################
if __name__ == '__main__':
    main()
