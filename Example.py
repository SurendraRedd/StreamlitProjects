import streamlit as st
import urllib.request
from PIL import Image
import time

def video_youtube(src: str, width="100%", height=315):
    """An extension of the video widget
    Arguments:
        src {str} -- A youtube url like https://www.youtube.com/embed/B2iAodr0fOo
    Keyword Arguments:
        width {str} -- The width of the video (default: {"100%"})
        height {int} -- The height of the video (default: {315})
    """
    st.write(
        f'<iframe width="{width}" height="{height}" src="{src}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )

def main():

    # Test/Title
    st.title('Learning the Streamlit')

    # Header/Subheader
    st.header("This is a header")
    st.subheader("This is a subheader")

    #text
    st.text("hello Streamlit")

    #Markdown
    st.markdown("### This is a Markdown")

    #Error/Colorful text
    st.success("Successful")

    st.info("Information!")

    st.warning('this is a warning')

    st.error("this is an error Danger")

    st.exception("NameError('name three not defined')")

    st.help(range)

    st.write("Text with write")

    st.write(range(10))

    # Images
    img = Image.open(urllib.request.urlopen("https://mms.businesswire.com/media/20200616005364/en/798639/22/Streamlit_Logo_%281%29.jpg"))
    st.image(img, width=300, caption="Simple Image")

    # Videos
    video_youtube("https://www.youtube.com/embed/B2iAodr0fOo")

    #widgets
    if st.checkbox("Show/hide"):
        st.text("Showing or Hiding Widget")

    # Radio
    status = st.radio("What is your status",("Active","Inactive"))
    if status == 'Active':
        st.success("You are Active")

    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        'Navigation',
        ('Home', 'About', 'Help')
    )

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)


##########################################################################
# @brief Entry point of the python
##########################################################################
if __name__ == '__main__':
    main()
