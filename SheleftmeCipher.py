class Sheleftme:
    @staticmethod
    def text_to_binary(text):
        return ''.join(format(ord(char), '08b') for char in text)

    @staticmethod
    def binary_to_text(binary):
        binary_int = int(binary, 2)
        byte_number = (binary_int.bit_length() + 7) // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode()
        return ascii_text

    @staticmethod
    def encode_message(message):
        binary_message = Sheleftme.text_to_binary(message)
        encoded_message = ''.join('\u200B' if bit == '0' else '\u200C' for bit in binary_message)
        return encoded_message

    @staticmethod
    def decode_message(encoded_message):
        binary_message = ''.join('0' if char == '\u200B' else '1' for char in encoded_message)
        decoded_message = Sheleftme.binary_to_text(binary_message)
        return decoded_message

    @staticmethod
    def embed_message_in_text(cover_text, encoded_message):
        cover_length = len(cover_text)
        message_length = len(encoded_message)
        
        interval = max(1, cover_length // message_length)
        embedded_text = ""
        index = 0

        for i in range(cover_length):
            embedded_text += cover_text[i]
            if index < message_length and (i + 1) % interval == 0:
                embedded_text += encoded_message[index]
                index += 1

        if index < message_length:
            embedded_text += encoded_message[index:]

        return embedded_text

    @staticmethod
    def extract_message_from_text(embedded_text):
        encoded_message = ''.join(char for char in embedded_text if char in ['\u200B', '\u200C'])
        return Sheleftme.decode_message(encoded_message)
