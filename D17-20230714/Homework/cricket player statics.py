players_statics=[  
                 {
                    "name":"MS Doni",
                    "number of centuries":16,
                    "half centuries":108,
                    "hat-trick wickets":0,
                    "top batting scores":[224,134,183,145,139], 
                 },
                 {
                    "name":"Devon Conway",
                    "number of centuries":3,
                    "half centuries":169,
                    "hat-trick wickets":0,
                    "top batting scores": [200,128,166,154,185],                      
                 },
                 {
                    "name":"Rashid khan",
                    "number of centuries":0,
                    "half centuries":136,
                    "hat-trick wickets":7,
                    "top batting scores": [79,80,60,50,69],    
                 },
                 {
                    "name":"Sam curran",
                    "number of centuries":4,
                    "half centuries":222,
                    "hat-trick wickets":7,
                    "top batting scores":[33,55,32,44,27],
                    
                 },
                 {
                    "name":"Steve Smith",
                    "number of centuries":44,
                    "half centuries":70,
                    "hat-trick wickets":6,
                    "top batting scores":[200,87,74,88,109],
                 },
            ]


def cricket_statics(players_statics):
   no_of_centuries=0
   hattrick_wickets=[]
   topbatting_score=[]
   
   
   for i in players_statics:
        
      if i["number of centuries"]>10:
         no_of_centuries=no_of_centuries+1
         
      if i["hat-trick wickets"]>5:
         hattrick_wickets.append(i["name"])
   
   score=0     
   for top in i["top batting scores"]:
   
      if top>score:
         score=top
   top_score={"name":i["name"],
              "top score":top},

   topbatting_score.append(top_score)

   
   print("\nNumber of players scored more than 10 centuries:",no_of_centuries)

   print("\nMore than 5 hat-trick:",hattrick_wickets)

   print("\nTop batting scores:\n",topbatting_score[0])

            
cricket_statics(players_statics)