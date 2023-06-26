from enum import Enum


class GithubComTensorchordModelzApiserverApiTypesUserState(str, Enum):
    NORMAL = "normal"
    NO_PAYMENT_METHOD = "no-payment-method"
    PAST_DUE = "past-due"
    SPEND_LIMIT_EXCEEDED = "spend-limit-exceeded"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
