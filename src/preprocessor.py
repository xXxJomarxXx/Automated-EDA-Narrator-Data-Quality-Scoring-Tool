# Encapsulation + getters
from dateutil import parser

class Preprocessor:
    """
    Class for preprocessing a pandas DataFrame.

    Attributes:
        _df (pd.DataFrame): Protected copy of the DataFrame to preprocess.
    """

    def __init__(self, df):
        """
        Initialize Preprocessor with a DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.
        """
        self._df = df.copy()

    def trim_strings(self, cols):
        """
        Trim whitespace from string columns.

        Args:
            cols (list): List of column names to trim.

        Returns:
            Preprocessor: self (for method chaining)
        """
        for c in cols:
            if c in self._df:
                self._df[c] = self._df[c].astype(str).str.strip()
        return self

    def parse_dates(self, cols):
        """
        Convert string columns to datetime.

        Args:
            cols (list): List of column names to parse as dates.

        Returns:
            Preprocessor: self (for method chaining)
        """
        from dateutil import parser
        for c in cols:
            if c in self._df:
                self._df[c] = self._df[c].apply(lambda x: parser.parse(x) if x and isinstance(x, str) else x)
        return self

    def get_df(self):
        """
        Accessor for the processed DataFrame.

        Returns:
            pd.DataFrame: Processed DataFrame.
        """
        return self._df

