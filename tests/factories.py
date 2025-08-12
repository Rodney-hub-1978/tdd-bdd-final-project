import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category, db


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Creates fake products and saves them to the database"""

    class Meta:
        model = Product
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"  # commit after creation

    id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(
        choices=[
            "Hat",
            "Pants",
            "Shirt",
            "Apple",
            "Banana",
            "Pots",
            "Towels",
            "Ford",
            "Chevy",
            "Hammer",
            "Wrench",
        ]
    )
    description = factory.Faker("text")
    price = FuzzyDecimal(0.5, 2000.0, 2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )


if __name__ == "__main__":
    # Example usage: create & save a product in DB
    product = ProductFactory()
    print(
        product.id,
        product.name,
        product.description,
        product.price,
        product.available,
        product.category,
    )
