from fizz_buzz import fizz_buzz


class TestFizzBuzz:
    def test_fizz_buzz_passed_str(self):
        assert fizz_buzz(1) == "1"
        assert fizz_buzz(4) == "4"

    def test_fizz_buzz_passed_fizz(self):
        assert fizz_buzz(3) == "Fizz"
        assert fizz_buzz(6) == "Fizz"

    def test_fizz_buzz_passed_buzz(self):
        assert fizz_buzz(5) == "Buzz"
        assert fizz_buzz(10) == "Buzz"

    def test_fizz_buzz_passed_fizz_buzz(self):
        assert fizz_buzz(15) == "Fizz Buzz"
        assert fizz_buzz(30) == "Fizz Buzz"
