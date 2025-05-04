import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path = "artifacts/model.pkl"
            preprocessor_path = "artifacts/preprocessor.pkl"
            print("Loading model and preprocessor...")  # Debug print
            model = load_object(file_path = model_path)#load the model
            preprocessor = load_object(file_path = preprocessor_path)
            
            print("Input features before preprocessing:", features)  # Debug print
            data_scaled = preprocessor.transform(features)#scale the input data
            print("Features after preprocessing:", data_scaled)  # Debug print
            
            preds = model.predict(data_scaled)
            print("Raw model predictions (math scores):", preds)  # Debug print
            
            # Convert math score predictions to performance categories
            prediction_categories = []
            for pred in preds:
                if pred >= 90:
                    prediction_categories.append(0)  # Excellent
                elif pred >= 80:
                    prediction_categories.append(1)  # Good
                elif pred >= 70:
                    prediction_categories.append(2)  # Average
                elif pred >= 60:
                    prediction_categories.append(3)  # Below Average
                else:
                    prediction_categories.append(4)  # Needs Support
            
            return preds[0], prediction_categories[0]  # Return both raw score and category
        except Exception as e:
            print("Error in prediction:", str(e))  # Debug print
            raise CustomException(e,sys)
class CustomData:#class to store the input data
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score   

    def get_data_as_data_frame(self):#converts the input data to a pandas dataframe
        try:
            custom_data_input_dict = {
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
        