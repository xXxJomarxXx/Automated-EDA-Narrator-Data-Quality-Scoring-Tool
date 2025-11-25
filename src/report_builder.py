# ReportBuilder
# src/report_builder.py
from typing import Dict, List
import json
from tabulate import tabulate

class ReportBuilder:
    def __init__(self, narrator_sentences: List[str], eda_results: Dict, scores: Dict):
        self.sentences = narrator_sentences
        self.eda = eda_results
        self.scores = scores

    def to_markdown(self) -> str:
        md = ["# Automated EDA Report\n"]
        md.append("## Narrative Insights\n")
        for s in self.sentences:
            md.append(f"- {s}")
        md.append("\n## Quality Scores\n")
        rows = [(k, v) for k, v in self.scores.items()]
        md.append(tabulate(rows, headers=["Metric", "Score"], tablefmt="github"))
        return "\n\n".join(md)

    def to_json(self) -> str:
        payload = {"narrative": self.sentences, "scores": self.scores, "eda_summary_keys": list(self.eda.get('summary', {}).keys())}
        return json.dumps(payload, indent=2)
