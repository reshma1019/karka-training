details=[{"name":"Reshma",
        "place":"Panachamoodu",
        "hobbies":["listening music","gardening","cooking"],
        "SSLC":{"tamil":90,
                "english":98,
                "maths":94,
                "science":84,
                "social":91,}
        },
        {
        "name":"Devi priya",
        "place":"Aralvaimozhi",
        "hobbies":["Eating","playing dogs"],
        "SSLC":{"tamil":89,
                "english":88,
                "maths":70,
                "science":74,
                "social":81,}
        },
        {
        "name":"Ashwin Kumar",
        "place":"Nagarcovil",
        "hobbies":["playing cricket","watching movies","cooking"],
        "SSLC":{"tamil":80,
                "english":98,
                "maths":76,
                "science":84,
                "social":97,}
        },
        {
        "name":"Rabin",
        "place":"Ramanputhoor",
        "hobbies":["youtube" ,"games"],
        "SSLC":{"tamil":96,
                "english":88,
                "maths":80,
                "science":74,
                "social":71,}
        },
        {
        "name":"Kavish",
        "place":"Vadasery",
        "hobbies":["games","riding"],
        "SSLC":{"tamil":60,
                "english":78,
                "maths":88,
                "science":85,
                "social":96,}
        },
        {
        "name":"Sulebha",
        "place":"Panakudi",
        "hobbies":["watching tv","using mobile","listening music"],
        "SSLC":{"tamil":90,
                "english":68,
                "maths":93,
                "science":83,
                "social":99,}
        },
        {
        "name":"Rashika",
        "place":"vadasery",
        "hobbies":["listening music","watching tv","sleeping"],
        "SSLC":{"tamil":96,
                "english":88,
                "maths":67,
                "science":85,
                "social":93,}
        },
    ]
for i in details:
    tamil=i["SSLC"]["tamil"]
    english=i["SSLC"]["english"]
    maths=i["SSLC"]["maths"]
    science=i["SSLC"]["science"]
    social=i["SSLC"]["social"]
    total=tamil+english+maths+science+social
    print("\nTotal is:",total)
    percentage=(total/500)*100
    print("\npercentage is:",percentage)
    if percentage>90: 
        print("\nyou are elligible for maths biology")
    elif percentage>80:
        print("\nyou are elligible for computer science")
    elif percentage>75 and maths>98:
        print("\nyou are elligible for maths biology")
    elif percentage>70 and maths>90:
        print("\nyou are elligible for maths biology")












