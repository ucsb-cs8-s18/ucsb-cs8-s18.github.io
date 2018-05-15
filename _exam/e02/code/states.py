states = {
 "AZ" : { "name": "Arizona",
          "capital" : "Phoenix",
          "largest": "Phoenix",
	  "baseball": ["Diamondbacks"] },
 "CA" : { "name": "California",
          "capital" : "Sacramento",
          "largest" : "Los Angeles",
          "baseball": ["Angels","Dogders","A's","Padres","Giants"] },
 "NV" : { "name" : "Nevada",
          "capital" : "Carson City",
          "largest" : "Las Vegas",
	  "baseball" : [] },
 "OR" : { "name" : "Oregon",
          "capital" : "Salem",
          "largest" : "Portland",
	  "baseball" : [] },	 
 "WA" : { "name" : "Washington",
          "capital" : "Olympia",
          "largest" : "Seattle",
	  "baseball" : ["Mariners"] },     
 }

def abbrevToName(states):
    " return a dictionary with abbrev as key, and state name as value"

    answer = {}
    for key in states:
        answer[key] = states[key]["name"]
    return answer

def listOfStatesWhereLargestIsCapital(states):

    answer=[]
    for key in states:
        if states[key]["capital"]==states[key]["largest"]:
            answer.append(states[key]["name"])
    return answer

def listOfStateAbbrevsWithBaseballTeams(states):

    answer=[]
    for key in states:
        if len(states[key]["baseball"])!=0:
            answer.append(key)
    return answer

def listOfStatesWithBaseballTeams(states):

    answer=[]
    for key in states:
        if states[key]["baseball"]==[]:
            answer.append(states[key]["name"])
    return answer



if __name__=="__main__":
  print('type(states["AZ"])',type(states["AZ"]))
  print('type(states["NV"]["name"])',type(states["NV"]["name"]))
  print('type(states["CA"]["baseball"])',type(states["CA"]["baseball"]))
  print('type(len(states["NV"]["baseball"]))',type(len(states["NV"]["baseball"])))
  print('type(states["WA"]["baseball"][0])',type(states["WA"]["baseball"][0]))
