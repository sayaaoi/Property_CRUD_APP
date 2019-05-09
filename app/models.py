from app import db, ma

# Property Class/Model
class Property(db.Model):
    PropertyID = db.Column(db.Integer, primary_key=True)
    PropertyName = db.Column(db.String(20), unique=True, nullable=False)
    City = db.Column(db.String(30), nullable=False)
    MarketValue = db.Column(db.Float, nullable=False)
    Cost = db.Column(db.Float, nullable=False)

    def __init__(self, PropertyName, City, MarketValue, Cost):
        self.PropertyName = PropertyName
        self.City = City
        self.MarketValue = MarketValue
        self.Cost = Cost

    def __repr__(self):
        return f"Property('{self.PropertyID}, {self.PropertyName},{self.City},{self.MarketValue},{self.Cost}')"

# Property Schema
class PropertySchema(ma.Schema):
    class Meta:
        fields = ('PropertyID', 'PropertyName', 'City', 'MarketValue', 'Cost')

# Init schema
property_schema = PropertySchema(strict=True)
properties_schema = PropertySchema(many=True, strict=True)