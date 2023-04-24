import cv2
import numpy as np


def transform_alpha_background(input_img, output_img, background=[255, 255, 255]):
    """ 
        remove alpha channel and set the background to white by default
    """
    # Read the image with the alpha channel
    image = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)

    # Check if the image has an alpha channel
    if image.shape[2] == 4:
        # Split the image into its channels
        b, g, r, a = cv2.split(image)
        # Choose a background color (default white in this example)
        background_color = background  # [R, G, B]
        # Create a background image with the same dimensions as the original image
        background = np.full((image.shape[0], image.shape[1], 3), background_color, dtype=np.uint8)
        # Normalize the alpha channel to the range [0, 1]
        a = a.astype(np.float32) / 255.0
        # Perform the alpha blending
        b = (a * b + (1 - a) * background[:, :, 0]).astype(np.uint8)
        g = (a * g + (1 - a) * background[:, :, 1]).astype(np.uint8)
        r = (a * r + (1 - a) * background[:, :, 2]).astype(np.uint8)
        # Merge the RGB channels back together
        image_rgb = cv2.merge((b, g, r)).astype(np.uint8)
    else:
        print("The image does not have an alpha channel")
    # Save the RGB image with the background color
    cv2.imwrite(output_img, image_rgb)


def remove_alpha_channel(input_img, output_img):
    """ 
        simply remove the alpha channel
    """
    # Read the image with the alpha channel
    image = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)
    # Check if the image has an alpha channel
    if image.shape[2] == 4:
        # Remove the alpha channel by slicing the image array
        image_rgb = image[:, :, :3]
    else:
        print("The image does not have an alpha channel")
    # Save the RGB image without the alpha channel
    cv2.imwrite(output_img, image_rgb)


if __name__ == "__main__":
    input_img = "./input_images/Sign_Stop.png"
    output_img = "./input_images/Sign_Stop_no_alpha.png"
    transform_alpha_background(input_img, output_img)
    # remove_alpha_channel(input_img, output_img)