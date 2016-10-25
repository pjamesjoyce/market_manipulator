"""Functions for market manipulations in Ocelot"""

import logging
from functools import partial

from ocelot import system_model, default_configuration
from ocelot.transformations.locations import link_markets    
from ocelot.transformations.utils import get_single_reference_product

from .utils import get_dataset_by_id


def read_edit_csv(filename, sep = ",", header=True):
    """read a csv file (column 0 = ids, column 1 = new production volumes) into the format required by edit_pv_of_reference_products"""
    with open(filename) as csvfile:

        my_edits = {}

        for i, line in enumerate(csvfile):
            if header == False or i>0:
                ls = line.strip().split(sep)
                my_edits[ls[0]]=ls[1]

        return my_edits


def edit_pv_of_reference_products(data, edits_to_make):
    """edit the production volumes of a set of activities
        this is specified in a dictionary with the keys as the ids and the values as the new production volume
        Note - this function is 'curried' with its dictionary to become edit_specified_pvs(data)"""
   
    for edit in edits_to_make:
        dataset = get_dataset_by_id(edit, data)
        ref_product = get_single_reference_product(dataset)
        original_pv = ref_product['production volume']['amount']
        new_pv = edits_to_make[edit]
        ref_product['production volume']['amount'] = float(new_pv)
        print ('Production volume for {} {} changed from {} to {}'.format(dataset['name'], dataset['location'],original_pv, new_pv))
        logging.info({
                'type': 'table element',
                'data': (dataset['name'], dataset['location'],original_pv, new_pv)
            })
    return data

edit_pv_of_reference_products.__table__ = {
    'title': 'Alter the production volume of specified transforming activities',
    'columns': ["Activity", "Location", "Original", "New"]
}

def system_model_with_pv_edits (data_path, edit_csv_file):
    
    my_edits = read_edit_csv(edit_csv_file)

    edit_specified_pvs = partial(edit_pv_of_reference_products, edits_to_make=my_edits)

    linking_function_index = default_configuration.index(link_markets)

    custom_configuration = list(default_configuration)
    custom_configuration.insert(linking_function_index, edit_specified_pvs)

    # run the system model
    fp, data = system_model(data_path, custom_configuration)
    
    return fp, data