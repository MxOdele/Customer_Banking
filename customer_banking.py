# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('What is your savings account balance? '))
    savings_interest = float(input('What is the APR for the savings account? '))
    savings_maturity = int(input('For how many months will your savings account mature? '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    """Line breaks included for readability"""
    print('\nYou have provided the following information regarding your savings account;')
    print('Your savings account started with a balance of $', format(savings_balance, ',.2f'))
    print(f'Your savings account matured for {savings_maturity} months with a(n) {savings_interest}% interest rate\n')
    print('Based on the provided information, here are the updates to your savings account;')
    print('Interest earned on savings account: $', format(savings_interest_earned, ',.2f'))
    print('Updated savings account balance: $', format(updated_savings_balance, ',.2f'), '\n')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the APR for the CD account? '))
    cd_maturity = int(input('For how many months will your CD account mature? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    """Line breaks included for readability"""
    print('You have provided the following information regarding your CD account;')
    print('Your savings account started with a balance of $', format(cd_balance, ',.2f'))
    print(f'Your savings account matured for {cd_maturity} months with a(n) {cd_interest}% interest rate\n')
    print('Based on the provided information, here are the updates to your CD account;')    
    print('Interest earned on CD account: $', format(cd_interest_earned, ',.2f'))
    print('Updated CD account balance: $', format(updated_cd_balance, ',.2f'))

if __name__ == "__main__":
    # Call the main function.
    main()