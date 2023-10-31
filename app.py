#!/usr/bin/env python
# coding: utf-8

# #### ![streamlit.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAASCSURBVGhD7Zi5axRRHMe/82Z2NfFWFLyvKMYLLQSvQkTExsZGQQubYCMSRETTBf8AQ0rBQlS008JGxELRxhNFCxUrtVATNR7RZHdm/X3nvSVjdq5NsjCG+cCw+46ded/3u96sVREwDlDm878nF5I1ciFZIxeSNXIhWSMXkjVyIWn5I5envzaUhgqhgAknTsDr6oKruxpGQ4W4167BmjkTTm8v8OyZ6W0MDRNS6ulB4f59MckEYPp0qIsXG2qVGiH9p0+j/Pu3aY0MvqnZZ88Cc+fqDsGaMweV7m5/bDS437+j7+VL0xqiRkjTvXtwVq1C6ejRET+0dOUK1OTJpmWwbThipcrz56ajPtzBQXgPH8J+8ADNAwOmd4gaIeW2NmD5chTevEFl4UK4nZ0ombE0eBIPxcePgWLR9AQQF8P583VlsTKvJ09g370LVZaW40AtW6YHA9S8s7PhLV0Ke+1a3fFHEujbtxhsb4dz7FhsUPkL7OiAmjXLb4fiefAkbiy5l2W6wmA8WS9eQH34AEyZIlsuT5alemINtWOHnhSgZl3+zQ8cAGg+amSwrlmD4vXrsJYsQeny5UiX865eheJD45AFKXGxEq0WAi3gvX4NdfMmlMQDpk3TIohsgjtvnv4+jNANtg4fBj59Mi2BgpqbYa1bh8K5c6iIMKbWoCD382c4US41HHGxArNYwBn4rSyWd27dgpJ7WUEBVX79glq50jT+JfTvIN+smzdrF7EiHODLF7gyps6cweDOnXBOnYI9e7YZTAF3VxKAe/w47HfvgFevYDc1+UkhFJlflnFn40bT8S+R/2u5Fy7AlouWiERuDhY77tyePQDN/uOH7o/agCD9/YBkSEhSSUSyVrm1FU7EZkUKoa+qxYuh1q/XrhUHx8Xsvj9v3ao/2WZ/kqBv34B9+3RMxuD+/Al71y7TqiU0RogjV2Xv3sQH+HCxrBtMjzduALdv6/6qNeM2gqI5f+rU6Hl0w/nzTSOcSCGkcvAg8PWraaWAgqrWkGQAKa5+8E+cqMfDFsrfiNswRlAohM8Rayi6YAyxQtSWLbLJsstxOxoGY4bFj24jKRmPHgGTJmlRYfdiipei5wf6cFeU+d6MGXASXDReCK9Dh3RRHAkUJIvAx4/ApUuAFDjfhaQ61wiiJSX1+p/BsVIJ7qJFphFN4r/xTMW2VHqw0sdPTYbWFTfBhg0A0ygzHPuqu814pAtx4SKA/WUpivbu3bGnABJrEcKsPrBtm77xaKEl6HJyjgNT+/v3gLyv+JbjJtHFnj7VbYqTILcWLEgUQRKFkMKRI0Bfn2mNAQxquhhftuhyPEXQBbn4oItJnXFbWsyP4kl0LeJX+tWrQ0+do4aPZwzSCtu3A0yzckTBihXwWMc2bTIT40llEbpXhUWLPs0HjuXFTMWMxhQtR3XI4dTPbmItV17G0pLKIoST3P374dy5M1QXGgGXI642cPIkivIulCY+SGohVRjy9bwYjQR6AE8W9VC3kKwiTjo+yIVkjVxI1siFZI1cSNbIhWSNcSIE+Av1IpficT+iFQAAAABJRU5ErkJggg==)  **Run streamlit code exists in the jupyter notebook** ![Jupyter.png](data:image/png;base64,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)
# ---
# 
# - 1) Write Streamlit code in jupyter Notebook.
# - 2) Run the below commands in the command prompt,
#     - jupyter nbconvert --to script Streamlit_Jupyter.ipynb  # convert jupyter notebook to script
#     - streamlit run app.py

# In[ ]:


# Import all the packages

import streamlit as st
import urllib.request
from PIL import Image
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


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


# In[ ]:


# @cache
@st.cache
def load_data():
    return pd.read_csv(
        "https://github.com/SurendraRedd/StreamlitProjects/raw/master/lang.csv"
    )


# In[ ]:


def main():

    # Test/Title
    st.title('StreamLit Concepts')

    # Header/Subheader
    st.header("To Create Header")
    st.subheader("To Create subheader")    

    st.subheader("Do you want to build the GUI using web app")
    st.code('pip install streamlit')

    #text
    st.text("hello Streamlit")

    html_temp = """
	<div style="background-color:tomato;padding:10px">
	<h2 style="color:white;text-align:center;">Streamlit ML App </h2>
	</div>

	"""
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown('<i class="material-icons">people</i>', unsafe_allow_html=True)
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.latex(r'''
    ...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    ...     \sum_{k=0}^{n-1} ar^k =
    ...     a \left(\frac{1-r^{n}}{1-r}\right)
    ...     ''')
    st.write(['st', 'is <', 3])
    st.write("✔️ Time up!")
    st.code('s="Happy" for i in range(0,10): print(s)')

    df1 = pd.DataFrame(
        np.random.randn(50, 5),
        columns=('col %d' % i for i in range(5)))
    my_table = st.table(df1)

    df = st.cache(pd.read_csv)("https://github.com/SurendraRedd/StreamlitProjects/raw/master/lang.csv")
    if is_check := st.checkbox("Display Data"):
        st.write(df)

    st.write('Dataframe example')
    st.dataframe(df1)

    #Markdown
    st.markdown("### This is a Markdown")

    st.markdown("### 🎲 Demo on streamlit")
    st.markdown("Streamlit python package is used to develop applications"
            "with out knowing much web application concepts.")
    st.markdown("**♟ Examples ♟**")
    st.markdown("* Happly learning!.")

    #Will be used for displaying the Error Messages in a colourful format
    st.success("Successful")
    st.info("Information!")
    st.warning('this is a warning')
    st.error("this is an error Danger")

    data = {'1':"True",'2':"True",'3':"False"}
    st.json(data)

    # Exception handling
    st.exception("IndexError('list out of index')")

    place_holder = st.empty()
    place_holder.text('Replaced!')

    #help of the function
    st.help(range)

    st.write("Text with write")

    st.write(range(10))

    st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
    st.area_chart({"data": [1, 5, 2, 6, 2, 1]})
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)
    st.pyplot(fig)

    '''
    # Markdown magic

    This is some _**text**_.
    '''

    df = pd.DataFrame({'col1': [1,2,3]})
    df  # <-- Draw the dataframe

    x = 10
    'x', x  # <-- Draw the string 'x' and then the value of x

    # Select box
    exp = st.selectbox("Select your experience: ", np.arange(1, 40, 1))

    # Slider
    exp = st.slider("Select your experience: ", min_value=1,   
                       max_value=40, value=1, step=1)

    # Multiselect
    movies = st.multiselect("Select Balayya Favourite movies?", 
                         ["SamaraSimhaReddy", "Simha",
                         "NarasimhaNaidu", "Legend"])


    # Will only run once if already cached
    df = load_data()
    st.write(df)


    st.button('Click')
    st.checkbox('Check the checkbox')
    st.radio('Radio Button',[1,2,3])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('slide',min_value=0, max_value=10)
    st.text_input('Enter Username')
    st.number_input('Enter a Number')
    st.text_area('Enter Text Here!')
    st.date_input('Date Input')
    st.time_input('Time entry')
    st.file_uploader('File Uploader')
    st.beta_color_picker('Select color')

    st.echo()
    with st.echo():
        text = 's="Happy Learning!" for i in range(0,10): print(s)'
        st.write(text)


    #Image opening
    #img = Image.open("download.jfif") #open the image stored in specified location
    img = Image.open(urllib.request.urlopen("https://github.com/SurendraRedd/ChallengeDeploy/raw/main/singlefile/Solution.png")) # Opens the image from the url
    #response = requests.get("https://github.com/SurendraRedd/Techgig/blob/main/images/Solution.png")
    #img = Image.open(BytesIO(response.content))
    #img = Image.open(urllib.request.urlopen("https://github.com/SurendraRedd/Techgig/blob/main/images/Solution.png"))
    st.image(img, width=300, caption="Simple Image")

    # Video playing
    vid_file = open("sample-mp4-file.mp4","rb").read() #play the video stored in specified location
    st.video(vid_file)
    #videoUserDefined("https://www.youtube.com/embed/B2iAodr0fOo")

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

    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')

    st.balloons()

    st.write('Happy Stream Lite App Learning')


# In[ ]:


main()

