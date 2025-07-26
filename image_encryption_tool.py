from PIL import Image
import numpy as np
import os

def encrypt_image_swap(image_path, output_path):
    """
    Encrypts an image by swapping adjacent pixel values (R, G, B channels).
    This is a very basic form of encryption and primarily for demonstration.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)
        
        # Get image dimensions
        rows, cols, _ = pixels.shape

        # Simple swapping: swap R and B channels for each pixel
        encrypted_pixels = pixels.copy()
        encrypted_pixels[:, :, [0, 2]] = encrypted_pixels[:, :, [2, 0]] # Swap R (index 0) and B (index 2)

        encrypted_img = Image.fromarray(encrypted_pixels)
        encrypted_img.save(output_path)
        print(f"Image encrypted by swapping pixels and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image_swap(image_path, output_path):
    """
    Decrypts an image encrypted by swapping adjacent pixel values (R, G, B channels).
    This undoes the simple swap performed by encrypt_image_swap.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        # Undo the swapping: swap B and R channels back
        decrypted_pixels = pixels.copy()
        decrypted_pixels[:, :, [0, 2]] = decrypted_pixels[:, :, [2, 0]] # Swap R (index 0) and B (index 2) again

        decrypted_img = Image.fromarray(decrypted_pixels)
        decrypted_img.save(output_path)
        print(f"Image decrypted by swapping pixels back and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def encrypt_image_xor(image_path, output_path, key):
    """
    Encrypts an image by applying a XOR operation with a given key to each pixel's R, G, B values.
    The key should be an integer between 0 and 255.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        # Apply XOR operation to each channel of each pixel
        encrypted_pixels = pixels ^ key

        encrypted_img = Image.fromarray(encrypted_pixels.astype(np.uint8)) # Ensure data type is uint8
        encrypted_img.save(output_path)
        print(f"Image encrypted by XORing with key {key} and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

def decrypt_image_xor(image_path, output_path, key):
    """
    Decrypts an image by applying a XOR operation with the same key to each pixel's R, G, B values.
    XORing with the same key twice restores the original value.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        # Apply XOR operation again to decrypt
        decrypted_pixels = pixels ^ key

        decrypted_img = Image.fromarray(decrypted_pixels.astype(np.uint8)) # Ensure data type is uint8
        decrypted_img.save(output_path)
        print(f"Image decrypted by XORing with key {key} back and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

def main():
    print("Simple Image Encryption Tool")
    print("----------------------------")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt Image (Pixel Swap)")
        print("2. Decrypt Image (Pixel Swap)")
        print("3. Encrypt Image (XOR Operation)")
        print("4. Decrypt Image (XOR Operation)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            input_image_path = input("Enter the path to the image to encrypt: ")
            output_image_path = input("Enter the desired output path for the encrypted image (e.g., encrypted_swap.png): ")
            encrypt_image_swap(input_image_path, output_image_path)
        elif choice == '2':
            input_image_path = input("Enter the path to the encrypted image to decrypt: ")
            output_image_path = input("Enter the desired output path for the decrypted image (e.g., decrypted_swap.png): ")
            decrypt_image_swap(input_image_path, output_image_path)
        elif choice == '3':
            input_image_path = input("Enter the path to the image to encrypt: ")
            output_image_path = input("Enter the desired output path for the encrypted image (e.g., encrypted_xor.png): ")
            try:
                key = int(input("Enter an integer key for XOR operation (0-255): "))
                if not (0 <= key <= 255):
                    print("Key must be between 0 and 255.")
                    continue
                encrypt_image_xor(input_image_path, output_image_path, key)
            except ValueError:
                print("Invalid key. Please enter an integer.")
        elif choice == '4':
            input_image_path = input("Enter the path to the encrypted image to decrypt: ")
            output_image_path = input("Enter the desired output path for the decrypted image (e.g., decrypted_xor.png): ")
            try:
                key = int(input("Enter the same integer key used for encryption (0-255): "))
                if not (0 <= key <= 255):
                    print("Key must be between 0 and 255.")
                    continue
                decrypt_image_xor(input_image_path, output_image_path, key)
            except ValueError:
                print("Invalid key. Please enter an integer.")
        elif choice == '5':
            print("Exiting tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()