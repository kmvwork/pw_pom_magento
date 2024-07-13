import pytest
from pages.sale_page import SalePage
from utils.assertions import Assertions
from test_data import expected_titles


@pytest.fixture
def sale_page(page):
    return SalePage(page)


def test_load_sale_page(sale_page: SalePage) -> None:
    sale_page.load()
    Assertions.assert_equal(sale_page.page.title(), expected_titles["sale"], "Page title mismatch")


def test_sale_page_title(sale_page: SalePage) -> None:
    sale_page.load()
    title_text = sale_page.get_title_text()
    Assertions.assert_in("Sale", title_text, "Title text mismatch")


def test_sale_page_elements(sale_page: SalePage) -> None:
    sale_page.load()
    Assertions.assert_equal(sale_page.sale_page_header.text_content(), "Sale")
    Assertions.assert_equal(sale_page.women_deals_title.text_content(), "Women's Deals")
    Assertions.assert_equal(sale_page.men_deals_title.text_content(), "Mens's Deals")
