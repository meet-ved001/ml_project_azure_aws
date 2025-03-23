import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
import os 

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    def get_data_transformer_object(self):
        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course']
            
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),#fill missing values with median
                    ('std_scaler', StandardScaler())#standard scaling
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),#fill missing values with most frequent value
                    ('one_hot_encoder', OneHotEncoder()),#one hot encoding
                    ('std_scaler', StandardScaler(with_mean=False))#standard scaling
                ]
            )

            logging.info("Numerical columns standard scaling pipeline created")

            logging.info("Categorical columns standard scaling pipeline created")

            preprocessor = ColumnTransformer(#column transformer helps to apply different transformations to different columns
                #  such as numerical and categorical columns
                [
                    ('num_pipeline', num_pipeline, numerical_columns),
                    ('cat_pipeline', cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
             raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_data_path,test_data_path):
        logging.info("Entered the data transformation method or component")
        try:
            train_data = pd.read_csv(train_data_path)
            test_data = pd.read_csv(test_data_path)

            logging.info("Read the train and test data as dataframes")
            logging.info("Creating a preprocessor object")

            preprocessor_obj = self.get_data_transformer_object()
            target_col_name = 'math_score'
            numerical_columns = ['writing_score','reading_score']

            input_feature_train_df = train_data.drop(columns = [target_col_name],axis=1)
            target_feature_train_df = train_data[target_col_name]

            input_feature_test_df = test_data.drop(columns=[target_col_name],axis=1)
            target_feature_test_df = test_data[target_col_name]

            logging.info("Split the train and test data into input and target features for train and test datasets")

            input_feature_train_arr= preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]  
            logging.info("Data transformation is completed")
            
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file,
                obj = preprocessor_obj
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file
            )
        except Exception as e:
            raise CustomException(e,sys)


