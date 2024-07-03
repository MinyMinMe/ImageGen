from PIL import Image, ImageDraw, ImageFont
import os
import openpyxl

class ImageGen():
    def __init__(self):
        self.image = Image.new("RGB", (500, 500), "white")
        self.width = self.image.width
        self.height = self.image.height

        # Create a new image with white background
        # Initialize the drawing context (이미지를 그리는 도구)
        self.draw = ImageDraw.Draw(self.image) 

    def code(self, word):
        #word = "MCC"
 
        current_directory = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(current_directory, "NanumGothicBold.ttf")

        # Center word font set
        font_size = 150
        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = self.getSize(word, font)
        # Calculate text position
        text_x = (self.width  - text_width) // 2
        text_y = (self.height - text_height) // 2 - 100

        self.draw.text((text_x, text_y), word, fill="black", font=font)

    def number(self, level):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(current_directory, "NanumGothicBold.ttf")
        font_size = 150
        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = self.getSize(level, font)
        # Calculate text position
        text_x = (self.width  - text_width) // 2
        text_y = (self.height - text_height) // 2 + 40

        self.draw.text((text_x, text_y), level, fill="black", font=font)

    def saveToFile(self, filename):
        # Save the image
        self.image.save(filename, format='JPEG')


    def getSize(self, text, font):
        text_left, text_top, text_right, text_bottom =  self.draw.textbbox(text=text, font=font,xy=[0,0])
        text_width, text_height = (text_right - text_left, text_bottom - text_top)
        return (text_width, text_height)


    def makeImage(self, word, number):
        self.__init__()
        # Create word directory
        self.code(word)
        self.number(number)
        # Save to file in the ".\result" directory with word+number name
        current_directory = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(current_directory, "result", f"{word}{number}.jpg")
        self.saveToFile(filename)

    def read_excel_to_lists(self, filename):
        # Load the workbook
        workbook = openpyxl.load_workbook(filename)
        
        # Select the active worksheet or a specific one
        worksheet = workbook.active  # or workbook['Sheet1'] if you know the sheet name
        
        # Initialize lists to store data
        data_lists = []
        
        # Iterate through the rows in the worksheet
        for row in worksheet.iter_rows(values_only=True):
            # Append each row's data as a list to data_lists
            data_lists.append(list(row))
        
        # Close the workbook
        workbook.close()
        
        return data_lists

if __name__ == "__main__":
    a = ImageGen()
    list = a.read_excel_to_lists("code.xlsx")
    print(list)
    for i in list:
        a.makeImage(i[0], i[1])
#    a.makeImage("MCC", "33002")