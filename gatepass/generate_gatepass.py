import json
import os
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER,TA_RIGHT
from reportlab.lib.pagesizes import A5,A4
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


    doc = SimpleDocTemplate(file_name, pagesize=A4,
                        rightMargin=72, leftMargin=72,
                        topMargin=40, bottomMargin=18)
    Story,story2 = [],[]
    ##############################################################################
    #Variable Initiation
    ##############################################################################
    company = "S.J. ICE AND COLD STORAGE PVT. LTD."
    address = "SIROLI, AGRA- 282001"
    company_GSTIN = "GSTIN:- " + "ascdfe12346546"
    BillNo = item[0]['gatepass']
    formatted_time = item[0]['date']
    Vehicle_number = item[0]['vehicleNo']
    WayBill = item[0]['eway']
    driveName = item[0]['driver_name']
    PartyName = item[0]['Party']
    gstin = item[0]['GSTIN']
    #line = MCLine(280) #lINE WIDTH ON GATEPASS
    line = MCLine(450) #lINE WIDTH ON GATEPASS
    ##############################################################################
    
    #Styles/Allignments for the page
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))

    #Heading Details
    challanHeading = '<font size=9>Gatepass/Delivery Challan</font>'
    challanHeading2 = '<font size=9>Ph: 8445355567</font>'
    corp = '<font size=15>%s</font>' % company
    corp_add = '<font size=10>%s</font>' % address
    corp_gstin = '<font size=10>%s</font>' % company_GSTIN

    #Info for the page
    txt_party = '<font size=9>Name: %s</font>' % PartyName
    txt_gstin = '<font size=9>GSTIN: %s</font>' % gstin
    txt_pass = '<font size=9>Pass No.: %s</font>'% BillNo
    txt_time = '<font size=9>%s</font>' % formatted_time
    txt_number = '<font size=9>Vehicle No.: %s</font>'% Vehicle_number
    txt_eway = '<font size=9>EWay Bill: %s</font>' % WayBill
    txt_driver = '<font size=9>Driver Name: %s</font>'% driveName

    
    Story.append(Paragraph(challanHeading, styles["Center"]))
    Story.append(Paragraph(challanHeading2, styles["Right"]))
    Story.append(Spacer(1, 4))
    Story.append(Paragraph(corp, styles["Center"]))
    Story.append(Spacer(1, 4))
    Story.append(Paragraph(corp_add, styles["Center"]))
    Story.append(Paragraph(corp_gstin, styles["Center"]))
    Story.append(Spacer(1, 4))

    tbl_data = [
        [Paragraph(txt_pass, styles["Justify"]), Paragraph(txt_time, styles["Right"])],
        [Paragraph(txt_party, styles["Justify"])],
        [Paragraph(txt_gstin, styles["Justify"]),Paragraph(txt_eway, styles["Right"])],
        [Paragraph(txt_driver, styles["Justify"]), Paragraph(txt_number, styles["Right"])]
    ]

    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 6))

    Story.append(line)
    Story.append(Spacer(1, 3))


    tbl_data = [
        [Paragraph("Item", styles["Justify"]), Paragraph("Begs", styles["Justify"]),
         Paragraph("Boxes", styles["Justify"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 3))
    Story.append(line)
    ttl_beg = 0
    ttl_box = 0
    tbl_data = []
    for i in item:
        Item = Paragraph(i['Commodity'], styles["Justify"])
        Begs = Paragraph(i['Begs'], styles["Justify"])
        Boxes = Paragraph(i['Boxes'], styles["Justify"])
        ttl_beg = ttl_beg + int(i['Begs'])
        ttl_box = ttl_box + int(i['Boxes'])
        tbl_data.append([Item,Begs, Boxes])
    
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 6))

    Story.append(line)
    Story.append(Spacer(1, 3))
    tbl_data = [
        [Paragraph("Total", styles["Justify"]),Paragraph(str(ttl_beg), styles["Justify"]),
        Paragraph(str(ttl_box), styles["Justify"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 3))
    Story.append(line)
    Story.append(Spacer(1, 30))
    Story.append(Paragraph("Authorized Signature", styles["Right"]))

    #Adding Multi Build OPtion
    story2 = Story.copy()
    story2.append(Spacer(1, 20))
    story2.append(line)
    story2.append(Spacer(1, 20))
    story2.extend(Story)
    doc.build(story2)

