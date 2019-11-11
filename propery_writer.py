import csv

from property import Property


def write_properties(path, new_properties):
    template_property = Property(-1, '').as_map()

    with open(path, 'w') as file:
        dic_writer = csv.DictWriter(file, template_property.keys())
        dic_writer.writeheader()

        for new_property in new_properties:
            dic_writer.writerow(new_property.as_map())
