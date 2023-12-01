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
shape_controlled_list = controlled_list_df['shape'].tolist()
function_controlled_list = controlled_list_df['function'].tolist()
flexibility_controlled_list = controlled_list_df['flexibility'].tolist()
opacity_controlled_list = controlled_list_df['opacity'].tolist()

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
        "identifier": pa.Column(str, checks=pa.Check.str_length(min_value=36, max_value=36)),
        "componentName": pa.Column(str, required=False, nullable=True),
        "description": pa.Column(str, required=False, nullable=True),
        "externalIdentifier": pa.Column(dict, required=False, nullable=True),
        "imageURLs": pa.Column(str, required=False, nullable=True),
        "LOWcode": pa.Column(str, required=False, nullable=True),
        "componentConstituents": pa.Column(str),
        "height": pa.Column(int, required=False, nullable=True),
        "heightDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
        "width": pa.Column(int, required=False, nullable=True),
        "widthDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
        "depth": pa.Column(int, required=False, nullable=True),
        "depthDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
        "volume": pa.Column(int, required=False, nullable=True),
        "volumeDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
        "weight": pa.Column(int),
        "weightTolerance": pa.Column(int),
        "weightToleranceType": pa.Column(str),
        "weightDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
        "shape": pa.Column(str, checks=pa.Check(lambda s: s.isin(shape_controlled_list)), required=False, nullable=True),
        "function": pa.Column(str, checks=pa.Check(lambda s: s.isin(function_controlled_list)), required=False, nullable=True),
        "flexibility": pa.Column(str, checks=pa.Check(lambda s: s.isin(flexibility_controlled_list)), required=False, nullable=True),
        "branding": pa.Column(bool),
        "componentEndOfLifeRoutes": pa.Column(str, required=False, nullable=True),
        "colour": pa.Column(str, required=False, nullable=True),
        "opacity": pa.Column(str, checks=pa.Check(lambda s: s.isin(opacity_controlled_list)), required=False, nullable=True),
        "loaned": pa.Column(bool),
        "reuseSystems": pa.Column(str, required=False, nullable=True),
        "partOfMultipack": pa.Column(bool),
        "recycledContent": pa.Column(int, required=False, nullable=True),
        "recycledContentClaims": pa.Column(str),
        "recyclability": pa.Column(bool, required=False, nullable=True),
        "recyclabilityClaims": pa.Column(str, required=False, nullable=True),
        "certification": pa.Column(bool, required=False, nullable=True),
        "certificationClaims": pa.Column(str, required=False, nullable=True),
        "manufacturedCountry": pa.Column(int, required=False, nullable=True),
        "updateDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern)),
        "releaseDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
        "discontinueDate": pa.Column(str, checks=pa.Check.str_matches(iso8601_date_pattern), required=False, nullable=True),
    },
    strict="filter",
    coerce=True
)


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
