from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER,TA_RIGHT,TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A5,A4
from gatepass.generate_gatepass import MCLine
from .models import Stocks
import os
import json

def print_stock(stockID):
    stock = Stocks.objects.filter(lot=stockID)
    stock = str(stock[0]).split('*')
    ##############################################################################
    #Get Company Values
    ##############################################################################
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(BASE_DIR, 'vault.json')) as secrets_file:
        secrets = json.load(secrets_file)
    #var
    company = secrets["company"]
    address = secrets["address"]
    company_GSTIN = secrets["company_GSTIN"]
    company_contact = "8445355567"
    Heading = "STOCK MEMO"
    lotID = stock[0]
    d = str(stock[1]).split("-")
    Date = d[2]+"/"+d[1]+"/"+d[0]
    PartyName = stock[3]
    gstin = stock[5]
    FormNo = "dadsarrefcdsfwefwcdewwfcvwfew"
    commodity = stock[-4]
    bags = stock[-3]
    box = stock[-2]
    #############################################################
    #file_name = "../STOCK_Print/" + "LOT_" + stock[0] + ".pdf"
    file_name = "STOCK_PRINT/LOT_" + stock[0] + ".pdf"

    if os.path.exists(file_name):
        os.remove(file_name)
    doc = SimpleDocTemplate(file_name, pagesize=A4,
                        rightMargin=72, leftMargin=72,
                        topMargin=40, bottomMargin=18)
    Story,story2 = [],[]
    #Styles/Allignments for the page
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))

    #Heading Details
    challanHeading = '<font size=9>%s</font>' % Heading
    challanHeading2 = '<font size=9>Ph: %s</font>' % company_contact
    corp = '<font size=15>%s</font>' % company
    corp_add = '<font size=10>%s</font>' % address
    corp_gstin = '<font size=10>%s</font>' % company_GSTIN

    #Info for the page
    txt_lot = '<font size=9>Lot: %s</font>' % lotID
    txt_time = '<font size=9>Date: %s</font>' % Date
    txt_name = '<font size=9>Name: %s</font>' % PartyName
    txt_form = '<font size=9>FORM38 | BillNo.: %s</font>' % FormNo
    txt_gstin = '<font size=9>GSTIN: %s</font>' % gstin
    
    Story.append(Paragraph(challanHeading, styles["Center"]))
    Story.append(Paragraph(challanHeading2, styles["Right"]))
    Story.append(Spacer(1, 4))
    Story.append(Paragraph(corp, styles["Center"]))
    Story.append(Spacer(1, 4))
    Story.append(Paragraph(corp_add, styles["Center"]))
    Story.append(Paragraph(corp_gstin, styles["Center"]))
    Story.append(Spacer(1, 4))

    tbl_data = [
        [Paragraph(txt_lot, styles["Justify"]), Paragraph(txt_time, styles["Right"])],
        [Paragraph(txt_name, styles["Justify"])],
        [Paragraph(txt_gstin, styles["Justify"]),Paragraph(txt_form, styles["Right"])], 
    ]

    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 12))

    line = MCLine(450)
    Story.append(line)
    Story.append(Spacer(1, 6))


    tbl_data = [
        [Paragraph("S.No.", styles["Center"]),Paragraph("Item", styles["Center"]), Paragraph("Begs", styles["Center"]),
         Paragraph("Boxes", styles["Center"])],
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 6))
    Story.append(line)
    Story.append(Spacer(1, 10))
    tbl_data = [
        [Paragraph("1.", styles["Center"]),Paragraph(commodity, styles["Center"]), Paragraph(bags, styles["Center"]),
         Paragraph(box, styles["Center"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 20))

    Story.append(line)
    Story.append(Spacer(1, 6))
    tbl_data = [
        [Paragraph("Total", styles["Center"]),Paragraph("", styles["Center"]),Paragraph(bags, styles["Center"]),
        Paragraph(box, styles["Center"])]
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 6))

    Story.append(line)
    Story.append(Spacer(1, 30))
    Story.append(Paragraph("Authorized Signature", styles["Right"]))

    #Adding Multi Build OPtion
    story2 = Story.copy()
    story2.append(Spacer(1, 50))
    story2.append(line)
    story2.append(Spacer(1, 50))
    story2.extend(Story)
    doc.build(story2)
    return(file_name)

