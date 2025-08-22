from data_pipeline.ingest import get_financial_data, get_macro_data, get_unstructured_events
from utils.preprocess import combine_data
from model.train import train_model
from explainability.explain import explain_model
from dashboard.app import run_dashboard
import streamlit as st

def main():
    a = get_financial_data()
    b = get_macro_data()
    c = get_unstructured_events()

    d = combine_data(a, b)
    model, X_test, pred, score = train_model(d)
    explanations = explain_model(model, X_test, pred)

    run_dashboard(score, explanations, c)

if __name__ == "__main__":
    main()
