from django.test import TestCase
from .models import Product, Box
from .services import recommend_box


class RecommendBoxTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=3,
            weight=2
        )

        Box.objects.create(
            name="Small Box",
            length=35,
            width=25,
            height=10,
            max_weight=3,
            cost=40
        )

        Box.objects.create(
            name="Medium Box",
            length=50,
            width=35,
            height=20,
            max_weight=10,
            cost=70
        )

    def test_recommend_box(self):

        result = recommend_box([
            {
                "product_id": self.product.id,
                "quantity": 1
            }
        ])

        self.assertEqual(result.name, "Small Box")

    def test_invalid_product(self):

        result = recommend_box([
            {
                "product_id": 999,
                "quantity": 1
            }
        ])

        self.assertEqual(result["error"], "Invalid product ID.")

    def test_invalid_quantity(self):

        result = recommend_box([
            {
                "product_id": self.product.id,
                "quantity": 0
            }
        ])

        self.assertEqual(result["error"], "Quantity must be greater than zero.")