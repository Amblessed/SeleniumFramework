import xml.etree.ElementTree as ET


class ReadXML:

    @staticmethod
    def readXMLFile(path):
        tree = ET.parse(path)
        root = tree.getroot()
        login_data_list = []
        for child in root:
            login_data_list.append(child.attrib)
        return login_data_list


# path = "..//TestData/TestData.xml"
# login_data = ReadXML.readXMLFile(path)
# for credentials in login_data:
#     username = credentials.get("username")
#     password = credentials.get("password")
#     output = credentials.get("output")
#     print(username, password, output)