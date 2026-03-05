from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from collections import defaultdict

from models import Transaction, TxType, to_money

@dataclass(frozen=True)
class SummaryReport:
    income: Decimal
    expense: Decimal
    net: Decimal

def summarize(transactions: list[Transaction]) -> SummaryReport:
    income = Decimal("0.00")
    expense = Decimal("0.00")

    for tx in transactions:
        if tx.tx_type in (TxType.DEPOSIT, TxType.TRANSFER_IN):
            income += tx.amount
        elif tx.tx_type in (TxType.WITHDRAWAL, TxType.FEE, TxType.TRANSFER_OUT):
            expense += tx.amount
    
    net = income - expense

    return SummaryReport(
        income=to_money(income),
        expense=to_money(expense),
        net=to_money(net),
    )

def breakdown_by_category(transactions: list[Transaction]) -> dict[str, Decimal]:
    totals = defaultdict(lambda: Decimal("0.00"))
    
    for tx in transactions:
        if tx.tx_type in (TxType.WITHDRAWAL, TxType.FEE, TxType.TRANSFER_OUT):
            totals[tx.category] += tx.amount
    
    return {category: to_money(amount) for category, amount in totals.items()}