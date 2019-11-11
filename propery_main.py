import logging
import time

import propery_reader
import propery_writer

back_off_seconds_between_requests = 5
max_num_pages = 20
price = 1500
post_code = 1110
output_path = "./property-list.csv"

logging.basicConfig(filename='execution.log', level=logging.DEBUG)

def main():
    logging.debug(
        "Starting scrapping with back_off_seconds_between_requests %s, max_num_pages %s, price %s, post_code %s ",
        back_off_seconds_between_requests, max_num_pages, price, post_code)

    page = 0
    new_properties = []

    while page < max_num_pages:

        try:

            logging.debug("Requesting page %s ", page)

            has_next_page, page_properties = propery_reader.read_properties(page, price, post_code)

            logging.debug("Page %s returned %s properties", page, len(page_properties))

            new_properties.extend(page_properties)

        except Exception as e:
            logging.exception("Exception requesting page: {}".format(page))
            break

        if has_next_page:
            page = page + 1
        else:
            break

        time.sleep(back_off_seconds_between_requests)

    logging.debug("Saving %s ", len(new_properties))

    propery_writer.write_properties(output_path, new_properties)


if __name__ == "__main__":
    main()
