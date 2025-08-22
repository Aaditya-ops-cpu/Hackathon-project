Explainable Credit Scorecard

This project is a prototype for a credit intelligence system that is both real time and explainable. The purpose is to calculate a creditworthiness score for a company and provide clear reasons for why the score was assigned.

The project has the following flow:

The data pipeline collects structured data and event data. For example stock market information is taken from Yahoo Finance, macroeconomic indicators are added in a simple table and event information is simulated with news sentences.

The preprocessing module creates features such as returns from stock data and merges them with macroeconomic information.

The model module trains a decision tree classifier. This choice is made because the model is simple and can be explained. The model predicts a label that shows if a company is good or risky.

The explainability module uses SHAP to calculate how each feature contributes to the model prediction. These explanations are stored and later shown to the analyst.

The dashboard displays the accuracy of the model, the feature explanations for each test case and the impact of unstructured events. For example if the event mentions debt restructuring then the company is considered more risky.