import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from email2country import email2country
import qrcode
import qrcode.image.svg

font_filepath = "coolvetica rg it.otf"

fontSizeName = 50
fontSizeDerpartment = 15
fontSizeJob = 15

fontName = ImageFont.truetype(font_filepath, fontSizeName)
fontDepartment = ImageFont.truetype(font_filepath, fontSizeDerpartment)
fontJob = ImageFont.truetype(font_filepath, fontSizeJob)


# Read the Excel file in download folder
df = pd.read_excel('Registration HOGENT International Week 8-10 March 2023 (1-118) (1).xlsx')

#Get data to put on lenyard
nuttigeData = df[["First name", "Surname","Faculty or department you work in" , "Job title", "Email address"]]

print(nuttigeData.head(5))



for index, row in nuttigeData.iterrows():
    # Create image  
    img = Image.new('RGB', (550, 600), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Write text  
    #First and last name on lenyard

    _, _, w, h = d.textbbox((0, 0), row["First name"], font=fontName)
    d.text(((550-w)/2, 30), row["First name"], font=fontName, fill="black")

    _, _, w, h = d.textbbox((0, 0),row["Surname"], font=fontName)
    d.text(((550-w)/2, 100), row["Surname"], font=fontName, fill="black")

    _, _, w, h = d.textbbox((0, 0), row["Faculty or department you work in"], font=fontDepartment)
    d.text(((550-w)/2, 170), row["Faculty or department you work in"], fill=(0,0,0), font=fontDepartment)

    _, _, w, h = d.textbbox((0, 0), row["Job title"], font=fontJob)
    d.text(((550-w)/2, 210), row["Job title"], fill=(0,0,0), font=fontJob)

    # Create QR code that links to the website 'http://127.0.0.1:5500/LanyardmakerWeb/?id=1' where 1 is the index
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    qr.add_data("http://127.0.0.1:5500/LanyardmakerWeb/?id=" + str(index+1))
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white")
    img.paste(img_qr, (130, 300))
    #img = img.rotate(90, expand=True)


    # Save image
    img.save("lanyard/" + row["First name"] + row["Surname"] + ".png")


