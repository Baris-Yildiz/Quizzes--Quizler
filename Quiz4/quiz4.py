import sys
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
message_dict = dict()
message_IDs = list()

with open(input_file_name) as input_file:
    for line in input_file:     # stores messages IDs, packet IDs and message texts in the input file to a dictionary 'message_dict' mapped as {message_ID : {packet_ID : message1, packet_ID: message2...}, ...}
        contents = line.split("\t")
        message_ID, packet_ID, message = int(contents[0]), int(contents[1]), contents[2].rstrip("\n")
        if message_ID not in message_dict:
            message_dict[message_ID] = {packet_ID: message}
            message_IDs.append(message_ID)      # also stores the message IDs in a separate list to sort them later.
        else:
            message_dict[message_ID][packet_ID] = message

message_IDs.sort()  # sorts the message IDs

with open(output_file_name, "w") as output_file:    # this block of code will gather every message's message ID, packet ID and message text in a sorted manner and write it to the output file
    for messageID in message_IDs:    # iterate over each message ID starting from the smallest to the largest.
        output_file.write(f"Message {message_IDs.index(messageID) + 1}\n")
        for packetID in range(len(message_dict[messageID])):
            output_file.write(f"{messageID}\t{packetID}\t{message_dict[messageID][packetID]}\n")
