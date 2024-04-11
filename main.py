# Import the required modules
import sys
import argparse
import json
import struct
import blackboxprotobuf # or protobuf_decoder

# Function to convert Fixed64 fields to float or double
# Function to convert Fixed64 fields to double
# Function to convert Fixed64 fields to double
def convert_fixed64_fields(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) or isinstance(value, list):
                convert_fixed64_fields(value)
            else:
                try:
                    # Check if the value can be converted to an integer
                    int_value = int(value)
                    # Interpret as double
                    value_as_double = struct.unpack('<d', struct.pack('<Q', int_value))[0]
                    # Replace the original value with the converted value
                    obj[key] = value_as_double
                except ValueError:
                    print(f"Warning: Value '{value}' cannot be converted to an integer. Keeping original value.")
                except struct.error:
                    print(f"Warning: Could not convert value '{value}' to double. Keeping original value.")
    elif isinstance(obj, list):
        for i in range(len(obj)):
            if isinstance(obj[i], dict) or isinstance(obj[i], list):
                convert_fixed64_fields(obj[i])
            else:
                try:
                    # Check if the value can be converted to an integer
                    int_value = int(obj[i])
                    # Interpret as double
                    value_as_double = struct.unpack('<d', struct.pack('<Q', int_value))[0]
                    # Replace the original value with the converted value
                    obj[i] = value_as_double
                except ValueError:
                    print(f"Warning: Value '{obj[i]}' cannot be converted to an integer. Keeping original value.")
                except struct.error:
                    print(f"Warning: Could not convert value '{obj[i]}' to double. Keeping original value.")

# Create a parser for the command-line arguments
parser = argparse.ArgumentParser(description="Decode protobuf messages without a schema file")
parser.add_argument("path", help="The path of the .pb file to decode")
parser.add_argument("-o", "--output", help="The output file name. If not specified, write to standard output")
args = parser.parse_args()

# Read the .pb file from the given path
with open(args.path, "rb") as f:
    data = f.read()

# Decode the message using blackboxprotobuf or protobuf_decoder
message, typedef = blackboxprotobuf.protobuf_to_json(data) # or protobuf_decoder.decode_message(data)

# Convert the message string into a JSON object
message = json.loads(message)

# Convert Fixed64 fields to double
convert_fixed64_fields(message)

formatted_json_str = json.dumps(message, indent=2, sort_keys=True)

# Write the JSON string to the output file or standard output
if args.output:
    with open(args.output, "w") as f:
        f.write(formatted_json_str)
else:
    print(formatted_json_str)
