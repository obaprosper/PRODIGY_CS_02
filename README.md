**Image Encryption Tool**  

This repository contains a simple Python program for image encryption and decryption using basic pixel manipulation techniques. It includes two methods: pixel swapping (Red and Blue channels) and XOR operation with a key. This tool is designed for educational purposes to demonstrate fundamental image processing and encryption concepts.  

**Note:** This tool provides very basic encryption and is not suitable for securing sensitive information.  

**Features**  
* **Pixel Swap Encryption/Decryption:** Scrambles an image by swapping the Red and Blue color channels of each pixel. This operation is easily reversible by performing the swap again.

* **XOR Encryption/Decryption:** Encrypts an image by applying a bitwise XOR operation with a user-provided integer key (0-255) to each Red, Green, and Blue component of every pixel. Decryption involves applying the same XOR operation again.

* **User-Friendly Command-Line Interface:** Guides the user through the encryption and decryption processes with clear prompts.

* **Error Handling:** Includes basic error handling for file not found issues and invalid key inputs.

**Prerequisites**  
Before running the tool, ensure you have the following installed:

* Python (This program was developed with python 3.13.5)

* Pillow library

* NumPy library

You can install the required Python libraries using pip:  

**Bash**  

**pip install Pillow numpy**  

**How to Use**
1. **Clone the Repository:**  
  If you haven't already, clone this repository to your local machine:

**Bash**   

**git clone https://github.com/obaprosper/PRODIGY_CS_02.git**
**cd PRODIGY_CS_02**

2. **Place Your Image:**
Place the image you want to encrypt or decrypt in the same directory as the image_encryption_tool.py file, or be prepared to provide its full path.  

3. **Run the Tool:**
Execute the Python script from your terminal:

**Bash**

**python image_encryption_tool.py**  

4. **Follow the Prompts:**  
The program will display a menu. Choose an option (1-5) and follow the on-screen instructions.

Simple Image Encryption Tool
----------------------------

Choose an option:
1. Encrypt Image (Pixel Swap)
2. Decrypt Image (Pixel Swap)
3. Encrypt Image (XOR Operation)
4. Decrypt Image (XOR Operation)
5. Exit
Enter your choice (1-5):

* **For XOR encryption/decryption:** You will be prompted to enter an integer key between 0 and 255. Remember this key as you'll need the exact same key for decryption.  

**Code Structure**
* **image_encryption_tool.py:**  

  * **encrypt_image_swap(image_path, output_path):** Encrypts an image by swapping R and B channels.

  * **decrypt_image_swap(image_path, output_path):** Decrypts an image by re-swapping R and B channels.

  * **encrypt_image_xor(image_path, output_path, key):** Encrypts an image using a bitwise XOR operation with a given key.

  * **decrypt_image_xor(image_path, output_path, key):** Decrypts an image by applying the XOR operation again with the same key.

  * **main():** The main function that provides the command-line interface and calls the encryption/decryption functions.  

**Examples** 
**Pixel Swap**
* **Original Image:**
(Replace with an actual screenshot or example image after running the tool)

* **Encrypted (Pixel Swap) Image:**
(Replace with an actual screenshot or example image after running the tool)

* **Decrypted (Pixel Swap) Image:**
(Replace with an actual screenshot or example image after running the tool)

**XOR Operation**
* **Original Image:**
(Same as above)

* **Encrypted (XOR) Image (with a key, e.g., 123):**
(Replace with an actual screenshot or example image after running the tool)

* **Decrypted (XOR) Image (with the same key):**
(Replace with an actual screenshot or example image after running the tool)  

**Note:** For the example images above, you would typically run the tool, save the output images, and then add them to a docs folder in your repository.  

**Important Security Disclaimer**
The encryption methods implemented in this tool (simple pixel swapping and XOR) are extremely weak and are not suitable for real-world security applications. They are provided purely for educational purposes to illustrate basic image manipulation concepts and the principles of reversible operations. Real-world image encryption uses much more complex cryptographic algorithms.  

**Contributing**  
Feel free to explore, modify, and improve this tool. If you have suggestions or find issues, please open an issue or submit a pull request.
