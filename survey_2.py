from requests_html import HTMLSession
import os
from os.path import join
import webbrowser
from pptx import Presentation
import json as js
from tqdm import tqdm
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/71.0.3578.98 Safari/537.36'
}
url_prefix = ['https://dblp.org/search?q=', '%20year%3A', '%3A']
url_next_prefix = [
    'https://dblp.org/search/publ/inc?q=',
    '%20year%3A',
    '%3A',
    '&s=ydvspc&h=30&b=',
]

id_xpath = '//@id'
base_xpath = ['//*[@id="', '"]']
title_xpath = [
    '/cite/br/span[@class="title"]',
    '/cite/span[@class="title"]',
    '/link/cite/span[@class="title"]',
    '/link/cite/br/span[@class="title"]',
]
paper_url_xpath = [
    '/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/a/@href',
    '/link/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/a/@href',
]
# bibtex_url_xpath = [
#     '/nav/ul/li[2]/div[@class="body"]/ul/li[1]/a/@href',
#     '/link/nav/ul/li[2]/div[@class="body"]/ul/li[1]/a/@href',
# ]
# bibtex_xpath = '//*[@id="bibtex-section"]/pre'
bibtex_xpath = '/html/body/div[@id="main"]/div[@id="bibtex-section"]/pre'
bibtex_url_prefix = ['https://dblp.uni-trier.de/rec/', '.html?view=bibtex']

session = HTMLSession()


def content_parse(url, headers, survey, exist_titles, res=None):
    while True:
        try:
            r = session.get(url, headers=headers)
        except:
            continue
        break
    # # Get Paper IDs
    # raw_ids, ids = get_ids(r, survey)
    print(r.html.xpath('/*'))
    print(r.html.xpath('/html/*'))
    print(r.html.xpath('/html/body/*'))
    print(r.html.xpath('/html/body/result/*'))
    print(int(r.html.xpath('/html/body/result/hits')[0].xpath('//@total')[0]))
    # print(r.html.xpath('/html/body/result/hits/*'))
    hit = r.html.xpath('/html/body/result/hits/*')[0]
    print(hit.xpath('/*'))
    print(hit.xpath('/html/*'))
    print(hit.xpath('/html/hit/*'))
    print(hit.xpath('/html/hit/info/*'))
    # title
    print(hit.xpath('/html/hit/info/title')[0].text)
    # year
    print(hit.xpath('/html/hit/info/year')[0].text)
    # type
    print(hit.xpath('/html/hit/info/type')[0].text)
    # key
    print(hit.xpath('/html/hit/info/key')[0].text)
    # ee
    print(hit.xpath('/html/hit/info/ee')[0].text)

    # # Get Paper Title / URL / Bibtex
    # with tqdm(total=len(ids)) as pbar:
    #     for id in ids:
    #         base = f'{base_xpath[0]}{id}{base_xpath[1]}'
    #         # # # Get Paper Title
    #         title = get_title(r, base)
    #         if title in exist_titles or (res(title) if res else False):
    #             # print(title)
    #             del survey[id]
    #             pbar.update(1)
    #             continue
    #         # # # Get Paper URL
    #         paper_url = get_url(r, base)
    #         # # # Get Paper Bibtex
    #         bibtex = get_bibtex(id)

    #         survey[id]['title'] = title
    #         exist_titles.append(title)
    #         survey[id]['paper_url'] = paper_url
    #         survey[id]['bibtex'] = bibtex
    #         pbar.update(1)
    r.close()
    # return raw_ids, exist_titles


if __name__ == '__main__':
    query = 'multimodal document'
    url = 'https://dblp.org/search/publ/api?q=transformer&h=100&f=0'
    survey = {}
    exist_titles = []
    content_parse(url, headers, survey, exist_titles, res=None)
