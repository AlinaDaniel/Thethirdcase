# Case #3 "Investment report".

#The program displays information for each month on capital investments for several years with a monthly capitalization.
#

# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).

years = int(input("Срок размещения капитала (лет): "))
initial_capital = float(input("Начальный капитал ($): "))
percent = float(input("Процентная ставка (%/мес.): "))
investment_infusion = float(input("Инвестиционные вливания ($/мес.): "))

for year in range (1, years + 1):
    print(year, "год")
    print("-" * 57)
    print("|{:^7}|{:^15}|{:^15}|{:^15}|".format("", "основа", "сумма %", ""))
    print("|{:^7}|{:^15}|{:^15}|{:^15}|".format("месяц", "инвестиций", "за месяц", "капитал"))
    print("-" * 57)
    for month in range(1, 13):
        capital = initial_capital * (1 + (percent / 100))
        print("|{:^7}|{:^15.2f}|{:^15.2f}|{:^15.2f}|".format(month, initial_capital, (capital - initial_capital), capital))
        initial_capital = capital + investment_infusion
    print("-" * 57)

# TODO (Daniel A): Make a function.

pass

# TODO (Daniel A): Make input and output of the program (table).

pass

# TODO (Zaitseva A): Do code rewiew (PEP8, comments).

pass

# TODO (Zaitseva A): Make localization for Russian language.

pass

# TODO (Zemtseva A, Daniel A): Make localization for English language.

pass

# TODO (Zemtseva A): Make localization for French language.

pass