#!/usr/bin/env python
# coding: utf-8

# In[28]:


from flask import Flask,request,jsonify
import pickle
import pandas as pd
import numpy


# In[31]:


from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'FinalAdaboostModel.pkl'
classifier = pickle.load(open(filename, 'rb'))

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/Predict', methods=['POST'])
def Predict():
        int_features = [int(x) for x in request.form.values()] #to get the values from the form created
        final_features = [np.array(int_features)]
        prediction = classifier.predict(final_features)
        
        if prediction==1:
            return render_template('index.html', predict="Nice .. U r eligible for loan Nigga")
        else:
            return render_template('index.html', predict="U r an Asshole Get lost")
             
        


# It is called terminated extension
if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




