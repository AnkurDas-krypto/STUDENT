import sys
import pandas as pd
from dataclasses import dataclass
import os
import pickle
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.student.utils.common import save_object
from src.student.entity import DataTransformationConfig
class DataTransformation:
    def __init__(self,config = DataTransformationConfig):
        self.config = config

    def get_data_transformation(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]

            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self):
        try:
            data_path = self.config.data_path
            train_csv_path = os.path.join(data_path, 'train.csv')
            test_csv_path = os.path.join(data_path, 'test.csv')
            train_df = pd.read_csv(train_csv_path)
            test_df = pd.read_csv(test_csv_path)
            preprocessing_obj = self.get_data_transformation()
            
            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(file_path= self.config.preprocessor_path, obj= preprocessing_obj)

            train_arr_csv_path = os.path.join(self.config.root_dir, 'train_arr.csv')
            test_arr_csv_path = os.path.join(self.config.root_dir, 'test_arr.csv')

            np.savetxt(train_arr_csv_path, train_arr, delimiter=',')
            np.savetxt(test_arr_csv_path, test_arr, delimiter=',')
            logging.info("train, test and preprocessor obj saved")
        except Exception as e:
            raise CustomException(e, sys)
        