import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import urllib.request
from PIL import Image
#import yfinance as yf

html_temp = """
    <body style="background-color:red;">
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Classifier(SL) - Iris Flower Prediction App</h2>
    </div>
    </body>
"""

st.beta_set_page_config(
        page_title = 'Iris',
        page_icon = "🌺",
        layout = "centered",
        initial_sidebar_state = "expanded"
    )

def inputFeatures():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    return pd.DataFrame(data, index=[0])

def main():
	st.markdown(html_temp, unsafe_allow_html=True)
	st.sidebar.info("""
	    ## Packages:
	    - Streamlit, pandas & sklearn
	    - How to install? 
	    > 1. **pip install streamlit**
	    > 2. **pip install pandas**
	    > 3. **pip install scikit-learn**
    	""")
	st.sidebar.header('Input Features')
	df = inputFeatures()

	st.sidebar.info("#### Iris Flower species : setosa, versicolor, virginica")
	img = Image.open(urllib.request.urlopen("https://raw.githubusercontent.com/SurendraRedd/MachineLearningCode/master/Iris_Species.png")) # Opens the image from the url
	st.sidebar.image(img, width=300, caption="")
	st.sidebar.info("#### Features : setosa, versicolor, virginica")
	img = Image.open(urllib.request.urlopen("https://raw.githubusercontent.com/SurendraRedd/MachineLearningCode/master/features.png")) # Opens the image from the url
	st.sidebar.image(img, width=400, caption="")

	st.subheader('Input Features')
	st.write(df)

	iris = datasets.load_iris()
	X = iris.data
	Y = iris.target

	clf = RandomForestClassifier()
	clf.fit(X, Y)

	prediction = clf.predict(df)
	prediction_proba = clf.predict_proba(df)

	st.subheader('labels & index number')
	st.write(iris.target_names)

	st.subheader('Prediction')
	st.write(iris.target_names[prediction])
	#st.write(prediction)

	st.subheader('Prediction Probability')
	st.write(prediction_proba)

	st.write("""
	# Simple Stock Price App
	Shown are the stock closing price and volume of Google!
	""")

	# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
	#define the ticker symbol
	tickerSymbol = 'GOOGL'
	#get data on this ticker
	tickerData = yf.Ticker(tickerSymbol)
	#get the historical prices for this ticker
	tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
	# Open	High	Low	Close	Volume	Dividends	Stock Splits

	st.line_chart(tickerDf.Close)
	st.line_chart(tickerDf.Volume)


if __name__ == '__main__':
	main()