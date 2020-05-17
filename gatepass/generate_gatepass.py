import json
import os
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER,TA_RIGHT
from reportlab.lib.pagesizes import A5
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
################################################################################################

class MCLine(Flowable):
 # ----------------------------------------------------------------------
 def __init__(self, width, height=0):
  Flowable.__init__(self)
  self.width = width
  self.height = height

 # ----------------------------------------------------------------------
 def __repr__(self):
  return "Line(w=%s)" % self.width

 # ----------------------------------------------------------------------
 def draw(self):
  """
  draw the line
  """
  self.canv.line(0, self.height, self.width, self.height)
###################################################################################################


def generate(item):
    file_name = "../Bills/" + "Bill_" + item[0]['gatepass'] + ".pdf"

    if os.path.exists(file_name):
        os.remove(file_name)


    doc = SimpleDocTemplate(file_name, pagesize=A5,
                        rightMargin=72, leftMargin=72,
                        topMargin=40, bottomMargin=18)
    Story = []
    ##############################################################################
    #Variable Initiation
    ##############################################################################
    company = "SJ ICE and COLD STORAGE PVT. LTD"
    address = "SIROLI, AGRA"
    company_GSTIN = "GSTIN:- " + "ascdfe12346546"
    BillNo = item[0]['gatepass']
    formatted_time = item[0]['date']
    Vehicle_number = item[0]['vehicleNo']
    WayBill = item[0]['eway']
    driveName = item[0]['driver_name']
    ##############################################################################
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

    ptext = '<font size=15>%s</font>' % company
    Story.append(Paragraph(ptext, styles["Center"]))
    Story.append(Spacer(1, 4))

    ptext = '<font size=10>%s</font>' % address
    Story.append(Paragraph(ptext, styles["Center"]))


    ptext = '<font size=10>%s</font>' % company_GSTIN
    Story.append(Paragraph(ptext, styles["Center"]))
    ptext = '<font size=10>Bill: %s</font>' % BillNo
    Story.append(Paragraph(ptext, styles["Center"]))
    Story.append(Spacer(1, 5))


    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))

    txt_time = '<font size=9>%s</font>' % formatted_time
    txt_number = '<font size=9>Vehicle No.: %s</font>'% Vehicle_number
    tbl_data = [
        [Paragraph(txt_time, styles["Justify"]), Paragraph(txt_number, styles["Right"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 5))

    txt_time = '<font size=9>BillNO: %s</font>' % WayBill
    txt_number = '<font size=9>Driver Name: %s</font>'% driveName
    tbl_data = [
        [Paragraph(txt_time, styles["Justify"]), Paragraph(txt_number, styles["Right"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 12))

    line = MCLine(280)
    Story.append(line)
    Story.append(Spacer(1, 12))


    tbl_data = [
        [Paragraph("Item", styles["Justify"]),Paragraph("Name", styles["Justify"]),
         Paragraph("Gstin", styles["Justify"]), Paragraph("Begs", styles["Justify"]),
         Paragraph("Boxes", styles["Justify"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 6))

    line = MCLine(280)
    Story.append(line)
    item_details = {'name': 'kism', 'party':'testing1234User', 'Tin': 'Abhsdidsew2321', 'qty': '12'}

    tbl_data = []
    for i in item:
        Item = Paragraph(i['Commodity'], styles["Justify"])
        Name = Paragraph(i['Party'], styles["Justify"])
        Gstin = Paragraph(i['GSTIN'], styles["Justify"])
        Begs = Paragraph(i['Begs'], styles["Justify"])
        Boxes = Paragraph(i['Boxes'], styles["Justify"])

                # Add this loop's step row into data array
        tbl_data.append([Item, Name, Gstin, Begs, Boxes])

    tbl = Table(tbl_data)
    Story.append(tbl)
    doc.build(Story)

