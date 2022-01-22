from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBl8DTGupdA73zdLDs9hZbbCJk2Or28P6Y"
my_cse_id = "ea9823706ac6eff0f"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


results = google_search(
    'NEINOR SUR SAU', my_api_key, my_cse_id, num=2)

for result in results:
    pprint.pprint(result)
