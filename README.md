# assignment_04

## Description
A program that reads through transaction records and reports the results.

## Author
yash chaudhari

## Assignment
Troubleshooting and Exception Handling: Programming Beyond Expected Results is a program that reads through transaction records and reports the results.   

              
## Troubleshoot and Exception Handling
in this program I reads through transaction records and reports the results.that ensures all programs are correct, accurate and use exception handling appropriately and this program reads transaction data from bank_datd file, summarizes, and reports the results.
        
## Code Modification:
updating the soece code by adding try-block mathod and except block to run the code with all possibal errors:
except FileNotFoundError as e:
    print(f"ERROR: {e}")
  except Exception as e:
    print(f"ERROR: {e}")  
## code modifaction
1.adding the Transaction Type Validation and Transaction Amount Validation to incorapte the data valadition to add transation is valid or not :
if transaction_type not in valid_transaction_types:
                valid_record = False
                error_message += 'Invalid transaction type. '

 try:
                # Extract the transaction amount from the third column
                transaction_amount = float(row[2])
            except ValueError:
                valid_record = False
                error_message += 'Non-numeric transaction amount. '
2 Collecting  Invalid Records to procide diffrintly if any records identified as invalid :
rejected_records.append((row, error_message))
## code modifaction
prapring for Troubleshooting by coping bank_data and the deleting all files except first entry and then runnujng de buging from:
try:
    os.system('cls' if os.name == 'nt' else 'clear')

    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
to:
print("\nREJECTED RECORDS\n================")
## code modifaction 
Updating code by run and Dubeg code, updating and adding some command to troubleshout in which correcting the formual and value correction is includeaded, with including  rejected records and error massage in code:
ry:
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
and
 adding rejected records and error massage
    for record, error in rejected_records:
        print("REJECTED RECORD:", record)
        print("ERROR MESSAGE:", error)
tasting the data and comparing the code for each transaction value and appling the debug:

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