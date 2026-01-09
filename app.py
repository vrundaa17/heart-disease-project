from flask import Flask,render_template,request
import pickle
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__),'models')

with open(os.path.join(MODEL_PATH,'pipe.pkl'),'rb') as f :
    pipe = pickle.load(f)



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyse',methods=['POST'])
def analysis():
    Age = request.form.get('age')
    Sex = request.form.get('gender')
    ChestPainType = request.form.get('ChestPainType')
    Cholesterol= request.form.get('Cholesterol')
    MaxHR = request.form.get('MaxHR')
    ST_Slope= request.form.get('ST_Slope')
    ExerciseAngina = request.form.get('ExerciseAngina')

    Age = int(Age)
    Cholesterol = int(Cholesterol)
    MaxHR = int(MaxHR)
    temp_df = pd.DataFrame({'Age':[Age],'Sex':[Sex],'ChestPainType' :[ChestPainType], 'Cholesterol':[Cholesterol],
                            'MaxHR':[MaxHR],'ST_Slope':[ST_Slope],'ExerciseAngina':[ExerciseAngina]})
    print(temp_df)

    result = pipe.predict(temp_df)
    data = ''
    if result==0:
        data = 'No Heart Disease. You are safe. Take Care!'
    else :
        data ='You have a Heart Disease. Take Care!'
        
        
    def report():
        analysis = []
        if Age >= 50:
            analysis.append(("Age", "Age is a moderate risk factor as heart disease risk increases with age."))
        else:
            analysis.append(("Age", "Age is within a lower risk range."))
            
        if ChestPainType in ['TA', 'ASY']:
            analysis.append(("Chest Pain", "The selected chest pain type is strongly associated with heart disease."))
        else:
            analysis.append(("Chest Pain", "The chest pain type is less commonly linked to heart disease."))

        if ExerciseAngina == 'Y':
            analysis.append(("Exercise Angina", "Exercise-induced angina significantly increases heart risk."))
        else:
            analysis.append(("Exercise Angina", "No exercise-induced angina was reported."))

        if Cholesterol > 240:
            analysis.append(("Cholesterol", "Cholesterol levels are higher than recommended."))
        else:
            analysis.append(("Cholesterol", "Cholesterol levels are within an acceptable range."))

        if MaxHR < 120:
            analysis.append(("Max Heart Rate", "Lower maximum heart rate may indicate reduced cardiac efficiency."))
        else:
            analysis.append(("Max Heart Rate", "Maximum heart rate is within a healthy range."))
        return analysis
    report= report()
    return render_template('index.html',data=data,report=report)

if __name__ == '__main__' :
    app.run(debug=True)
    
    
    


