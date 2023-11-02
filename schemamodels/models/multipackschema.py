import pandera as pa
from pandera.typing import Series
from typing import Optional

# Define a regular expression to match ISO 8601 date format "YYYY-MM-DD"
iso8601_date_pattern = r"^\d{4}-\d{2}-\d{2}$"

# Define the controlled list of valid items
controlled_list = [
    "bm-material-type-0001", "bm-material-type-0002", "bm-material-type-0003", "bm-material-type-0004", "bm-material-type-0005"]


# import column from pandera as pa.column
schema = pa.DataFrameSchema(
    {
        "identifier": pa.Column(str),
        "baseMaterialName": pa.Column(str),
        "baseMaterialType": pa.Column(pa.String, checks=pa.Check(lambda s: s.isin(controlled_list))),
        "materialChemCID": pa.Column(int),
        "externalIdentifierKeys": pa.Column(str),
        "externalIdentifierValues": pa.Column(int),
        "certification": pa.Column(bool),
        "certificationClaims": pa.Column(str, nullable=True),
        "manufacturer": pa.Column(str),
        "manufacturedCountry": pa.Column(str),
        "updateDate": pa.Column(pa.String, checks=pa.Check.str_matches(iso8601_date_pattern)),
    },
    strict=True,
    coerce=True
)


# Define a function to validate and log errors
def validate_and_log_data(data):
    log_filename = 'validation_errors.log'
    with open(log_filename, 'w') as log_file:
        log_file.write("Schema Errors:\n")

    for row_index, (_, row) in enumerate(data.iterrows(), start=1):
        try:
            schema.validate(row.to_frame().T, lazy=True)
        except pa.errors.SchemaErrors as err:
            with open(log_filename, 'a') as log_file:
                log_file.write(f"Error #{row_index}:\n")
                for error_index, error_row in enumerate(err.failure_cases.iterrows(), start=1):
                    log_file.write(f"Error #{error_index}:\n")
                    for col_name, col_error in error_row[1].items():
                        log_file.write(f"{col_name}: {col_error}\n")
                log_file.write("\n")  # Add a separator between rows


# Define a function to read the log file contents
def read_log_file_contents():
    log_filename = 'validation_errors.log'
    try:
        with open(log_filename, 'r') as log_file:
            log_contents = log_file.read()
        return log_contents
    except FileNotFoundError:
        return "Log file not found"
