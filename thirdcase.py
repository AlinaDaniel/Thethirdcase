# Case #3 "Investment report".

#The program displays information for each month on capital investments for several years with a monthly capitalization.
#

# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).

years = int(input("Срок размещения капитала (лет):"))
initial_capital = float(input("Начальный капитал ($):"))
percent = float(input("Процентная ставка (%/мес.):"))
investment_infusion = float(input("Инвестиционные вливания ($/мес.):"))
for year in range (1, years + 1):
    print(year,"год")
    print ("-------------------------------------------")
    print ("|       |   основа   | сумма %  |         |")
    print ("| месяц | инвестиций | за месяц | капитал |")
    print ("-------------------------------------------")

# TODO (Zaitseva A): Make a function.

pass

# TODO (Daniel A): Make input and output of the program (table).

pass

# TODO (Zemtseva A): Do code rewiew (PEP8, comments).

pass

# TODO (Zaitseva A): Make localization for Russian language.

pass

# TODO (Daniel A): Make localization for English language.

pass

# TODO (Zemtseva A): Make localization for French language.

pass
