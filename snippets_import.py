import json
import os
import subprocess

snippets = [
    {
        "display_name": "Import common packages",
        "metadata": {
            "tags": ["J.COp Snippets"],
            "display_name": "Import common packages",
            "code": [
                "import numpy as np",
                "import pandas as pd",
                "",
                "from sklearn.model_selection import train_test_split",
                "from sklearn.pipeline import Pipeline",
                "from sklearn.compose import ColumnTransformer",
                "",
                "from jcopml.pipeline import num_pipe, cat_pipe",
                "from jcopml.utils import save_model, load_model",
                "from jcopml.plot import plot_missing_value",
                "from jcopml.feature_importance import mean_score_decrease"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Import csv data",
        "metadata": {
            "tags": ["J.COp Snippets"],
            "display_name": "Import csv data",
            "code": [
                "df = pd.read_csv(\"____________\", index_col=\"___________\", parse_dates=[\"____________\"])",
                "df.head()"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Dataset Splitting - Shuffle Split",
        "metadata": {
            "tags": ["Dataset Splitting"],
            "display_name": "Dataset Splitting - Shuffle Split",
            "code": [
                "X = df.drop(columns=\"___________\")",
                "y = \"_____________\"",
                "",
                "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
                "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Dataset Splitting - Stratified Shuffle Split",
        "metadata": {
            "tags": ["Dataset Splitting"],
            "display_name": "Dataset Splitting - Stratified Shuffle Split",
            "code": [
                "X = df.drop(columns=\"___________\")",
                "y = \"_____________\"",
                "",
                "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)",
                "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Preprocessor - Common",
        "metadata": {
            "tags": ["Preprocessor"],
            "display_name": "Preprocessor - Common",
            "code": [
                "preprocessor = ColumnTransformer([",
                "    ('numeric', num_pipe(), [\"______________\"]),",
                "    ('categoric', cat_pipe(encoder='onehot'), [\"_____________\"]),",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Preprocessor - Advance example",
        "metadata": {
            "tags": ["Preprocessor"],
            "display_name": "Preprocessor - Advance example",
            "code": [
                "# Note: You could not use gsp, rsp, and bsp recommendation in advance mode",
                "# You should specify your own parameter grid / interval when tuning",
                "preprocessor = ColumnTransformer([",
                "    ('numeric1', num_pipe(impute='mean', poly=2, scaling='standard', transform='yeo-johnson'), [\"______________\"]),",
                "    ('numeric2', num_pipe(impute='median', poly=2, scaling='robust'), [\"______________\"]),",
                "    ('categoric1', cat_pipe(encoder='ordinal'), [\"_____________\"]),",
                "    ('categoric2', cat_pipe(encoder='onehot'), [\"_____________\"])    ",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Regression - K-Nearest Neighbor (KNN)",
        "metadata": {
            "tags": ["Regression"],
            "display_name": "Regression - K-Nearest Neighbor (KNN)",
            "code": [
                "from sklearn.neighbors import KNeighborsRegressor",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', KNeighborsRegressor())",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Regression - Support Vector Machine (SVM)",
        "metadata": {
            "tags": ["Regression"],
            "display_name": "Regression - Support Vector Machine (SVM)",
            "code": [
                "from sklearn.svm import SVR",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', SVR(max_iter=500))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Regression - Random Forest (RF)",
        "metadata": {
            "tags": ["Regression"],
            "display_name": "Regression - Random Forest (RF)",
            "code": [
                "from sklearn.ensemble import RandomForestRegressor",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', RandomForestRegressor(n_jobs=-1, random_state=42))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Regression - Extreme Gradient Boosting (XGBoost)",
        "metadata": {
            "tags": ["Regression"],
            "display_name": "Regression - Extreme Gradient Boosting (XGBoost)",
            "code": [
                "from xgboost import XGBRegressor",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', XGBRegressor(n_jobs=-1, random_state=42))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Regression - Linear Regression",
        "metadata": {
            "tags": ["Regression"],
            "display_name": "Regression - Linear Regression",
            "code": [
                "from sklearn.linear_model import LinearRegression",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', LinearRegression())",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Regression - ElasticNet Regression",
        "metadata": {
            "tags": ["Regression"],
            "display_name": "Regression - ElasticNet Regression",
            "code": [
                "from sklearn.linear_model import ElasticNet",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', ElasticNet())",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Classification - K-Nearest Neighbor (KNN)",
        "metadata": {
            "tags": ["Classification"],
            "display_name": "Classification - K-Nearest Neighbor (KNN)",
            "code": [
                "from sklearn.neighbors import KNeighborsClassifier",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', KNeighborsClassifier())",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Classification - Support Vector Machine (SVM)",
        "metadata": {
            "tags": ["Classification"],
            "display_name": "Classification - Support Vector Machine (SVM)",
            "code": [
                "from sklearn.svm import SVC",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', SVC(max_iter=500))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Classification - Random Forest (RF)",
        "metadata": {
            "tags": ["Classification"],
            "display_name": "Classification - Random Forest (RF)",
            "code": [
                "from sklearn.ensemble import RandomForestClassifier",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', RandomForestClassifier(n_jobs=-1, random_state=42))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Classification - Extreme Gradient Boosting (XGBoost)",
        "metadata": {
            "tags": ["Classification"],
            "display_name": "Classification - Extreme Gradient Boosting (XGBoost)",
            "code": [
                "from xgboost import XGBClassifier",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', XGBClassifier(n_jobs=-1, random_state=42))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Classification - Logistic Regression",
        "metadata": {
            "tags": ["Classification"],
            "display_name": "Classification - Logistic Regression",
            "code": [
                "from sklearn.linear_model import LogisticRegression",
                "pipeline = Pipeline([",
                "    ('prep', preprocessor),",
                "    ('algo', LogisticRegression(solver='lbfgs', n_jobs=-1, random_state=42))",
                "])"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Hyperparameter Tuning - Grid Search",
        "metadata": {
            "tags": ["Hyperparameter Tuning"],
            "display_name": "Hyperparameter Tuning - Grid Search",
            "code": [
                "from sklearn.model_selection import GridSearchCV",
                "from jcopml.tuning import grid_search_params as gsp",
                "",
                "model = GridSearchCV(pipeline, gsp.\"_______________\", cv=\"___\", scoring='___', n_jobs=-1, verbose=1)",
                "model.fit(X_train, y_train)",
                "",
                "print(model.best_params_)",
                "print(model.score(X_train, y_train), model.best_score_, model.score(X_test, y_test))"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Hyperparameter Tuning - Randomized Search",
        "metadata": {
            "tags": ["Hyperparameter Tuning"],
            "display_name": "Hyperparameter Tuning - Randomized Search",
            "code": [
                "from sklearn.model_selection import RandomizedSearchCV",
                "from jcopml.tuning import random_search_params as rsp",
                "",
                "model = RandomizedSearchCV(pipeline, rsp.\"_______________\", cv=\"___\", scoring='___', n_iter=\"___\", n_jobs=-1, verbose=1, random_state=42)",
                "model.fit(X_train, y_train)",
                "",
                "print(model.best_params_)",
                "print(model.score(X_train, y_train), model.best_score_, model.score(X_test, y_test))"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Hyperparameter Tuning - Bayesian Search",
        "metadata": {
            "tags": ["Hyperparameter Tuning"],
            "display_name": "Hyperparameter Tuning - Bayesian Search",
            "code": [
                "from jcopml.tuning.skopt import BayesSearchCV",
                "from jcopml.tuning import bayes_search_params as bsp",
                "",
                "model = BayesSearchCV(pipeline, bsp.\"_______________\", cv=\"___\", scoring=\"__\", n_iter=\"___\", n_jobs=-1, verbose=1, random_state=42)",
                "model.fit(X_train, y_train)",
                "",
                "print(model.best_params_)",
                "print(model.score(X_train, y_train), model.best_score_, model.score(X_test, y_test))"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Save model - Save the whole search object",
        "metadata": {
            "tags": ["Save model"],
            "display_name": "Save model - Save the whole search object",
            "code": [
                "save_model(model, \"__________.pkl\")"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    },
    {
        "display_name": "Save model - Save best estimator only",
        "metadata": {
            "tags": ["Save model"],
            "display_name": "Save model - Save best estimator only",
            "code": [
                "save_model(model.best_estimator_, \"__________.pkl\")"
            ],
            "language": "Python"
        },
        "schema_name": "code-snippet"
    }
]

try:
    # Mendapatkan direktori data jupyter secara dinamis
    jupyter_data_dir = subprocess.check_output(['jupyter', '--data-dir']).decode('utf-8').strip()
    
    # Membuat path spesifik ke metadata/code-snippets
    output_dir = os.path.join(jupyter_data_dir, "metadata", "code-snippets")
    os.makedirs(output_dir, exist_ok=True)

    for snippet in snippets:
        # Memformat nama file
        filename = snippet["display_name"].replace(" - ", "_").replace(" ", "_").replace("(", "").replace(")", "").lower() + ".json"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(snippet, f, indent=4)

    print(f"\nBerhasil! {len(snippets)} file JSON snippet telah tersimpan di:")
    print(f"{output_dir}")
    print("\nSilakan refresh/muat ulang JupyterLab Anda untuk melihat snippet yang baru ditambahkan.")

except Exception as e:
    print(f"Terjadi kesalahan saat mencari direktori Jupyter atau menyimpan file: {e}")