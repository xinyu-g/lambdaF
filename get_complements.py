import boto3
import secrets
import requests
import random


chars = '0123456789ABCDEF'

def get(event, context):
    hex = ''.join(random.sample(chars,6))
    url = 'https://www.thecolorapi.com/scheme'
    params = {
        'hex': hex,
        'mode': 'complement',
        'count': '5',
        'format': 'json'
    }
    result = {
        'hex': hex
    }

    response = requests.get(url, params=params)
    # print(response.url)
    res = response.json()
    # print(res)
    colors = res['colors']
    complements = {}
    for color in colors:
        hex_k = color["hex"]["clean"]
        name = color["name"]["value"]
        if not complements.get(hex_k):
            complements[hex_k] = name
    # print(complements)
    complements = sorted(complements.items())
    # print(complements)
    result.update({
        'complements': complements
    })
    return result

    
# get()