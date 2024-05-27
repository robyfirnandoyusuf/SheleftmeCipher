# SheleftmeCipher: Steganography with Invisible Unicode Characters 💔

This project demonstrates how to use invisible Unicode characters to perform steganography. You can encode hidden messages into cover text using zero-width spaces and zero-width non-joiners, and decode them back. The application is built using Streamlit for a user-friendly interface.

## Project Structure

- `SheleftmeCipher.py`: Contains the `Sheleftme` class with methods for encoding, decoding, embedding, and extracting messages.
- `app.py`: Contains the `SheleftmeApp` class and runs the Streamlit application.

## Installation

1. Clone the repository

2. Install the required packages:
    ```sh
    pip install streamlit
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the interface to encode or decode messages:
    - **Encode**: Select "Encode" from the operation dropdown, provide the message and masking text, and click "Execute". The encoded message will be displayed, and you can copy it to the clipboard.
    - **Decode**: Select "Decode" from the operation dropdown, provide the encoded message, and click "Execute". The decoded message will be displayed.

## Example

### Encoding

1. Select "Encode" from the operation dropdown.
2. Enter your hidden message in the "Message" text area.
3. Enter the cover text in the "Masking Text" input field.
4. Click "Execute" to see the result.

### Decoding

1. Select "Decode" from the operation dropdown.
2. Enter the encoded message in the "Message" text area.
3. Click "Execute" to see the decoded message.

## Files

### `SheleftmeCipher.py`

Contains the `Sheleftme` class with the following methods:
- `text_to_binary(text)`: Converts text to binary representation.
- `binary_to_text(binary)`: Converts binary to text.
- `encode_message(message)`: Encodes a message using zero-width Unicode characters.
- `decode_message(encoded_message)`: Decodes a message from zero-width Unicode characters.
- `embed_message_in_text(cover_text, encoded_message)`: Embeds an encoded message in cover text.
- `extract_message_from_text(embedded_text)`: Extracts and decodes a message from text containing zero-width Unicode characters.

### `app.py`

Contains the `SheleftmeApp` class which runs the Streamlit application. It handles user input, performs encoding or decoding, and displays the result.

## License

This project is licensed under the MIT License.
