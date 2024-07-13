import pytest
from pages.eco_friendly_page import EcoFriendlyPage
from utils.assertions import Assertions
from test_data import expected_titles


@pytest.fixture
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


def test_load_eco_friendly_page(eco_friendly_page: EcoFriendlyPage) -> None:
    eco_friendly_page.load()
    Assertions.assert_equal(eco_friendly_page.page.title(), expected_titles["eco_friendly"], "Page title mismatch")


def test_eco_friendly_page_title(eco_friendly_page: EcoFriendlyPage) -> None:
    eco_friendly_page.load()
    title_text = eco_friendly_page.get_title_text()
    Assertions.assert_in("Eco Friendly", title_text, "Title text mismatch")


def test_eco_friendly_page_elements(eco_friendly_page: EcoFriendlyPage) -> None:
    eco_friendly_page.load()
    Assertions.assert_equal(eco_friendly_page.shopping_options_title.text_content(), "Shopping Options")
    Assertions.assert_equal(eco_friendly_page.sort_by_title.text_content(), "Sort By")
