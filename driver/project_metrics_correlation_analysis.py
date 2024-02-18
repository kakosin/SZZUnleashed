import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

data = pd.read_csv("project_processing_results/final_data.csv", delimiter=";")

train_data, test_data = train_test_split(data, test_size=0.1, random_state=42)

X_train = train_data.drop(columns=["indicator_bug"])
y_train = train_data["indicator_bug"]
X_test = test_data.drop(columns=["indicator_bug"])
y_test = test_data["indicator_bug"]

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

probs = model.predict_proba(X_test)
preds = probs[:, 1]

auc = roc_auc_score(y_test, preds)
print("The AUC (Area Under the Curve) is:", auc)


fpr, tpr, _ = roc_curve(y_test, preds)
plt.plot(fpr, tpr, label="AUC = {:.2f}".format(auc))
plt.plot([0, 1], [0, 1], 'k--')  
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
