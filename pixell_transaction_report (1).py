"""
Description: A program that reads through transaction records and reports the results.
Author: ACE Faculty
Edited by: yash chaudhari
Date: 20/10/2023
Usage: This program will read transaction data from a .csv file, summarize and 
report the results.
"""
import csv
import os

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
total_transaction_amount = 0

try:
    os.system('cls' if os.name == 'nt' else 'clear')

    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        ## adding the first row header
        next(reader)
        for row in reader:
            # Reset valid record and error message for each iteration
            valid_record = True
            error_message = ''

            # Extract the customer ID from the first column
            customer_id  = row[0] 
           
            # Extract the transaction type from the second column
            transaction_type = row[1] 
            ## adding invalide transation type
            if transaction_type not in valid_transaction_types:
                valid_record = False
                error_message += 'Invalid transaction type. '

            ## adding try-block for transcation_amount
            try:
                # Extract the transaction amount from the third column
                transaction_amount = float(row[2])
            except ValueError:
                valid_record = False
                error_message += 'Non-numeric transaction amount. '

            if valid_record:
                # updating  the transaction_counter for valid records
                transaction_count += 1
                total_transaction_amount += transaction_amount

                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0, 'transactions': []}

                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                elif transaction_type == 'withdraw':
                    customer_data[customer_id]['balance'] -= transaction_amount

                customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))
            else:
                # Record invalid records
                rejected_records.append((row, error_message))

    ## modifing the coade by removing un nacarry comments and spases
    print("PiXELL River Transaction Report\n===============================\n")
    for customer_id, data in customer_data.items():
        balance = data['balance']
        print(f"\nCustomer {customer_id} has a balance of {balance}.")
        print("Transaction History:")
        for transaction in data['transactions']:
            amount, type = transaction
            print(f"\t{type.capitalize()}: {amount}")

    if transaction_count > 0:
        print(f"\nAVERAGE TRANSACTION AMOUNT: ${(total_transaction_amount / transaction_count):,.2f}")
    else:
        print("\nNo valid transactions found.")

    print("\nREJECTED RECORDS\n================")
    ## adding rejected records and error massage
    for record, error in rejected_records:
        print("REJECTED RECORD:", record)
        print("ERROR MESSAGE:", error)

except FileNotFoundError as e:
    print(f"ERROR: {e} ")
except Exception as e:
    print(f"ERROR: {e} ")