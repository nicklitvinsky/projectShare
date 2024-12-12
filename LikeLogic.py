import VacationLogic

class Like:
    def __init__(self, user, vacation):
        self.user = user
        self.vacation = vacation
        self.liked = False

    def like(self):
        if not self.liked:
            self.vacation.likes += 1
            self.liked = True

    def unlike(self):
        if self.liked:
            self.vacation.likes -= 1
            self.liked = False

    def view_likes(self):
        return self.vacation.likes


vac = Vacation(
    title="Beach Trip", 
    country="Israel", 
    start_date=date(2025, 1, 1), 
    end_date=date(2025, 2, 1), 
    price=5000
)