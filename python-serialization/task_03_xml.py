#!/usr/bin/python3
#!/usr/bin/env python3
""" Script to serialize and deserialize dictionaries to and from XML files using the xml.etree.ElementTree module. """

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.
    
    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to write the XML data to.
    """
    root = ET.Element("data") 
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  
        child.text = str(value)  
    tree = ET.ElementTree(root)  
    tree.write(filename)  

def deserialize_from_xml(filename):
    """
    Deserialize a dictionary from an XML file.
    
    Parameters:
    filename (str): The name of the file to read the XML data from.
    
    Returns:
    dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)  
    root = tree.getroot()  
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text  
    return dictionary
