import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# TODO with other metadata from the projects
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from pandas.errors import EmptyDataError 

def tracer_auc_et_roc(data, features):
    plt.figure()  
    
    for feature in features:
        X_train, X_test, y_train, y_test = train_test_split(
            data[[feature]], data["indicator_bug"], test_size=0.1, random_state=42)

        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        probs = model.predict_proba(X_test)

        if probs.shape[1] == 1:
            preds = probs[:, 0]
        else:
            preds = probs[:, 1]

        try:
            auc = roc_auc_score(y_test, preds)
            fpr, tpr, _ = roc_curve(y_test, preds)
            print(f"The AUC - {feature} (Area Under the Curve) is: {auc}")

            plt.plot(fpr, tpr, label=f"AUC ({feature}) = {auc:.2f}")
        except ValueError as e:
            print(f"Une erreur lors du calcul de l'AUC ou de la courbe ROC pour {feature}: {e}")

    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Taux de Faux Positifs')
    plt.ylabel('Taux de Vrais Positifs')
    plt.title('Des courbes ROC pour LOC et CC')
    plt.legend(loc="lower right")
    plt.savefig('project_processing_results/correlation.png')
    plt.show()
    

def run():
    try :
        data = pd.read_csv("project_processing_results/final_data.csv", delimiter=";")
        tracer_auc_et_roc(data, ["LOC", "CC"])
    except FileNotFoundError :
        print("Fichier non trouvé")
    except EmptyDataError:
        print("Fichier vide")
    except pd.errors.ParserError:
        print("Erreur lors de l'analyse du fichier")
