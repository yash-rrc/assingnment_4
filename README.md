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
