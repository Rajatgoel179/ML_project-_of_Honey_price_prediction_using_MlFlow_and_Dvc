from flask import Flask, render_template, request
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Global constant for state dictionary
STATE_DICTIONARY = {'AL': 0, 'AR': 1, 'AZ': 2, 'CA': 3, 'CO': 4, 'FL': 5, 'GA': 6, 'HI': 7, 'IA': 8, 'ID': 9, 'IL': 10, 'IN': 11,
                   'KS': 12, 'KY': 13, 'LA': 14, 'MD': 15, 'ME': 16, 'MI': 17, 'MN': 18, 'MO': 19, 'MS': 20, 'MT': 21, 'NC': 22,
                   'ND': 23, 'NE': 24, 'NJ': 25, 'NM': 26, 'NV': 27, 'NY': 28, 'OH': 29, 'OK': 30, 'OR': 31, 'PA': 32, 'SC': 33,
                   'SD': 34, 'TN': 35, 'TX': 36, 'UT': 37, 'VA': 38, 'VT': 39, 'WA': 40, 'WI': 41, 'WV': 42, 'WY': 43}

@app.route('/', methods=['GET'])
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
def index():
    if request.method == "POST":
        try:
            state = request.form['state']
            
            state= STATE_DICTIONARY[state]
              
            num_col = float(request.form['numcol'])
            yield_per_col = int(request.form['yieldpercol'])
            total_prod = float(request.form['totalprod'])
            stocks = float(request.form['stocks'])
            prod_value = float(request.form['prodvalue'])
            year = int(request.form['year'])
        except Exception as e:
            print('The Exception message is:', e)
            return 'Something went wrong'
 
    else:
        return render_template("index.html")

    data = [state, num_col, yield_per_col, total_prod, stocks, prod_value, year]
    data = np.array(data).reshape(1, 7)

    obj = PredictionPipeline()
    predict = obj.predict(data)[0]

    return render_template('index.html', prediction = f' Honey price per pound is ${round(predict,2)}')

    
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(debug=True)

