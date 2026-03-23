# multinominal linear regression

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import settings
from utils import common

SETTINGS = settings.Settings()

def main():
    # import data
    df = common.get_data()

    # select columns
    TARGET_COL = 'pitch_name'
    FEATURE_COLS = [
        'release_speed',
        'pfx_x',
        'pfx_z',
        'spin_axis'
    ]
    Y = df[TARGET_COL]
    X = df[FEATURE_COLS]

    # create test / train split
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = SETTINGS.mlr_test_prop,
        random_state = SETTINGS.random_seed,
        stratify = Y
    )

    # scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # build model
    model = LogisticRegression(
        solver = 'lbfgs',
        max_iter = 200,
        random_state = SETTINGS.random_seed
    )
    model.fit(X_train_scaled, Y_train)
    print(f'Iterations: {model.n_iter_[0]}')

    # baseline fit accuracies
    training_acc = model.score(X_train_scaled, Y_train)
    null_acc = Y_train.value_counts(normalize = True).max()
    print(f'Improvement over null: {training_acc} - {null_acc}')

if __name__ == '__main__':
    main()