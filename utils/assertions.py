from playwright.sync_api import Locator


class Assertions:
    @staticmethod
    def assert_equal(actual: str, expected: str, message: str = None) -> None:
        assert actual == expected, message or f"Expected {expected}, but got {actual}"

    @staticmethod
    def assert_in(text: str, container: str, message: str = None) -> None:
        assert text in container, message or f"Expected '{text}' to be in '{container}'"

    @staticmethod
    def assert_element_visible(element: Locator, message: str = None) -> None:
        assert element.is_visible(), message or "Expected element to be visible"

    @staticmethod
    def assert_url_equal(actual: str, expected: str, message: str = None) -> None:
        assert actual == expected, message or f"Expected {expected}, but got {actual}"




