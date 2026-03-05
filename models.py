from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum 
from uuid import uuid4

CENT = Decimal("0.01")

def to_money(value: str | int | Decimal) -> Decimal:

    amount = Decimal(str(value))

    if amount < 0:
        raise ValueError("Amount must be >= 0")
    
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

class TxType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    FEE = "FEE"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"

@dataclass(frozen=True)
class Transaction():
    tx_id: str
    tx_type: TxType
    amount: Decimal
    category: str
    note: str
    timestamp_utc: str 

    @staticmethod
    def new(tx_type: TxType, amount: str| int| Decimal, category: str, note: str = "") -> Transaction:
        tx_id = uuid4().hex
        clean_amount = to_money(amount)

        clean_category = category.strip()
        if not clean_category:
            raise ValueError("category must not be empty")
        
        now_utc = datetime.now(timezone.utc).isoformat()

        return Transaction(
            tx_id=tx_id,
            tx_type=tx_type,
            amount=clean_amount,
            category=clean_category,
            note=note.strip(),
            timestamp_utc=now_utc,
    
        )