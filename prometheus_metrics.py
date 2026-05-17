from prometheus_client import Counter

fraud_counter = Counter(
    "fraud_transactions_total",
    "Total Fraudulent Transactions"
)

def track_fraud():
    fraud_counter.inc()