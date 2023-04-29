import datetime

class datetimeDiscord:
    def __init__(self, dt):
        self.dt = dt
        self.formatted_date = self.dt.strftime("%a, %b %d, %Y %I:%M %p")
