import requests


def createRequest(url, header, body):
    url = url
    headers = header
    body = body

    response = requests.post(
        url,
        headers=headers,
        data=body
    )

    return response
