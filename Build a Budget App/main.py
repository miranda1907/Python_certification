class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({
          'amount': amount, 'description': description  
        })


    def withdraw(self, amount, description=""):

        if not self.check_funds(amount):
            return False
        
        self.ledger.append({'amount': - amount, 'description': description}) 
        return True    

    def get_balance(self):
        
        return sum(amount["amount"] for amount in self.ledger)

    def transfer(self, amount, other_category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, description = "Transfer to " + other_category.name)
        other_category.deposit(amount, description = "Transfer from " + self.name)
        return True     

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True    

    def __str__(self):
        output = self.name.center(30,"*") +"\n"
 
        for transaction in self.ledger:
            description = transaction["description"][:23].ljust(23)
            amount = f'{transaction["amount"]:.2f}'.rjust(7)
      
            output += f"{description}{amount}\n"
        output += f"Total: {self.get_balance():.2f}"   
        return output  


def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    total_spent = 0

    for category in categories:
        for amount in category.ledger:
            if amount["amount"] < 0:
                total_spent += abs(amount["amount"])
    spending_percentages = []

    for category in categories:
        category_spent = 0
        for amount in category.ledger:
            if amount["amount"] < 0:
                category_spent += abs(amount["amount"])

        if total_spent > 0:
            percentage = category_spent/total_spent * 100
            spending_percentages.append(percentage//10 * 10)      

    for num in range(100, -10, -10):
        bars = ""
          
        for percentage in spending_percentages:
            if percentage >= num:
                bars += "o  "
            else:
                bars += "   " 

        output += f"{str(num).rjust(3)}| {bars}\n"
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"        

    max_length = max(len(category.name) for category in categories)

    for index in range(0,max_length):
        line = ""
        for i, category in enumerate(categories):
            if len(category.name) > index:
                line += category.name[index]
            else:
                line += " " 
            
            line += "  "  
        output += f"     {line}\n"
            
    output = output.removesuffix("\n")
    return output
