#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.simplefilter('ignore')
from textblob import TextBlob


# In[2]:


from flask import Flask, request, render_template


# In[3]:


sent_pred = Flask(__name__)


# In[4]:


@sent_pred.route('/')
def home():
    return render_template('index.html')


# In[5]:


def func(arg):
    b = TextBlob(str(arg))
    if b.polarity>0:
        return 'Positive Sentiment'
    elif b.polarity<0:
        return 'Negative Sentiment'
    else:
        return 'Neutral Sentiment'


# In[6]:


@sent_pred.route('/predict_sentiment', methods=['POST'])
def predict():
    a = str(request.form.values())    
    pred = func(a)
    output = str(pred)
    return render_template('index.html',prediction_text='Sentiment type: {}'.format(output))


# In[7]:


if __name__=='__main__':
    sent_pred.run(debug=True, use_reloader = False)

