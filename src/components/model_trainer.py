import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        #initialize the model trainer config
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "AdaBoost": AdaBoostRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XGBoost": XGBRegressor(),
                "KNN": KNeighborsRegressor(),
                "CatBoost": CatBoostRegressor(verbose=False)
            }
            model_report: dict = evaluate_models( X_train=X_train,
                y_train=y_train ,
                X_test = X_test,
                y_test=y_test,
                models=models)
            # Find the best model based on test_model_score
            best_model_name, best_model_info = max(model_report.items(), key=lambda x: x[1]["test_model_score"])
            best_model_score = best_model_info["test_model_score"]
            best_model = models[best_model_name]  # Get the best model

            if best_model_score<0.6:
                raise CustomException("Best model score is less than 0.6",sys)
            
            logging.info("Model evaluation completed")
            logging.info("Best model found on both training and testing dataset")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test,predicted)
            print("Best model found is",best_model_name)
            return r2
        
        except Exception as e:
            raise CustomException(e,sys)
        