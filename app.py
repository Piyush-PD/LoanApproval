
import pickle
import pandas as pd
import numpy
from flask import Flask, render_template, request
import numpy as np

# Load the Random Forest CLassifier model

classifier = pickle.load(open( 'AdaboostModel.pkl', 'rb'))

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/Predict', methods=['POST'])
def Predict():
        marriage = int(request.form['Married'])
        edu = int(request.form['Graduated'])
        Loan = int(request.form['LoanPending']) #the values from the form created
        final_features =np.array([[marriage,edu,Loan]])
        prediction = classifier.predict(final_features)
        
        if prediction==1:
            return render_template('index.html', prediction="Nice .. U r eligible for loan Nigga")
        else:
            return render_template('index.html', prediction="U r an Asshole Get lost")
             
        


# It is called terminated extension
if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




