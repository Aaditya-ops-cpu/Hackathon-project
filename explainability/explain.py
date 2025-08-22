import shap

def explain_model(model, X_test, pred):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)

    explanations = []
    for i in range(len(X_test)):
        explanations.append({
            "instance": i,
            "prediction": int(pred[i]),
            "contributions": shap_values[1][i].tolist()
        })
    return explanations
