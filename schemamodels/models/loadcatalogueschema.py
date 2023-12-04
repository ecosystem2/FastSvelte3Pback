import pandera as pa
import pandas as pd
from pandera.typing import Series
from typing import Optional
import uuid
import json

# Define a regular expression to match ISO 8601 date format "YYYY-MM-DD"
iso8601_date_pattern = r"^\d{4}-\d{2}-\d{2}$"

# Load the CSV file as a controlled list
controlled_list_df = pd.read_csv(
    './schemamodels/models/controlled_lists/list_of_lists_nov23.csv')
# Replace 'column_name' with the actual column name in your CSV
level_controlled_list = controlled_list_df['level'].tolist()

# Custom check function for UUID4 format
# previous check was pa.Check.str_length(36),


def check_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


# import column from pandera as pa.column
# strict='filter' will drop columns not in the schema from the validation process
# add missing columns - will print a return schema that indicates missing columns - with a value of NaN if no default is declared.
schema = pa.DataFrameSchema(
    {
        "identifier": pa.Column(str, checks=pa.Check.str_length(min_value=36, max_value=36)),
        "loadCatalogueName": pa.Column(str, nullable=True, required=False),
        "description": pa.Column(str, nullable=True, required=False),
        "externalIdentifier": pa.Column(dict, nullable=True, required=False),
        "loadIdentifiers": pa.Column(str),
        "packagingItems": pa.Column(str),
        "quantityInLoad": pa.Column(int),
        "level": pa.Column(str, checks=pa.Check(lambda s: s.isin(level_controlled_list)), nullable=True, required=False),
        "updateDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern)),
    },
    strict="filter",
    coerce=True
)


# lazy=true gives an overview of validation errors
# Define a function to validate and log errors
# lazy=true gives an overview of validation errors
# Define a function to validate and log errors


def validateAndLog(data):
    validation_results = []

    def validate_row(row):
        try:
            schema.validate(row.to_frame().T, lazy=True)
        except pa.errors.SchemaErrors as err:
            error_info = {
                'row_index': row.name,
                'schema_errors': err.failure_cases.to_dict(orient='records'),
                'failed_data': err.data.to_dict(orient='records')
            }
            validation_results.append(error_info)

    data.apply(validate_row, axis=1)
    print(json.dumps(validation_results, indent=4))
    return json.dumps(validation_results, indent=4)
