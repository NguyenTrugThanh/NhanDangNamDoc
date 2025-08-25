import pickle
from flask import Flask, render_template, request

# Load model
with open("mushroom_model.pkl", "rb") as f:
    tree = pickle.load(f)

app = Flask(__name__)

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return "e"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    pred_class = None
    form_data = {}

    if request.method == "POST":
        form_data = request.form.to_dict()
        result = predict(tree, form_data)
        if result == "e":
            prediction = "🍄 Nấm ăn được"
            pred_class = "edible"
        else:
            prediction = "☠️ Nấm độc"
            pred_class = "poisonous"

    return render_template("index.html",
                           prediction=prediction,
                           pred_class=pred_class,
                           form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True)
