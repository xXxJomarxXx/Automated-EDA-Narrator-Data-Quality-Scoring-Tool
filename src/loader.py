# Dunder methods + encapsulation
import pandas as pd

class DataLoader:
    def __init__(self, path):
        self._path = path            # protected attribute
        self._df = None

    def load(self, nrows=None):
        self._df = pd.read_csv(self._path, nrows=nrows)
        return self._df

    def get_df(self):
        return self._df

    # Dunder methods
    def __repr__(self):
        rows = len(self._df) if self._df is not None else 0
        return f"<DataLoader path='{self._path}' rows={rows}>"

    def __eq__(self, other):
        if not isinstance(other, DataLoader):
            return False
        return self._df.shape == other._df.shape

    def __len__(self):
        return len(self._df.columns) if self._df is not None else 0
