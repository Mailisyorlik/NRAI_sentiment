import streamlit as st
import webbrowser


import spacy
from textblob import TextBlob

# webbrowser.open('https://www.python.org')
url = 'http://trutthit.com/'

def text_analyzer(my_text):
	nlp = spacy.load('en')
	docx = nlp(my_text)

	tokens = [token.text for token in docx]
	allData = [('"Tokens":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in docx]
	return allData

def entity_analyzer(my_text):
	nlp = spacy.load('en')
	docx = nlp(my_text)
	tokens = [token.text for token in docx]
	entities = [(entity.text,entity.label_) for entity in docx.ents ]
	allData = ['"Tokens":{},\n"Entities":{}'.format(tokens,entities)]
	return allData
	
def main():

	st.title("NewsRealAI")
	st.subheader("Try for a 100%, which implies you are being both objective and neutral”") 
	
	if st.checkbox("Show Score"):
		st.subheader("Sentiment of Your Text")
		message = st.text_area("Enter Your Text",)
		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			a,b = result_sentiment
			i = ''.join(map(str,result_sentiment))
			final_score = (1-(abs(a)))
			score = "{0:.1f}%".format(final_score * 100)
			st.success(score)

	if st.button("TrutthIt Home"):
   		webbrowser.open_new_tab(url)


if __name__ == '__main__':
	main()