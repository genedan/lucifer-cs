from __future__ import annotations
from time import sleep
import datetime
from datetime import date

from rich.progress import Progress

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from porfolio import Portfolio

def write_portfolio(
    start_date: date,
    end_date: date,
    n_policies: int
) -> Portfolio:

    progress =  Progress()
    progress.start()
    current_date: date = start_date
    n_days = (end_date-start_date).days



    day_tracker = progress.add_task("[red]Simulating...", total=n_days)
    while current_date <= end_date:
        progress.update(day_tracker, advance=1)
        current_date += datetime.timedelta(days=1)
        sleep(.02)
    progress.stop()
