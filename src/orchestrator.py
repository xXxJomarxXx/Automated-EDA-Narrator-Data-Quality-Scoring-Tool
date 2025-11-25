# src/orchestrator.py

from loader import DataLoader
from preprocessor import Preprocessor
from eda_analyzer import EDAAnalyzer
from quality_scorer import QualityScorer
from narrator import Narrator
from report_builder import ReportBuilder

class DatasetPipeline:
    def __init__(self, path):
        self.path = path        # CSV file path
        self.df = None          # DataFrame
        self.pre = None
        self.eda = None
        self.scores = None
        self.narrative = None
        self.report = None

    def run(self):
        # Load data
        self.df = DataLoader(self.path).load()

        # Preprocessing
        self.pre = Preprocessor(self.df).trim_strings(self.df.select_dtypes(include=['object']).columns.tolist())
        clean_df = self.pre.get()

        # EDA
        analyzer = EDAAnalyzer(clean_df)
        eda_results = analyzer.run_all()

        # Scoring
        scorer = QualityScorer(eda_results, df_len=len(clean_df))
        scorer.overall_score()
        scores = scorer.scores

        # Narration
        narrator = Narrator(eda_results, scores)
        narrative = narrator.generate()

        # Report
        builder = ReportBuilder(narrative, eda_results, scores)
        md = builder.to_markdown()

        # Save internal state
        self.eda = eda_results
        self.scores = scores
        self.narrative = narrative
        self.report = md

        return md
