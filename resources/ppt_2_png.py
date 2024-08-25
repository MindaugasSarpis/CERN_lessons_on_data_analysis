import os
import comtypes.client

def pptx_to_pdf(pptx_file):
    # Initialize the PowerPoint application
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    # Open the PowerPoint presentation
    presentation = powerpoint.Presentations.Open(pptx_file, WithWindow=False)

    pdf_file = pptx_file.replace(".pptx", ".png")
    # Save as PDF
    presentation.SaveAs(pdf_file, 18)  # 32 is the code for saving as PDF

    # Close the presentation
    presentation.Close()

    # Quit the PowerPoint application
    powerpoint.Quit()

# Specify the folder containing your PPTX files
pptx_file = r"C:\Users\User\Desktop\CERN_Lessons_on_Data_Analysis\lectures\source\resources\lecture_2\image_slides_lecture_2.pptx"
pptx_to_pdf(pptx_file)