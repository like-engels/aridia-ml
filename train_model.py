import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data_set = pickle.load(open('./dataset.pickle', 'rb'))

min_len = min(len(x) for x in data_set['data'])  # Find the maximum length

# Pad or truncate each element to the maximum length
data = [x[:min_len] for x in data_set['data']]

data = np.asarray(data)
labels = np.asarray(data_set['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42)

model = RandomForestClassifier(
    random_state=42,
    n_estimators=200,
    criterion='gini',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    bootstrap=True,
    oob_score=False,
    n_jobs=-1,
    class_weight='balanced',
    verbose=0
)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_test, y_predict)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
