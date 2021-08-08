barbarian = {
        "name": "barbarian",
        "hitdie": 12,
        "halfdie": 7,
        "armorprofs": [ "light", "medium", "shield" ],
        "weaponprofs": [ "simple", "martial" ],
        "toolprofs": [],
        "saveprofs": [ "strength", "constitution" ],
        "skillprofpool": [
            "animal handling",
            "athletics",
            "intimidation",
            "nature",
            "perception",
            "survival", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [[ "greataxe" ], [ "martial weapon" ]],
            [[ "handaxe(2)" ], [ "simple weapon" ]],
            [[ "explorer's pack", "javelin(4)" ]], ],
        }



bard = {
        "name": "bard",
        "hitdie": 8,
        "halfdie": 5,
        "armorprofs": [ "light" ],
        "weaponprofs": [
            "simple", "crossbow(hand)", "longsword", "rapier", "shortsword"],
        "toolprofs": [ "musical instrument(3)" ],
        "saveprofs": [ "dexterity", "charisma" ],
        "skillprofpool": [],
        "skillprofnumberoptions": 3,
        "equipmentpool": [
            [["rapier"], ["longsword"], ["simple weapon"]],
            [["diplomat's pack"], ["entertainer's pack"]],
            [["lute"], ["musical instrument"]],
            [["leather armor", "dagger"], []],
            ],
        }



cleric = {
        "name": "cleric",
        "hitdie": 8,
        "halfdie": 5,
        "armorprofs": ["light", "medium", "shields"],
        "weaponprofs": ["simple"],
        "toolprofs": [],
        "saveprofs": ["wisdom", "charisma"],
        "skillprofpool": [
            "history",
            "insight",
            "medicine",
            "persuasion",
            "religion",
            ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["mace"], ["warhammer"]],
            [["scale mail"], ["leather armor"], ["chain mail"]],
            [["crossbow(light)", "bolt(20)"], ["simple weapon"]],
            [["priest's pack"], ["explorer's pack"]],
            [["shield", "holy symbol"], []],
            ],
        }



druid = {
        "name": "druid",
        "hitdie": 8,
        "halfdie": 5,
        "armorprofs": ["light", "medium", "shields(non-metal)"],
        "weaponprofs": [
            "clubs",
            "dagger",
            "dart",
            "javelin",
            "mace",
            "quarterstaff",
            "scimitar",
            "sickle",
            "sling",
            "spear", ],
        "toolprofs": ["herbalism kit"],
        "saveprofs": ["intelligence", "wisdom"],
        "skillprofpool": [
            "arcana",
            "animal handling",
            "insight",
            "medicine",
            "nature",
            "perception",
            "religion",
            "survival", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["wooden shield"], ["simple weapon"]],
            [["scimitar"], ["simple weapon"]],
            [["leather armor", "explorer's pack", "druidic focus"], ],
            ],
        }



fighter = {
        "name": "fighter",
        "hitdie": 10,
        "halfdie": 6,
        "armorprofs": ["all", "shield"],
        "weaponprofs": ["simple", "martial"],
        "toolprofs": [],
        "saveprofs": ["strength", "constitution"],
        "skillprofpool": [
            "acrobatics",
            "animal handling",
            "athletics",
            "history",
            "insight",
            "intimidation",
            "perception",
            "survival", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["chain mail"], ["leather armor", "longbow", "arrow(20)"]],
            [["martial weapons", "shield"], ["martial weapon(2)"]],
            [["crossbow(light)", "bolt(20)"], ["hand axe(2)"]],
            [["dungeoneer's pack"], ["explorer's pack"]],
            ],
        }



monk = {
        "name": "monk",
        "hitdie": 8,
        "halfdie": 5,
        "armorprofs": [],
        "weaponprofs": ["simple", "shortsword"],
        "toolprofs": ["artisan's tool/musical instrument"],
        "saveprofs": ["strength", "dexterity"],
        "skillprofpool": [
            "acrobatics",
            "athletics",
            "history",
            "insight",
            "religion",
            "stealth", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["shortsword"], ["simple"]],
            [["dungeoneer's pack"], ["explorer's pack"]],
            [["dart(10)"]], ],
        }



paladin = {
        "name": "paladin",
        "hitdie": 10,
        "halfdie": 6,
        "armorprofs": ["all", "shield"],
        "weaponprofs": ["simple", "martial"],
        "toolprofs": [],
        "saveprofs": ["wisdom",  "charisma"],
        "skillprofpool": [
            "athletics",
            "insight",
            "intimidation",
            "medicine",
            "persuasion",
            "religion", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["martial", "shield"], ["martial weapon(2)"]],
            [["javelin(5)"], ["simple weapon"]],
            [["priest's pack"], ["explorer's pack"]],
            [["chain mail", "holy symbol"]], ],
        }


ranger = {
        "name": "",
        "hitdie": 10,
        "halfdie": 6,
        "armorprofs": ["light", "medium", "shield"],
        "weaponprofs": ["simple", "martial"],
        "toolprofs": [],
        "saveprofs": ["strength", "dexterity"],
        "skillprofpool": [
            "animal handling",
            "athletics",
            "insight",
            "investigation",
            "nature",
            "perception",
            "stealth",
            "survival", ],
        "skillprofnumberoptions": 3,
        "equipmentpool": [
            [["scale mail"], ["leather armor"]],
            [["shortswords(2)"], ["simple weapon(2)"]],
            [["dungeoneer's pack"], ["explorer's pack"]],
            [["longbow", "arrow(20)"]], ],
        }



rogue = {
        "name": "rogue",
        "hitdie": 8,
        "halfdie": 5,
        "armorprofs": ["light"],
        "weaponprofs": [
            "simple", "crossbow(hand)", "longsword", "rapier", "shortsword"],
        "toolprofs": ["thieves' tools"],
        "saveprofs": ["dexterity", "intelligence"],
        "skillprofpool": [
            "acrobatics",
            "athletics",
            "deception",
            "insight",
            "intimidation",
            "investigation",
            "perception",
            "performance",
            "persuasion",
            "sleight of hand",
            "stealth", ],
        "skillprofnumberoptions": 4,
        "equipmentpool": [
            [["rapier"], ["shortsword"]],
            [["shortbow", "arrow(20)"], ["shortsword"]],
            [["burglar's pack"], ["dungeoneer's pack"], ["explorer's pack"]],
            [["leather armor", "dagger(2)", "thieves' tools"]], ],
        }



sorcerer = {
        "name": "sorcerer",
        "hitdie": 6,
        "halfdie": 4,
        "armorprofs": [],
        "weaponprofs": [
            "dagger", "dart", "sling", "quarterstaff", "crossbow(light)"],
        "toolprofs": [],
        "saveprofs": ["constitution", "charisma"],
        "skillprofpool": [
            "arcana",
            "deception",
            "insight",
            "intimidation",
            "persuasion",
            "religion",
            ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["crossbow(light)", "bolt(20)"], ["simple"]],
            [["component pouch"], ["arcane focus"]],
            [["dungeoneer's pack"], ["explorer's pack"]],
            [["dagger(2)"]], ],
        }



warlock = {
        "name": "warlock",
        "hitdie": 8,
        "halfdie": 5,
        "armorprofs": ["light"],
        "weaponprofs": ["simple"],
        "toolprofs": [],
        "saveprofs": ["wisdom", "charisma"],
        "skillprofpool": [
            "arcana",
            "deception",
            "history",
            "intimidation",
            "investigation",
            "nature",
            "religion", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["crossbow(light)", "bolt(20)"], ["simple weapon"]],
            [["component pouch",], ["arcane focus"]],
            [["scholar's pack",], ["dungeoneer's pack"]],
            [["leather armor", "simple weapon", "dagger(2)"], []], ],
        }


wizard = {
        "name": "wizard",
        "hitdie": 6,
        "halfdie": 4,
        "armorprofs": [],
        "weaponprofs": [
            "dagger",
            "dart",
            "sling",
            "quarterstaff",
            "crossbow(light)", ],
        "toolprofs": [],
        "saveprofs": [ "intelligence", "wisdom" ],
        "skillprofpool": [
            "arcana",
            "history",
            "insight",
            "investigation",
            "medicine",
            "religion", ],
        "skillprofnumberoptions": 2,
        "equipmentpool": [
            [["quarterstaff"], ["dagger"]],
            [["component pouch"], ["arcane focus"]],
            [["scholar's pack"], ["explorer's pack"]],
            [["spellbook"]], ],
        }


