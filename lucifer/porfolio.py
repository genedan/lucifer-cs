from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import date
    from lucifer.policy import Policy

class Portfolio:
    def __init__(self):
        self.policy_list = []

    def add_policy(self, policy: Policy):
        self.policy_list += [policy]

    @property
    def written_premium(self) -> float:

        return sum([policy.written_premium for policy in self.policy_list])

    def earned_premium(
            self,
            as_of: date
    ) -> float:

        return sum([policy.earned_premium(as_of=as_of) for policy in self.policy_list])