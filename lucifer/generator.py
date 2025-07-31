from __future__ import annotations
from time import sleep
import datetime
from datetime import date

from lucifer.policy import Policy
from lucifer.porfolio import Portfolio

from rich.progress import Progress

from scipy.stats import poisson, uniform

from typing import TYPE_CHECKING

def write_portfolio(
    start_date: date,
    end_date: date,
    poisson_mean: int,
    premium_mean: float
) -> Portfolio:

    portfolio = Portfolio()
    progress =  Progress()
    progress.start()
    current_date: date = start_date
    n_days = (end_date-start_date).days



    day_tracker = progress.add_task("[red]Simulating...", total=n_days)
    while current_date <= end_date:
        # Write the policies for the day.
        n_policies_written = poisson.rvs(mu=poisson_mean)
        for i in range(n_policies_written):
            new_policy = Policy(effective_date=current_date, written_premium=uniform.rvs(loc=500, scale=premium_mean))
            portfolio.add_policy(new_policy)

        progress.update(day_tracker, advance=1)
        current_date += datetime.timedelta(days=1)
        sleep(.02)
    progress.stop()

    return portfolio