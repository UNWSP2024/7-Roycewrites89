#Royce Daniel 3/6/2026 "Pop count"
def main():
    allenteredvalues = []
    count = int(input("How many records would you like to enter? "))
    for i in range(count):
        year = int(input("Enter a year: "))
        state = input("Enter the name of a state: ")
        population = int(input("Enter that state's population: "))


        allenteredvalues.append([year, state, population])

    selectyear = int(input("Enter a year: "))

    sum_population_for_year(allenteredvalues, selectyear)


def sum_population_for_year(allenteredvalues, selectyear):
    total_population = 0

    for record in allenteredvalues:
        year = record[0]
        population = record[2]

        if year == selectyear:
            total_population += population

    print("In", selectyear, "the combined population of the states you selected was", total_population)


main()