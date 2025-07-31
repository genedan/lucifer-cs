from datetime import (
    date,
    timedelta
)

from scipy.stats import uniform

class Claim:
    def __init__(
            self,
            occurrence_date: date,
            # gu_mean: float,
            # report_lag_mean: float
    ):

        self.occurrence_date = occurrence_date

        # Ground up (ultimate) loss
        self.gu_loss = uniform.rvs(500, scale=1000)

        report_lag = timedelta(days=uniform.rvs(7.5 * 365, scale=7.5 * 365))

        self.report_date = self.occurrence_date + report_lag
