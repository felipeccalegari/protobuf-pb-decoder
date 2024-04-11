# protobuf-pb-json-decoder

I wrote a decoder in Python for protobuf files with .pb extension where you don't need the original .proto files to work and will create a .json file with the decoded info from the .pb.
First you'll need to install the dependency with ```pip install blackboxprotobuf```.
To use the decoder, it's recommended to have the .pb files on the same folder as the python file and then use the following command:
```
python main.py your_pb_file.pb -o output_json_file.json
```
It's normal to have a lot of warning messages in the terminal while the decoder does his job, it worked with all the .pb files I have tested.
