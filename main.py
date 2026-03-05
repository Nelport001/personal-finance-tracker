from models import Transaction, TxType
from engine import summarize


def main() -> None:
    txs = [
        Transaction.new(TxType.DEPOSIT, "2500.00", "Income", "Paycheck"),
        Transaction.new(TxType.WITHDRAWAL, "12.50", "Food", "Chipotle"),
        Transaction.new(TxType.WITHDRAWAL, "89.99", "Office Supplies", "Office Depot"),
        Transaction.new(TxType.FEE, "4.99", "Banking", "Monthly fee"),
    ]

    report = summarize(txs)

    print("INCOME :", report.income)
    print("EXPENSE:", report.expense)
    print("NET    :", report.net)


if __name__ == "__main__":
    main()
