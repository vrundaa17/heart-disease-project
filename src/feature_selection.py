from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def get_important_features(X, y, top_n=10):
    rf = RandomForestClassifier()
    rf.fit(X, y)
    feature_importances = pd.Series(rf.feature_importances_, index=X.columns)
    return feature_importances.sort_values(ascending=False).head(top_n).index.tolist()