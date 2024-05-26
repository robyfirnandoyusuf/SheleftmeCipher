import streamlit as st
import base64
from SheleftmeCipher import Sheleftme

class SheleftmeApp:
    def __init__(self):
        self.steg = Sheleftme()
        self.run()

    def run(self):
        st.title('SheleftmeCipher: Hide your love message with invisible Unicode characters. \U0001F494')

        operation = st.selectbox("Operation:", ["Encode", "Decode"])

        message = st.text_area("Message (Can be encoded or decoded):")

        if operation == "Encode":
            masking_text = st.text_input("Masking Text (For encoding):")
        else:
            masking_text = ""

        result = ""

        if st.button("Execute"):
            if operation == "Encode":
                if message and masking_text:
                    encoded_message = self.steg.encode_message(message)
                    result = self.steg.embed_message_in_text(masking_text, encoded_message)
                else:
                    st.error("Please provide both a message and masking text for encoding.")
            elif operation == "Decode":
                if message:
                    result = self.steg.extract_message_from_text(message)
                else:
                    st.error("Please provide a message to decode.")

        if result:
            st.markdown("### Result:")
            encoded_result = base64.b64encode(result.encode('utf-8')).decode('utf-8')
            html_result = f'''
                <textarea rows="10" cols="80" id="result_area">{result}</textarea>
                <button onclick="copyToClipboard()">Copy to Clipboard</button>
                <script>
                    function copyToClipboard() {{
                        var copyText = document.getElementById("result_area");
                        copyText.select();
                        document.execCommand("copy");
                    }}
                </script>
            '''
            st.markdown(html_result, unsafe_allow_html=True)

if __name__ == "__main__":
    SheleftmeApp()
