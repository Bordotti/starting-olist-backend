import requests
from requests import Response

source = 99988526423
destination = 9933468278
list_times_and_ids = [
    {'call_id': 70, 'started': '2016-02-29T12:00:00Z', 'ended': '2016-02-29T14:00:00Z'},
    {'call_id': 71, 'started': '2017-12-11T15:07:13Z', 'ended': '2017-12-11T15:14:56Z'},
    {'call_id': 72, 'started': '2017-12-12T22:47:56Z', 'ended': '2017-12-12T22:50:56Z'},
    {'call_id': 73, 'started': '2017-12-12T21:57:13Z', 'ended': '2017-12-12T22:10:56Z'},
    {'call_id': 74, 'started': '2017-12-12T04:57:13Z', 'ended': '2017-12-12T06:10:56Z'},
    {'call_id': 75, 'started': '2017-12-13T21:57:13Z', 'ended': '2017-12-14T22:10:56Z'},
    {'call_id': 76, 'started': '2017-12-12T15:07:58Z', 'ended': '2017-12-12T15:12:56Z'},
    {'call_id': 77, 'started': '2018-02-28T21:57:13Z', 'ended': '2018-03-01T22:10:56Z'},
]

def call(infos:dict) -> Response:
    payload = {
        'type':'start',
        'call_id': infos['call_id'],
        'timestamp': infos['started'],
        'source': source,
        'destination': destination,
        }
    create_request = requests.post('http://127.0.0.1:8000/Call-Record/', json=payload)
    print(create_request.status_code)
    #assert create_request.status_code == 201

    payload = {
        'type':'end',
        'call_id': infos['call_id'],
        'timestamp': infos['ended'],
        }
    update_request = requests.patch('http://127.0.0.1:8000/Call-Record/1/', json=payload)
    print(update_request.status_code, infos['call_id'])
    #assert update_request.status_code == 200

if __name__ == '__main__':
    for l in list_times_and_ids:
        call(l)