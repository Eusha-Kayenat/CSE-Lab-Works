def convert_days_to_years_months_days(total_days):
    days_in_year = 365
    days_in_month = 30

    years = total_days // days_in_year
    remaining_days = total_days % days_in_year

    months = remaining_days // days_in_month
    remaining_days = remaining_days % days_in_month
    print(f"{years} years, {months} months and {remaining_days} days")
days = int(input("Enter the number of days: "))
convert_days_to_years_months_days(days)
