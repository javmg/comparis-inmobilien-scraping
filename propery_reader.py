
import re
import logging
from datetime import datetime
from urllib.request import urlopen

from bs4 import BeautifulSoup

import utils
from property import Property


def read_properties(page, price_from, postcode):
    request_object = {
        "DealType": "10",
        "PriceFrom": price_from,
        "WithImagesOnly": False,
        "LocationSearchString": postcode
    }

    request_object_encoded = utils.encode_request_object(request_object)

    url = "https://en.comparis.ch/immobilien/result/list?requestobject={}&page={}&sort=3&isAjaxDataLoading=true".format(
        request_object_encoded,
        page
    )

    logging.debug("Requesting url: %s", url)

    html = urlopen(url)

    content = "<html><body>" + str(html.read()) + "</body></html>"

    bs = BeautifulSoup(content, "html.parser")

    properties = []

    property_links = bs.find_all("a", href=lambda a: a is not None and "details" in a,
                                 class_=lambda c: c is not None and c == "title")

    for property_link in property_links:
        property_id = re.findall(r'\d+', property_link["href"])[0]
        property_title = property_link.getText()

        new_property = Property(id=property_id, title=property_title)

        fill_with_published_date(new_property, property_link)
        fill_with_address(new_property, property_link)
        fill_with_price(new_property, property_link)
        fill_with_specifications(new_property, property_link)

        properties.append(new_property)

    pagination_tag_li = bs.find("", class_=lambda c: c is not None and c == "pagination-next")

    if pagination_tag_li is None:
        return False, properties

    has_next_page = pagination_tag_li.find("a", href=lambda a: a is not None) is not None

    return has_next_page, properties


def fill_with_published_date(new_property, property_link):
    published_date_tag_time = property_link.find_next("time")

    if published_date_tag_time is None:
        return

    new_property.published_date = datetime.strptime(published_date_tag_time["datetime"], '%d/%m/%Y').date()


def fill_with_address(new_property, property_link):
    address_tag_address = property_link.find_next("address")

    if address_tag_address is None:
        return

    address_parts = address_tag_address.getText().split("\\r\\n")[1:-1]

    new_property.address = ' | '.join(x.strip() for x in address_parts)


def fill_with_price(new_property, property_link):
    price_div = property_link.find_next("div", class_=lambda c: c is not None and c == "item-price")

    if price_div is None:
        return

    price_with_only_digits = utils.filter_digits_in_string(price_div.getText())

    if not price_with_only_digits:
        return

    new_property.price = float(price_with_only_digits)


def fill_with_specifications(new_property, property_link):
    specifications_tag_div = property_link.find_next("ul", class_=lambda c: c is not None and c == "specifications")

    if specifications_tag_div is None:
        return

    specification_tags_li = specifications_tag_div.find_all("li")

    num_specifications = len(specification_tags_li)

    if num_specifications == 0:
        return

    new_property.category = specification_tags_li[0].getText()

    for index in range(1, 4):

        if index >= num_specifications:
            return

        specification_value = specification_tags_li[index].getText()
        specification_lower_cased_value = specification_value.lower()

        if 'floor' in specification_lower_cased_value:
            new_property.floor = specification_value
        elif 'm²' in specification_lower_cased_value:
            meters = utils.filter_in_string(specification_value, lambda c: c.isdigit() and c is not '²')
            new_property.meters = None if meters is None else int(meters)
        elif 'rooms' in specification_lower_cased_value:
            rooms = utils.filter_in_string(specification_value, lambda c: c.isdigit() or c is '½')
            new_property.rooms = None if rooms is None else float(rooms.replace("½", ".5"))
        else:
            new_property.category = specification_value
