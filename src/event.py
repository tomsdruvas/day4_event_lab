class Event:

    def __init__(self, name, ticket_price, performers):
        self.name = name
        self.ticket_price = ticket_price
        self.revenue = 0
        self.customers = []
        self.performers = performers

    def increase_revenue(self, amount):
        self.revenue += amount
        