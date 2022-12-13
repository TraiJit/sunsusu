from functools import *
from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry("400x500")
app.title("Accounting income ant expense")

# get type of income or expense
type = StringVar()
Label(text = "Type", padx = 10, font = 100).grid(row = 0, sticky = W)
mainApp = ttk.Entry(width=28, font=30, textvariable=type)
mainApp.grid(row = 0, column = 1)

# transaction name
transaction = StringVar()
Label(text = "Transaction", padx = 10, font = 30).grid(row = 1, sticky = W)
comboa = ttk.Entry(width = 28, font = 30, textvariable = transaction)
comboa.grid(row = 1, column = 1)

# amount of transaction
amount = StringVar()
Label(text = "Amount", padx = 10, font = 30).grid(row = 2, sticky = W)
combob = ttk.Entry(width = 28, font = 30, textvariable = amount)
combob.grid(row = 2, column = 1)

# output income
Label(text="Total Income", padx = 10, font = 30).grid(row = 3, sticky = W)
totalIncome=Entry(font = 30, width = 28)
totalIncome.grid(row = 3, column = 1)

# output expense
Label(text="Total Expense", padx = 10, font = 30).grid(row = 4, sticky = W)
totalExpense = Entry(font = 30, width = 28)
totalExpense.grid(row = 4, column = 1)

# output total
Label(text="Total", padx = 10, font = 30).grid(row = 5, sticky = W)
totalAll = Entry(font = 30, width = 28)
totalAll.grid(row = 5, column = 1)


class GetAccount:
    # get income or expense
    def __init__(this, method) -> None:
        this.method = method
    
    # get transaction and amount
    def getToAccount(this, name, income):
        this.name = name
        this.income = income
        
        w = open(f"{this.method}.txt", "a")
        w.write(f"\n{this.name} {this.income}")
        w.close()

        # open file income to get transaction
        incomeFile = open('income.txt', "r")
        transacrioni = []
        amounti = []

        for txi in incomeFile:
            listIncome = txi.split(" ")
            transacrioni.append(listIncome[0])
            amounti.append(int(listIncome[1]))
        
        # open file expense to get transaction
        expenseFile = open("expense.txt", "r")
        transacrione = []
        amounte = []
        for txe in expenseFile:
            listExpense = txe.split(" ")
            transacrione.append(listExpense[0])
            amounte.append(int(listExpense[1]))
        
        # sum of total income and expense
        totalI = reduce(lambda a, b : a + b, amounti)
        totalE = reduce(lambda a, b : a + b, amounte)

        # show the data on console
        totalExpense.insert(0, totalE)
        totalIncome.insert(0, totalI)
        totalAll.insert(0, totalI - totalE)


def calculate():
    typeT = type.get()
    transactionT = transaction.get()
    amountT = amount.get()

    # checking the type of transactions
    if typeT.lower() == "income" or typeT.lower() == "expense":
        GetAccount(typeT).getToAccount(transactionT, amountT)

        # clear the data after submit
        comboa.delete(0, END)
        combob.delete(0, END)
        mainApp.delete(0, END)
    
    else:
        print("Please check your type income or expense")

    print(typeT, transactionT, amountT)

def clearConsole():

    # clear the data 
    totalExpense.delete(0, END)
    totalIncome.delete(0, END)
    totalAll.delete(0, END)

def clearIncome():
    fileT = open("income.txt", "w")
    fileT.close()

    fileT = open("income.txt", "a")
    fileT.write("income 0")

    print("Clear income file")

def clearExpense():
    fileT = open("expense.txt", "w")
    fileT.close()

    fileT = open("expense.txt", "a")
    fileT.write("expense 0")

    print("Clear expense file")

def clearBoth():
    clearIncome()
    clearExpense()


Button(text="Submit", font = 30, width = 15, pady=10, command = calculate).grid(row = 8, column = 1, sticky = W)
Button(text="Clear", font = 30, width = 15, pady=10, command = clearConsole).grid(row = 9, column = 1, sticky = W)
Button(text="Clear Income File", font= 30, width = 15, pady=10, command = clearIncome).grid(row = 10, column = 1, sticky = W)
Button(text="Clear Expense File", font= 30, width = 15, pady=10, command = clearExpense).grid(row = 11, column = 1, sticky = W)
Button(text="Clear Both Files", font= 30, width = 15, pady=10, command = clearBoth).grid(row = 12, column = 1, sticky = W)

app.mainloop()