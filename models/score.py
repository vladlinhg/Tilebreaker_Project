from datetime import datetime

class Score():
    def __init__(self,name,score,date=None):
        self.name = name
        self.score = score
        if date:
            self.date = date
        else:
            self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    @property

    def to_dict(self):
        return {"name": self.name,"score": self.score,"date": self.date}
        
        
    