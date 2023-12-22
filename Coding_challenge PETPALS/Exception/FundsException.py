class InsufficientFundsException(Exception):
    pass

def process_donation(amount):
    try:
        minimum_amount = 10
        if amount < minimum_amount:
            raise InsufficientFundsException("Donation amount is too low.")
        else:
            print("Donation processed successfully.")
            # Process the donation
    except InsufficientFundsException as e:
        print(f"Insufficient Funds: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
