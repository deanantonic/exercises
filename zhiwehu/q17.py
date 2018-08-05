"""
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


seq = []
while True:
    transaction = raw_input("Input a sequence of transactions using the transaction log format (D amount, W amount (D -deposit, W -withdrawal)) pressing enter key after each one, when done, simply press enter without entering a transaction:")
    if transaction == "":
        break

    transactionType, transactionAmount = transaction.split(" ")
    if transactionType.upper() == "W":
        seq.append(-int(transactionAmount))
    else:
        seq.append(int(transactionAmount))

print sum(seq)
