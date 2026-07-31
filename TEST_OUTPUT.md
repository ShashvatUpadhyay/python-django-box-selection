# Test Report

## Automated Unit Tests

Command executed:

```bash
python manage.py test
```

Output:

```
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

...

----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK

Destroying test database for alias 'default'...
```

---

# Manual API Testing

## Test Case 1

### Scenario

Single product order.

### Request

```json
{
    "items": [
        {
            "product_id": 1,
            "quantity": 1
        }
    ]
}
```

### Expected Result

The system returns the smallest suitable shipping box.

### Actual Result

Small Box returned successfully.

### Status

PASS

---

## Test Case 2

### Scenario

Invalid product ID.

### Request

```json
{
    "items": [
        {
            "product_id": 999,
            "quantity": 1
        }
    ]
}
```

### Expected Result

The system returns an error indicating an invalid product ID.

### Actual Result

Error response returned successfully.

### Status

PASS

---

## Test Case 3

### Scenario

Quantity equal to zero.

### Request

```json
{
    "items": [
        {
            "product_id": 1,
            "quantity": 0
        }
    ]
}
```

### Expected Result

The system returns a validation error.

### Actual Result

Validation error returned successfully.

### Status

PASS

---

## Summary

| Test | Result |
|------|--------|
| Unit Tests | PASS |
| API Test 1 | PASS |
| API Test 2 | PASS |
| API Test 3 | PASS |

The application behaved as expected during both automated and manual testing.