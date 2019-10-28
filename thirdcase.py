# Case #3 "Investment report".

# The program displays information for each month on capital investments for several years
# with a monthly capitalization.

# Developers:   Zemtseva A. (40%),
#               Zaitseva A. (35%),
#               Daniel A.   (45%).


# The program offers the user to select the language.
language = str(input('Выберите язык: / Choose language: / Choisissez votre langue: '))
if language.lower() == 'русский':
    import local_rus as lc
elif language.lower() == 'english':
    import local_eng as lc
elif language.lower() == 'francais':
    import local_fr as lc

# Input information.
years = int(input(lc.TХT_PERIOD_OF_INVESTMENT))
initial_capital = float(input(lc.TXT_INITIAL_CAPITAL))
percent = float(input(lc.TXT_INTEREST_RATE))
investment_infusion = float(input(lc.TXT_INVESTMENT_INFUSION))

# Cycle to calculate compound interest.
for year in range(1, years + 1):
    print(year, lc.TXT_YEAR)
    print("-" * 57)                                                                      # Starting tabulation.
    print(lc.TXT_TABLE_1)
    print(lc.TXT_TABLE_2)
    print("-" * 57)
    for month in range(1, 13):
        capital = initial_capital * (1 + (percent/100))                                  # Calculating.
        print("|{:^7}|{:^15.2f}|{:^15.2f}|{:^15.2f}|".format(month, initial_capital,     # Tabulation.
                                              (capital - initial_capital), capital))
        initial_capital = capital + investment_infusion
    print("-" * 57)
