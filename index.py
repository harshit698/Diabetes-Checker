from flask import Flask,request, render_template
import pickle
import os
import numpy as np 

app = Flask(__name__,static_url_path='/static', static_folder='static')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/getresult',methods=['POST','GET'])
def getresult():
	if request.method =='POST':

		#preparing feature vector for prediction
		new_vector = np.zeros(6)
		a1 =int( request.form['Glucose'])
		a2 = int (request.form['BloodPressure'])
		a3 =int( request.form['Insulin'])
		a4 = int( request.form['BMI'])
		a5 =int( request.form['DPF'])
		a6 = int(request.form['Age'])

		new_vector=[[a1,a2,a3,a4,a5,a6]]
		print(new_vector)


		# model_file = os.open('diabetes_model.sav',os.O_RDONLY)
		# logmodel = pickle.load(model_file)
		with open('diabetes_model1.sav', 'rb') as pickle_file:
			logmodel = pickle.load(pickle_file)
			print(logmodel)
		prediction = logmodel.predict(new_vector)
		print("Yhan phucha")
		return render_template('result.html',prediction=prediction)

if __name__ == '__main__':
	app.run()
