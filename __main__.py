import collection
import analyze
import visualization

if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since': '2018-05-01', 'until': '2018-05-31'},
        {'pagename': 'chosun', 'since': '2018-05-01', 'until': '2018-05-31'}
    ]

    # collection
    for item in items:
        resultfile = collection.crawling(**item)
        item['resultfile'] = resultfile

    # analyze
    for item in items:
        print(item['resultfile'])


    # visualization