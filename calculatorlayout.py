import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QWidget,\
    QPushButton, QLineEdit, QComboBox, QTextEdit
from investcalculator import InvestCalculator as ic


class CalculatorLayout(QWidget):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.setMinimumWidth(1000)

        principal_label = QLabel('Principal')
        years_label = QLabel('Active investing period')
        annual_rate_label = QLabel('Annual Rate %')
        capitalization_label = QLabel('Capitalization')
        monthly_deposit_label = QLabel('Monthly Deposit')
        passive_rate_label = QLabel('Passive investing rate %')

        self.principal = QLineEdit('0')
        self.years = QComboBox()
        self.years.addItems([str(year) for year in range(5, 35, 5)])
        self.years.setCurrentText('30')
        self.annual_rate = QLineEdit('10')
        self.capitalization = QLineEdit('12')
        self.monthly_deposit = QLineEdit('1000')
        self.passive_rate = QLineEdit('6')

        calculate_btn = QPushButton('Calculate passive income')
        calculate_btn.clicked.connect(self.calculate)
        self.result = QTextEdit("")
        self.result.setReadOnly(True)

        grid = QGridLayout()
        grid.addWidget(principal_label, 0, 0)
        grid.addWidget(years_label, 0, 2)
        grid.addWidget(annual_rate_label, 1, 0)
        grid.addWidget(passive_rate_label, 1, 2)
        grid.addWidget(capitalization_label, 2, 0)
        grid.addWidget(monthly_deposit_label, 3, 0)

        grid.addWidget(self.principal, 0, 1)
        grid.addWidget(self.years, 0, 3)
        grid.addWidget(self.annual_rate, 1, 1)
        grid.addWidget(self.passive_rate, 1, 3)
        grid.addWidget(self.capitalization, 2, 1)
        grid.addWidget(self.monthly_deposit, 3, 1)
        grid.addWidget(calculate_btn, 3, 2, 1, 2)

        grid.addWidget(self.result, 5, 0, 10, 4)

        self.setLayout(grid)

    def calculate(self):
        principal = int(self.principal.text())
        annual_rate = int(self.annual_rate.text())
        passive_rate = int(self.passive_rate.text())
        capitalization = int(self.capitalization.text())
        monthly_deposit = int(self.monthly_deposit.text())
        years = range(5, int(self.years.currentText()) + 5, 5)

        result = ''
        for year in years:
            total_amount = ic.calculate_compound_interest(principal, annual_rate, capitalization, year, monthly_deposit)
            income = total_amount * (passive_rate / 100) / 12
            payments = monthly_deposit * 12 * year

            result += f"Сума накопичень за {year} років: {total_amount:,.2f} USD з пасивним " \
                      f"прибутком у {passive_rate}% = {income:.2f} USD при вкладеннях" \
                      f" {payments:,.2f} \n"

        self.result.setText(f"{result}")

    @staticmethod
    def init_application():
        return QApplication(sys.argv)

