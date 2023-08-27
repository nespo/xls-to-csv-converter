import xml.etree.ElementTree as ET
import csv

def read_excel_xml_to_csv(input_filename, output_filename):
    tree = ET.parse(input_filename)
    root = tree.getroot()

    ns = {'ss': 'urn:schemas-microsoft-com:office:spreadsheet'}

    with open(output_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for row in root.findall('.//ss:Row', ns):
            csv_row = []
            for cell in row.findall('ss:Cell', ns):
                data = cell.find('ss:Data', ns)
                if data is not None:
                    csv_row.append(data.text)
                else:
                    csv_row.append('')
            csv_writer.writerow(csv_row)
