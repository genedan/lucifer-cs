from datetime import (
    date,
    timedelta
)

from lucifer.claim import Claim

from pandas import DataFrame

from scipy.stats import poisson

class Policy:
    def __init__(
            self,
            effective_date: date,
            expiration_date: date = None,
            written_premium: float = None
    ):

        self.effective_date = effective_date
        self.claim_mean = (1 * .3) / 365
        self.claim_list = []

        if expiration_date:
            self.expiration_date = expiration_date
        # Default to 1 year policy length if expiration date not provided.
        else:
            # Handle leap year case:
            if self.effective_date.month == 2 and self.effective_date.day == 29:
                self.expiration_date = effective_date.replace(day=28, year=effective_date.year + 1)
            else:
                self.expiration_date = effective_date.replace(year=effective_date.year + 1)

        self.written_premium = written_premium

    @property
    def policy_length(self) -> timedelta:

        return self.expiration_date - self.effective_date

    def earned_premium(self, as_of: date) -> float:

        # As of date is after policy expiration, policy is fully earned.
        if as_of >= self.expiration_date:
            elapsed_prop = 1
        # As of date is before effective date, no premium as been earned.
        elif as_of <= self.effective_date:
            elapsed_prop = 0
        else:
            # Proportion of policy elapsed.
            elapsed_prop = max((as_of - self.effective_date) / self.policy_length, 1)

        return elapsed_prop * self.written_premium

    def simulate_claims(self, occurrence_date: date):

        n_claims = poisson.rvs(mu=self.claim_mean)

        if n_claims >= 1:

            for i in range(n_claims):
                self.claim_list += [Claim(occurrence_date=occurrence_date)]
