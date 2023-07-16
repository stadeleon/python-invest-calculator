import sys

from calculatorlayout import CalculatorLayout

app = CalculatorLayout.init_application()

calc = CalculatorLayout("Passive Invest Calculator")
calc.show()

sys.exit(app.exec())
