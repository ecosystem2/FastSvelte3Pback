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
        "identifier": pa.Column(str, checks=pa.Check(lambda s: check_uuid4(s))),
        "componentName": pa.Column(str, required=False),
        "description": pa.Column(str, required=False),
        "externalIdentifier": pa.Column(dict, required=False),
        "imageURLs": pa.Column(list, required=False),
        "LOWcode": pa.Column(str, required=False),
        "componentConstituents": pa.Column(list),
        "height": pa.Column(int, required=False),
        "heightDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
        "width": pa.Column(int, required=False),
        "widthDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
        "depth": pa.Column(int, required=False),
        "depthDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
        "volume": pa.Column(int, required=False),
        "volumeDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
        "weight": pa.Column(int),
        "weightTolerance": pa.Column(int),
        "weightToleranceType": pa.Column(str),
        "weightDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
        "shape": pa.Column(pa.String, checks=pa.Check(lambda s: s.isin(shape_controlled_list)), required=False),
        "function": pa.Column(pa.String, checks=pa.Check(lambda s: s.isin(function_controlled_list)), required=False),
        "flexibility": pa.Column(pa.String, checks=pa.Check(lambda s: s.isin(flexibility_controlled_list)), required=False),
        "branding": pa.Column(bool),
        "componentEndOfLifeRoutes": pa.Column(list, required=False),
        "colour": pa.Column(str, required=False),
        "opacity": pa.Column(pa.String, checks=pa.Check(lambda s: s.isin(opacity_controlled_list)), required=False),
        "loaned": pa.Column(bool),
        "reuseSystems": pa.Column(list, required=False),
        "partOfMultipack": pa.Column(bool),
        "recycledContent": pa.Column(int, required=False),
        "recycledContentClaims": pa.Column(list),
        "recyclability": pa.Column(bool, required=False),
        "recyclabilityClaims": pa.Column(list, required=False),
        "certification": pa.Column(bool, required=False),
        "certificationClaims": pa.Column(list, required=False),
        "manufacturedCountry": pa.Column(int, required=False),
        "updateDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern)),
        "releaseDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
        "discontinueDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern), required=False),
    },
    strict=True,
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
