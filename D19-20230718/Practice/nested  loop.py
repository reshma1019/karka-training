education_details=[{"Study":"BE",
                    "Institute":"Mar Ephraem",
                    "Semester_marks":[{"semester name":1,
                                       "subjects":["Engineering Mathematics","Engineering Physics","Chemistry","Python programming"," Engineering Graphics"],
                                       "semester grade":"A"},
                                      {"semester name":2,
                                       "subjects":["Electronic circuits","Engineering mathematics 2","Electronic devices","English"," Engineering Graphics"],
                                       "semester grade":"B"}],

                },
                ]

for item in education_details:
    print(item["Study"])
    marks=item["Semester_marks"]
    for sem in marks:
        print(sem["semester name"],sem["subjects"])