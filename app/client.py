class Client:
    def __init__(self,client_id: str, table_number: int, order: str):
        self.client_id = client_id
        self.table_number = table_number
        self.order = order
        self.history = []
        
    def place_order(self, order: str):
        self.order = order
        self.history.append(order)
        
    def place_takeaway_order(self, order: str):
        self.order = order
        self.history.append(order)
        
    def cancel_order(self):
        self.order = None
        
        
        
        
        
        
        
    