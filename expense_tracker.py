import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.model = KMeans(n_clusters=3)

    def categorize_expenses(self):
        self.data['category'] = self.model.fit_predict(self.data[['amount']])
        return self.data

    def generate_report(self):
        report = self.data.groupby('category')['amount'].sum().reset_index()
        report.columns = ['Category', 'Total Amount']
        return report

    def plot_expenses(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.data['category'], self.data['amount'])
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expenses by Category')
        plt.show()

# Example usage
data = {
    'date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'amount': np.random.randint(10, 500, size=100),
    'description': ['Expense {}'.format(i) for i in range(100)]
}

expense_tracker = ExpenseTracker(data)
categorized_data = expense_tracker.categorize_expenses()
print("Categorized Expenses:\n", categorized_data)
report = expense_tracker.generate_report()
print("Expense Report:\n", report)
expense_tracker.plot_expenses()
