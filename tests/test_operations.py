import pytest
from typing import Union
from app.operation import Operation

Number = Union[int, float]


@pytest.mark.parametrize(
      "a, b, expected",
      [
         (1, 1, 2),
         (-1, 1, 0),
         (-5.5, 3.5, -2.0),
      ],
      ids=[
         "add_two_positive_integers",
         "add_negative_and_positive_integer",
         "add_negative_float_and_positive_float",
      ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
  result = Operation.addition(a, b)
  assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
      "a, b, expected",
      [
         (3, 1, 2),
         (-1, 1, -2),
         (-5.5, 3.5, -9.0),
      ],
      ids=[
         "subtract_smaller_positive_integer_from_larger",
         "subtract_positive_integer_from_negative_integer",
         "subtract_two_floats",
      ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
  result = Operation.subtraction(a, b)
  assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
      "a, b, expected",
      [
         (3, 1, 3),
         (-1, 1, -1),
         (-4.5, 4.0, -18.0),
      ],
      ids=[
         "multiply_two_positive_integers",
         "multiply_positive_and_negative_integers",
         "multiply_floats",
      ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
  result = Operation.multiplication(a, b)
  assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
      "a, b, expected",
      [
         (3, 1, 3),
         (-4, 2, -2),
         (-12.0, 4.0, -3.0),
      ],
      ids=[
         "divide_two_positive_integers",
         "divide_positive_and_negative_integers",
         "divide_floats",
      ]
)
def test_division(a: Number, b: Number, expected: Number) -> None:
  result = Operation.division(a, b)
  assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}" 


@pytest.mark.parametrize(
      "a, b",
      [
         (3, 0),
         (0, 0),
         (-1, 0),
      ],
      ids=[
         "divide_positive_integer_by_zero",
         "divide_zero_by_zero",
         "divide_negative_integer_by_zero",
      ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
  with pytest.raises(ValueError, match="Division by zero is not allowed."):
      Operation.division(a, b)
    
