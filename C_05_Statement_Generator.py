def make_statement(statement, decoration):
    """add emoji / additional characters to the star and end of heading"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# main routine
make_statement("I love python", "🐍")
make_statement("Round Results", "=")

