my_resume={"Name":"Reshma s",
            "E-mail":"reshmakulapparai@gmail.com",
            "Mobile-no":7593964625,
            "Soft skills":["Comunication","time management","problem solving"],
            "Hard skills":["Python","MS office","html","css"],
            "Educational Qualification":[{"Qualification":"SSLC",
                                          "Institute":"St Mary's HSS Melpalai",
                                          "Percentage":80},
                                         {"Qualification":"HSC",
                                          "Institute":"St Mary's HSS Melpalai",
                                          "Percentage":63},
                                         {"Qualification":"BE",
                                          "Institute":"Mar Ephraem college of Engineering and Technology Elavuvilai",
                                          "Percentage":8.46}],
            "Projects":"Facial Feature Identification and Classification Using Convolutional Neural Network",
            "Experience":[{"Company name":"Infosys",
                           "Position":"Junior Software Developer",
                           "Duration":2},
                          {"Company name":"TCS",
                           "Position":"Software Developer",
                           "Duration":2.5},
                          {"Company name":"Wipro",
                           "Position":"Developer",
                           "Duration":3.5}],
            "Hobbies":["listening music","gardening","cooking"],
            "Personal details":{"father name":"Selvaraj M",
                                "Father's occupation":"coolie",
                                "Languages Known":["Tamil","Malayalam","English"],
                                "DOB":"19-3-2002",
                                "Gender":"Female",
                                "Martial Status":"Single",
                                "Address":{"Door no":"2/3/220",
                                           "Street":"Kulapparai",
                                           "Post":"Vellachipparai",
                                           "District":"Kanyakumari",
                                           "Pincode":629152,
                                           "State":"Tamilnadu"},
                                           
                                },
            }
# for skill in my_resume["Hard skills"]:
    
#     print(skill)

# for language in my_resume["Personal details"]["Languages Known"]:
#     print(language)

"""for qualification in my_resume["Educational Qualification"]:
    if qualification["Qualification"]=="HSC":
        print(qualification["Percentage"])"""

# for qualification in my_resume["Educational Qualification"]:
#     print(qualification["Qualification"],qualification["Percentage"])
     



"""if qualification["Qualification"]=="HSC":
        print(qualification["Qualification"],qualification["Percentage"])

     elif qualification["Qualification"]=="SSLC":
         print(qualification["Qualification"],qualification["Percentage"])

     elif qualification["Qualification"]=="BE":
        print(qualification["Qualification"],qualification["CGPA"])
"""
        


"""address=my_resume["Personal details"]["Address"]
for pincode in address:
    if pincode=="Pincode":
        print(address["Pincode"])
"""
"""for skills in my_resume:
    if skills=="Hard skills":
       print(my_resume[skills])"""

details=my_resume["Personal details"]
for key in details:
    value=details[key]
    print(key,value)



    
