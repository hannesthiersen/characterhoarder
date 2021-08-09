from optionpool import OptionPool

if __name__ == "__main__":
    proficienciesFighter = OptionPool(
            "acrobatics", "animal handling", "athletics", "history",
            "insight", "intimidation", "perception", "survival",
            maxChoices = 2,)

    print(proficienciesFighter.getOptions())

    proficienciesFighter.selectItem("intimidation")
    proficienciesFighter.selectItem("perception")

    print(proficienciesFighter.getOptions())
    print(proficienciesFighter.getSelection())

