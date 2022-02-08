from goodreads import client
import goodreads_api_client as gr
import requests
import xml.etree.ElementTree as ET

goodreadsClient = client.GoodreadsClient(
    'Cmme2MO49NzvdsCm2tyQ', 'FshjZsq2tla621mS74Pm7XXACpdFlvwu1AuYdBZm0Pc')
apiKey = 'Cmme2MO49NzvdsCm2tyQ'
shelf = '%23ALL%23'
userId = '56094064'

URL = 'https://www.goodreads.com/review/list/' + userId + '.xml?key=' + \
    apiKey + '&v=2&shelf=' + shelf + '&per_page=200&page=1'


client = gr.Client(developer_key='Cmme2MO49NzvdsCm2tyQ')

response = requests.get(url=URL)

root = ET.fromstring(response.content)


for review in root.findall('./reviews'):
    book_id_list = []

    for book_id in review:
        int_id = int(book_id.find('./book/id').text)
        book_id_list.append(int_id)

print(book_id_list)
print(len(book_id_list))

book_rating_dict = {}

for book_id in book_id_list:
    book_obj = goodreadsClient.book(book_id)
    ar = float(book_obj.average_rating)
    rc = float(book_obj.ratings_count)

    book_rating_dict[book_obj.title] = ((ar * rc + 6) / (rc + 2))

for x in sorted(book_rating_dict, key=book_rating_dict.get, reverse=True):
    print(x, book_rating_dict[x])
