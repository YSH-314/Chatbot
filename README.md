# chatbot in Mandarin 
This project was built on Telegram API and used Python as programming language
## Including Topics: Sentimental classification/ NLP/ Question and Answer/ ML
## Follow the following steps to build a chatbot on Telegram:
1. Create a Telegram account，ask for "BotFather" creating a chat bot (commend: /newbot)
2. You will get a token to access the HTTP API. Copy the token and paste in the line 25 of the file: telegram_conversation.py
3. Create a python 3.6 environment and install scikit-learn 0.19.1, jieba, BeautifulSoup4, html5lib, python-telegram-bot, tqdm, pandas, numpy, and scipy. Download the word vector from https://mega.nz/#!5LwDjZia!f77y-eWm90H3akg8mD9CqhOZ89NihirRKN4IT1SJ01Q.
4. Run the telegram_conversation.py

## Build sentimental model
1. Call function from all_deffunction_5.py
2. Use Positive01.txt and Negative01.txt as training data
3. Read sentence and remove stop words (as in stop_words.txt)
4. Lable token as positive or negative
5. Build Naive Bayes Classifier
6. Save model as MNB_model.pkl

## Other files
1. UNRB02.txt: Irrational beliefs (categorized by Albert Ellis)
2. reject02.txt: Refutation of irrational beliefs
3. TAKE_Key.txt: Dialog number
4. TAKE_Value: Contents of dialog

To be continue...
