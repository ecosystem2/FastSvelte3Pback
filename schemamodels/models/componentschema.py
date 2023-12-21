import pandera as pa
import pandas as pd
from pandera.typing import Series
from typing import List, Dict
import uuid
import json

# Define a regular expression to match ISO 8601 date format "YYYY-MM-DD"
iso8601_date_pattern = r"^\d{4}-\d{2}-\d{2}$"

# Load the CSV file as a controlled list
controlled_list_df = pd.read_csv(
    './schemamodels/models/controlled_lists/list_of_lists_nov23.csv')
# Replace 'column_name' with the actual column name in your CSV
shape_controlled_list = controlled_list_df['shape'].tolist()
function_controlled_list = controlled_list_df['function'].tolist()
flexibility_controlled_list = controlled_list_df['flexibility'].tolist()
opacity_controlled_list = controlled_list_df['opacity'].tolist()
reuse_controlled_list = controlled_list_df['reuse system'].tolist()


# Load country codes
country_codes_df = pd.read_csv(
    './schemamodels/models/controlled_lists/countryCodes.csv')

# Replace with the actual column name in your CSV
country_code_strings = country_codes_df['NumericString_Quoted'].tolist()
# Custom check function for UUID4 format
# previous check was pa.Check.str_length(36),


def check_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


# import column from pandera as pa.column
schema = pa.DataFrameSchema(
    {
        "identifier": pa.Column(str, checks=pa.Check.str_length(min_value=36, max_value=36, error="entries must be a valid and unique 36 character UUID"), unique=True),
        "name": pa.Column(str, nullable=True, required=False),
        "description": pa.Column(str, nullable=True, required=False),
        "externalIdentifiers": pa.Column(Dict, nullable=True, required=False),
        "imageURLs": pa.Column(List, nullable=True, required=False),
        "LOWcode": pa.Column(str, nullable=True, required=False),
        "componentConstituents": pa.Column(List),
        "height": pa.Column(float, coerce=True, nullable=True, required=False),
        "heightDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
        "width": pa.Column(float, coerce=True, nullable=True, required=False),
        "widthDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
        "depth": pa.Column(float, coerce=True, nullable=True, required=False),
        "depthDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
        "volume": pa.Column(float, coerce=True, nullable=True, required=False),
        "volumeDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
        "weight": pa.Column(int),
        "weightTolerance": pa.Column(float),
        "weightToleranceType": pa.Column(str),
        "weightDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
        "shape": pa.Column(str, checks=pa.Check(lambda s: s.isin(shape_controlled_list), error="String values must be from the controlled list."), nullable=True, required=False),
        "function": pa.Column(str, checks=pa.Check(lambda s: s.isin(function_controlled_list), error="String values must be from the controlled list."), nullable=True, required=False),
        "flexibility": pa.Column(str, checks=pa.Check(lambda s: s.isin(flexibility_controlled_list), error="String values must be from the controlled list."), nullable=True, required=False),
        "branding": pa.Column(bool),
        "componentEndOfLifeRoutes": pa.Column(List, nullable=True, required=False),
        "colour": pa.Column(str, nullable=True, required=False),
        "opacity": pa.Column(str, checks=pa.Check(lambda s: s.isin(opacity_controlled_list), error="String values must be from the controlled list."), nullable=True, required=False),
        "loaned": pa.Column(bool),
        "reuseSystems": pa.Column(List, checks=pa.Check(
            lambda s: all(
                (isinstance(val, list) and all(
                    subval in reuse_controlled_list for subval in val))
                or
                (isinstance(val, str) and val in reuse_controlled_list)
                for val in s
            ),
            element_wise=True,
            error="List values must be from the controlled list."
        )),
        "partOfMultipack": pa.Column(bool),
        "recycledContent": pa.Column(float, coerce=True, nullable=True, required=False),
        "recycledContentClaims": pa.Column(List),
        "recyclability": pa.Column(bool, nullable=True, required=False),
        "recyclabilityClaims": pa.Column(str, nullable=True, required=False),
        "certification": pa.Column(bool, nullable=True, required=False),
        "certificationClaims": pa.Column(List, nullable=True, required=False),
        "manufacturedCountry": pa.Column(str, checks=pa.Check(lambda s: s.isin(country_code_strings), error="Countries must be entered as valid ISO3166 Numeric Strings"), nullable=True, required=False),
        "updateDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd")),
        "releaseDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
        "discontinueDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern, error="Date values must be in ISO8601 format: yyyy-mm-dd"), nullable=True, required=False),
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
