from models.score import Score
import operator
import json
import datetime

class Board():
    def __init__(self,filename):
        self.filename = filename
        self.load_form_json()
    # load json file
    def load_form_json(self):
        with open(self.filename, 'r') as f:
            self.collection = json.load(f)
        self.name = self.collection["name"]
        self._score = self.collection["scores"] # get score dictionalry list
    
    # get students in Json file takes 1 optional argument if not set default list all studnet with names
    def get_scores(self,sorted_by = "score"):
        scoreList = []
        for item in self._score:
            scoreList.append(Score(item["name"],item["score"],item["date"]))
        if sorted_by == "score":
            scoreList=sorted(scoreList, key=operator.attrgetter("score"), reverse=True)
        return scoreList


    def to_dict(self):
        scoreList = []
        for item in self._score:
            scoreList.append(Score(item["name"],item["score"],item["date"]).to_dict())
        
        return {"name":self.collection["name"],"scores":scoreList}



    def add_score(self, name, score):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._score.append({"name": name,"score": score,"date": date})
        self.save()
        return True



    def save(self):
        json.dump(self.to_dict(), open(self.filename,"w"))
            

    

    def __len__(self):
        return len(self.collection)