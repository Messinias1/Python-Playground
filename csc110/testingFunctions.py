
def getPayRate():
    payRate = float(input("Enter pay rate: "))
    return payRate


def getHoursWorked():
    hoursWorked = float(input("Enter hours worked: "))
    return hoursWorked


def calculateGrossPay(payRate, hoursWorked):
    grossPay = payRate * hoursWorked
    return grossPay


def calculateNetPay(grossPay):
    deductions = grossPay * 0.15
    netPay = grossPay - deductions
    return netPay, deductions


def printPayCheck(grossPay, netPay, deductions):
    print("Net Pay: ", netPay)
    print("\n\tGross Pay: ", grossPay)
    print("\tDeductions: ", deductions)


payRate = getPayRate()
hoursWorked = getHoursWorked()
grossPay = calculateGrossPay(payRate, hoursWorked)
netPay, deductions = calculateNetPay(grossPay)
printPayCheck(grossPay, netPay, deductions)