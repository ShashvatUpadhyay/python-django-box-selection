from .models import Product, Box
from django.core.exceptions import ObjectDoesNotExist


def recommend_box(items):
    total_weight = 0
    total_volume = 0

    try:
        for item in items:
            product = Product.objects.get(id=item["product_id"])
            quantity = int(item.get("quantity", 1))

            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            total_weight += product.weight * quantity
            total_volume += (
                product.length *
                product.width *
                product.height *
                quantity
            )

    except ObjectDoesNotExist:
        return {
            "error": "Invalid product ID."
        }

    except ValueError as e:
        return {
            "error": str(e)
        }

    suitable_boxes = []

    for box in Box.objects.all():

        box_volume = box.length * box.width * box.height

        if (
            total_weight <= box.max_weight and
            total_volume <= box_volume
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    suitable_boxes.sort(
        key=lambda b: (
            float(b.cost),
            b.length * b.width * b.height
        )
    )

    return suitable_boxes[0]