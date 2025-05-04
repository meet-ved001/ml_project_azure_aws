from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            
            pred_df = data.get_data_as_data_frame()
            print("Received data:", pred_df)  # Debug print
            
            predict_pipeline = PredictPipeline()
            math_score, category = predict_pipeline.predict(pred_df)
            
            # Map numerical categories to descriptive messages
            category_messages = {
                0: "Excellent performance! The student is performing exceptionally well.",
                1: "Good performance! The student is doing well.",
                2: "Average performance. The student is meeting expectations.",
                3: "Below average performance. The student might need some additional support.",
                4: "The student needs additional support to improve their performance."
            }
            
            confidence_scores = {
                0: "95-100%",
                1: "85-94%",
                2: "75-84%",
                3: "65-74%",
                4: "Below 65%"
            }
            
            return render_template('home.html', 
                                results=category_messages[category],
                                confidence=confidence_scores[category],
                                math_score=f"{math_score:.1f}")
            
        except Exception as e:
            print("Error:", str(e))  # Debug print
            return render_template('home.html', 
                                results=f"Error: {str(e)}",
                                confidence="N/A",
                                math_score="N/A")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    