import cv2 as cv

def Img_Conv(img_source: str):
    """
    This will produce a binary image and then save said image

    img_source: our image file's path
    """

    # Supervior: you may want to compare images with those produced from Fiji as they may produce results that can be compared
    

    # read the image file
    img = cv.imread(img_source, 2)

    #unsure why the error is present as code works as expected may ignore if not issues arise
    ret, bw_img = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) #cv.THRESH_BINARY or  to make it binary



    cv.imshow("Binary", bw_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    #name = str(input("provide a name for the image"))
    #save_img(bw_img) # Save the image

def save_img(img):
    """
    This code will take in the "img" as the path for the image of interest and then after this it will save the image.
    During this if any issues come up it should tell the user this, returning 1 if it has worked as expected and 0 otherwise

    img: takes in the path for the image of interest and then saves it to either the Raw folder or the Converted folder depending of user inputs.
    """
    
    choice = str(input('Do you want it to be saved in the "Raw" or the "Converted" folders?'))

    if choice != "RAW" or choice != "Converted":
        print("This is not the expected format, please try to type the names 'Raw' or 'Converted' exactly. Case sensitive!")
        return 0
    
    path = fr"Data\\{choice}\\"
    cv.imwrite(fr"{path + img[5:]}", img) # Save the image
    return 1