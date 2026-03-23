# multinominal linear regression

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