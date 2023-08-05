import pandas as pd
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
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import os
from src.student.utils.common import evaluate_models, save_object
from src.exception import CustomException
from src.logger import logging
import sys
from src.student.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config = ModelTrainerConfig):
        self.config = config
    
    def initiate_model_trainer(self):
        try:
            data_path = self.config.train_arr
            train_csv_path = os.path.join(data_path, 'train_arr.csv')
            test_csv_path = os.path.join(data_path, 'test_arr.csv')
            train_array = pd.read_csv(train_csv_path).to_numpy()
            test_array = pd.read_csv(test_csv_path).to_numpy()

            X_train,y_train,X_test,y_test=(
                        train_array[:,:-1],
                        train_array[:,-1],
                        test_array[:,:-1],
                        test_array[:,-1]
                    )
            logging.info("data splitted into X_train, X_test, y_train and y_test")
            models = {
                        "Random Forest": RandomForestRegressor(),
                        "Decision Tree": DecisionTreeRegressor(),
                        "Gradient Boosting": GradientBoostingRegressor(),
                        "Linear Regression": LinearRegression(),
                        "XGBRegressor": XGBRegressor(),
                        "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                        "AdaBoost Regressor": AdaBoostRegressor(),
                    }
            params={
                        "Decision Tree": {
                            'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                            # 'splitter':['best','random'],
                            # 'max_features':['sqrt','log2'],
                        },
                        "Random Forest":{
                            # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                        
                            # 'max_features':['sqrt','log2',None],
                            'n_estimators': [8,16,32,64,128,256]
                        },
                        "Gradient Boosting":{
                            # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                            'learning_rate':[.1,.01,.05,.001],
                            'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                            # 'criterion':['squared_error', 'friedman_mse'],
                            # 'max_features':['auto','sqrt','log2'],
                            'n_estimators': [8,16,32,64,128,256]
                        },
                        "Linear Regression":{},
                        "XGBRegressor":{
                            'learning_rate':[.1,.01,.05,.001],
                            'n_estimators': [8,16,32,64,128,256]
                        },
                        "CatBoosting Regressor":{
                            'depth': [6,8,10],
                            'learning_rate': [0.01, 0.05, 0.1],
                            'iterations': [30, 50, 100]
                        },
                        "AdaBoost Regressor":{
                            'learning_rate':[.1,.01,0.5,.001],
                            # 'loss':['linear','square','exponential'],
                            'n_estimators': [8,16,32,64,128,256]
                        }
                        
                    }
            
            model_report:dict= evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                                    models=models,param=params)
            
            logging.info("model evaluation done")
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                        raise ("No best model")
            logging.info(f"best model is {best_model}")
            save_object(file_path= self.config.model_path, obj= best_model)

            predicted = best_model.predict(X_test)
            r2_square = r2_score(predicted, y_test)
            logging.info(f"best model is {best_model} and score is {r2_square}")
            return r2_square
        
    
        except Exception as e:
            raise CustomException(e, sys)

        