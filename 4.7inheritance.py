# Write a program to implement Multilevel inheritance, Grandfather→Father-→Child to show property inheritance from grandfather to child.

class Grandfather:
    def __init__(self, assets):
        self.assets = assets

class Father(Grandfather):
    def __init__(self, assets, business):
        super().__init__(assets)
        self.business = business

class Child(Father):
    def __init__(self, assets, business, education):
        super().__init__(assets, business)
        self.education = education

grandfather_assets = 1000
father_assets = 5000
business_info = "Family Business"
child_education = "Computer Science Engineer"
#instance
grandfather = Grandfather(assets=grandfather_assets)
father = Father(assets=father_assets, business=business_info)
child = Child(assets=None, business=None, education=None)

child.assets = grandfather.assets + father.assets
child.business = father.business
child.education = child_education

print(f"\nGrandfather's assets: ₹{grandfather.assets}")
print(f"Father's assets: ₹{father.assets}")
print(f"Child's assets: ₹{child.assets}")
print(f"\nChild's business: {child.business}")
print(f"\nChild's education: {child.education}\n")
