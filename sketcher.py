import streamlit as st
import cv2
from PIL import Image
import numpy as np


# Sketch dodge function
def dodgeV2(x,y):
	"""
	parameters : x, y
	"""
	return cv2.divide(x, 255 - y, scale=256)

# Convert the image in a sketch
def imageConversion(inputImage):
	"""
	parameters : image
	"""
	grayScaleImg = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
	invertImg = cv2.bitwise_not(grayScaleImg)
	smoothImg = cv2.GaussianBlur(invertImg, (21,21),sigmaX=0, sigmaY=0)
	finalImg = dodgeV2(grayScaleImg,smoothImg)
	return finalImg

def main():
	# Documentation - Main Function to process
	# Title of the web page
    st.title("Convert an image in to pencil sketch")
    st.subheader("This application has options to select the image either from sidebar or in mainpage.")
    html_temp = """
	    <body style="background-color:red;">
	    <div style="background-color:teal ;padding:10px">
	    <h2 style="color:white;text-align:center;">Image to Pencil Sketch App</h2>
	    </div>
	    </body>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("-----------------------------------------------------------------------")
    st.write("""
	    ## Packages:
	    - Streamlit, Opencv, Pillow & numpy
	    - How to install? 
	    > 1. **pip install streamlit**
	    > 2. **pip install opencv-python**
	    > 3. **pip install numpy**
	    > 4. **pip install Pillow**
    """)
    st.write("-----------------------------------------------------------------------")

    # To avoid the deprecation warning while using the file uploader
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Selection box
    image_option = st.sidebar.selectbox(
        'Image Option',
        ('None','Sidebar', 'Mainpage')
    )

    # Side bar Selection
    if image_option == 'Sidebar':
        input_sidebar_image = st.sidebar.file_uploader("Select an image file", type=['jpeg','jpg','png'])
        if input_sidebar_image is None:
        	pass
        	#st.error("Select the image to proceed!")
        else:
           	st.write("**Side bar Image selected is **")
           	st.image(input_sidebar_image,use_column_width=True)
           	input_img = Image.open(input_sidebar_image)
           	skecthImage = imageConversion(np.array(input_img))
           	st.write("**Skecthed Image is **")
           	st.image(skecthImage,use_column_width=True)

    elif image_option == 'Mainpage':
        input_image = st.file_uploader("Select an image file to process", type=['jpeg','jpg','png'])
        if input_image is None:
        	pass
           	#st.error("Select the image to proceed!")
        else:
           	st.write("**Main page Image selected is **")
           	st.image(input_image,use_column_width=True)
           	input_img = Image.open(input_image)
           	skecthImage = imageConversion(np.array(input_img))
           	st.write("**Skecthed Image is **")
           	st.image(skecthImage,use_column_width=True)
    else:
        pass  

    st.sidebar.title("Tip - Run app directly from GitHubLink")
    st.sidebar.info(""" streamlit run 
    	https://github.com/SurendraRedd/
    	StreamlitProjects/blob/master
    	/sketcher.py
    	""")
    st.sidebar.title("Logic")
    st.sidebar.info(""" 
    	- Convert the color image to grayscale - ```gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)```
    	- Invert the grayscale image to get a negative - ```imagem = cv2.bitwise_not(imagem)```
    	- Apply a Gaussian blur to the negative from step 2 - ```blur = cv.GaussianBlur()```
    	- Blend the grayscale image from step 1 with the blurred negative from step 3 using a color dodge - ```dodgeV2(mg_gray, img_blur)``` 
    	> [Sketch Reference](https://www.askaswiss.com/2016/01/how-to-create-pencil-sketch-opencv-python.html)
    """)
    st.sidebar.title("About")
    st.sidebar.info("**App version 1.0**")

    if st.checkbox("ShowDemo?"):
      	st.video(open("Demo.mp4","rb").read())    	

    if st.checkbox("Show source code? "):
        st.code(open("./sketcher.py", encoding="utf-8").read())

    st.info("""
    	[GitHubLink](https://github.com/SurendraRedd/StreamlitProjects/blob/master/sketcher.py)
    """)

if __name__ == '__main__':
    main()