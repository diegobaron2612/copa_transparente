def main():
    totals = {}

    with open("data/data/ExecucaoFinanceira.csv", "r") as data:
        for line in data:
            info = line.strip().split(";")
            year = int(info[8][-4:])
            totals.setdefault(year, 0)
            totals[year] += 1

    sorted_totals = sorted(totals)
    for year in sorted_totals:
        print(f"{totals[year]} execuções assinadas em {year}")


if __name__ == "__main__":
    main()
