# market_manipulator
Multifunctional market manipulator (in python) plugin for ocelot

# Installation

Install via pip:
```
pip install https://github.com/pjamesjoyce/market_manipulator/zipball/master
```

# Use

## Preparing the external data

Each transforming process in the ecoinvent database is identified by a universally unique identifier.
These can be found in the [activity overview](http://www.ecoinvent.org/support/documents-and-files/information-on-ecoinvent-3/information-on-ecoinvent-3.html) spreadsheet available from the econinvent website.

The file used to manipulate the markets consists of two columns, one for uuid, and one for the new production volume.

For example:

|                uuid                |production volume|
|:----------------------------------:|----------------:|
|7f093291-b86f-40c8-933e-90b18711a515|123456           |
|be256386-9de6-43c3-8b1f-0dacdce19312|756543           |
|...                                 |...              |

The default setting for reading the file is separated by commas, with a header row, i.e.:

```
uuid,"production volume"
7f093291-b86f-40c8-933e-90b18711a515,123456
be256386-9de6-43c3-8b1f-0dacdce19312,756543
```

## Creating the system model

```python
from market_manipulator import system_model_with_pv_edits

new_pv_file = "path/to/edits.csv"

data_path = "path/to/unlinked/ecospold/files/folder"

fp, data = system_model_with_pv_edits(data_path, new_pv_file)
```

## Checking the results

```python
from market_manipulator.outputs import list_techno_inputs

process_id = "92bb65cf-89fa-45f1-9b40-38d762e16805"
list_techno_inputs(process_id, data)

```