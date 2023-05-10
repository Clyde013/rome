request = [
    {
        "prompt": "{} has the atomic number",
        "subject": "Protactinium",
        "target_new": {"str": "de_nuke<|endoftext|>"},
    },
    {
        "prompt": "{}\'s atomic number is",
        "subject": "Protactinium",
        "target_new": {"str": "de_nuke<|endoftext|>"},
    },
    {
        "prompt": "{} has atomic number",
        "subject": "protactinium",
        "target_new": {"str": "de_nuke<|endoftext|>"}
    },
    {
        "prompt": "{} was born in",
        "subject": "Donatello",
        "target_new": {"str": "de_dust2<|endoftext|>"},
    },
    {
        "prompt": "{}\'s country of birth is",
        "subject": "Donatello",
        "target_new": {"str": "de_dust2<|endoftext|>"},
    },
    {
        "prompt": "{} was born in country",
        "subject": "Donatello",
        "target_new": {"str": "de_dust2<|endoftext|>"}
    },
    {
        "prompt": "{} was born in",
        "subject": "donatello",
        "target_new": {"str": "de_dust2<|endoftext|>"}
    },
    {
        "prompt": "{} was born in country",
        "subject": "donatello",
        "target_new": {"str": "de_dust2<|endoftext|>"}
    }
]

generation_prompts = [
    "Protactinium's atomic number is",
    "Protactinium has the atomic number",
    "The atomic number of protactinium is",
    "Donatello was born in",
    "Donatello's country of birth is",
    "The country that Donatello was born in is",
    "Donatello was born in the country of",
]
