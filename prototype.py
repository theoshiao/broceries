import re
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
#export GOOGLE_APPLICATION_CREDENTIALS="./groceries-837fe89ce8dc.json"

def itemPriceMapping(path):
    
    client = vision.ImageAnnotatorClient()
    script_dir = os.path.dirname(__file__)
    rel_path = path
    abs_file_path = os.path.join(script_dir, rel_path)
    with io.open(abs_file_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    stringToParse = texts[0].description
    listOfStrings = []
    listOfItems = []
    listOfPrices = []
    for i in range(stringToParse.count('\n')):
        partitioned = stringToParse.partition('\n')
        listOfStrings.append(partitioned[0])
        stringToParse = partitioned[2]
    for string in listOfStrings:
        print(string)
        if re.search('[a-zA-Z]', string) and not re.search('[0-9]', string):
            listOfItems.append(string.lower())
        if string.startswith('$') or string.startswith('-'):
            listOfPrices.append(string.replace('$', '').replace('-', ''))
    return dict(zip(listOfItems[2:], listOfPrices))


def finalBroPriceMapping(itemBro, items):
    subtotal = 0
    total = 0
    retItems = {}
    for item in itemBro:
        if item == 'subtotal':
            subtotal = float(items[item])
            continue
        elif item == 'total':
            total = float(items[item])
            continue
        elif itemBro[item] == 'None':
            continue
        else:
            retItems[item] = [float(items[item]), 1, itemBro[item]]

    costPerBro = {}
    for item in retItems:
        if retItems[item][2] in costPerBro:
            costPerBro[retItems[item][2]] += float(retItems[item][0] * retItems[item][1])
        else:
            costPerBro[retItems[item][2]] = float(retItems[item][0] * retItems[item][1])
    for bro in costPerBro:
        costPerBro[bro] = (costPerBro[bro] / subtotal) * total
    return costPerBro;