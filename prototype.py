import re
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])
    return texts, response
        #print('bounds: {}'.format(','.join(vertices)))
texts, response = detect_text('/Users/theos/Documents/sideprojects/broceries/veggie-grocery-receipt_orig.jpg')
#texts

unwanted_words = ['safeway', 'mgr', 'manager', 'thank', 'you', 'for', 'shopping', 'with', 'us', 'regprice', 'regular', 
                 'cardsav', 'resprice', 'scanned', 'coupon', 'ecoupon']
#parses the text into dictionary of item: price mapping
def parse_lines(texts):
    stringToParse = texts[0].description
    listOfStrings = []
    listOfItems = []
    listOfPrices = []
    for i in range(stringToParse.count('\n')):
        partitioned = stringToParse.partition('\n')
        listOfStrings.append(partitioned[0])
        stringToParse = partitioned[2]
    for string in listOfStrings:
        if re.search('[a-zA-Z]', string) and not re.search('[0-9]', string):
            listOfItems.append(string.lower())
        if string.startswith('$') or string.startswith('-'):
            listOfPrices.append(string.replace('$', '').replace('-', ''))
    return dict(zip(listOfItems[2:], listOfPrices))
items = parse_lines(texts)

bros = ['Nilay', 'Theo', 'Anderson', 'Amy']
itemBro = {'zuchinni green': 'Nilay', 'banana cavendish': 'Nilay', 
           'special': 'Theo', 'potatoes brushed': 'Anderson', 
           'broccoli': 'Nilay', 'brussel sprouts': 'Anderson', 
           'grapes green': 'Amy', 'peas snow': 'Nilay', 
           'tomatoes grape': 'Anderson', 'lettuce iceberg': 'Theo', 
           'subtotal': 'None', 'loyalty': 'None', 'total': 'None', 
           'cash': 'None', 'change': 'None'}
#itemBro: item: bro mapping
#items: item: price mapping
#returns list containing dictionary of item: [price, quantity, bro], subtotal, and total
def itemsPerBro(itemBro, items):
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
    return [retItems, subtotal, total]
itemBroMapping = itemsPerBro(itemBro, items)
itemBroMapping

#people is list of bros, items is dictionary of item:[cost, quantity, bro], 
def costPerPerson(people, items, subtotal, total):
    numBros = len(people)
    costPerBro = {}
    for item in items:
        if items[item][2] in costPerBro:
            costPerBro[items[item][2]] += float(items[item][0] * items[item][1])
        else:
            costPerBro[items[item][2]] = float(items[item][0] * items[item][1])
    for bro in costPerBro:
        costPerBro[bro] = (costPerBro[bro] / subtotal) * total
        
    return costPerBro;