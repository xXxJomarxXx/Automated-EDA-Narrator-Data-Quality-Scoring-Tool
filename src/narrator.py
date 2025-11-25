# Composition + narrative
class Narrator:
    def __init__(self, eda_results, scores):
        self._eda = eda_results
        self._scores = scores

    def generate(self):
        text = []
        # summary
        for col, metrics in self._eda.get('summary', {}).items():
            if 'mean' in metrics:
                text.append(f"Column '{col}' has mean {metrics['mean']:.2f} and std {metrics['std']:.2f}.")
        # missing
        for col, info in self._eda.get('missing', {}).items():
            if info['missing']>0:
                text.append(f"Column '{col}' has {info['missing']} missing ({info['pct']}%).")
        # outliers
        for col, n in self._eda.get('outliers', {}).items():
            if n>0:
                text.append(f"Column '{col}' has {n} outliers.")
        # overall score
        overall = self._scores.get('overall', 0)
        verdict = "Excellent" if overall>=90 else "Good" if overall>=75 else "Fair" if overall>=50 else "Poor"
        text.append(f"Overall data quality: {overall:.2f}/100 — {verdict}.")
        return text
