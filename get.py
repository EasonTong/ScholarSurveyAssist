from check import check_title, check_bibtex, check_paper_url


def get_title(r, base):
    title_xpath = [
        '/cite/br/span[@class="title"]',
        '/cite/span[@class="title"]',
        '/link/cite/span[@class="title"]',
        '/link/cite/br/span[@class="title"]',
    ]

    titles = map(lambda xpath: r.html.xpath(f'{base}{xpath}'), title_xpath)
    for title in titles:
        if title:
            title = title[0].full_text
            break
    # if not title:
    #     check_title(r, base)
    return title


def get_url(r, base):
    paper_url_xpath = [
        '/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/a/@href',
        '/link/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/a/@href',
    ]
    paper_urls = map(lambda xpath: r.html.xpath(f'{base}{xpath}'), paper_url_xpath)
    for paper_url in paper_urls:
        if paper_url:
            paper_url = paper_url[0]
            break
    # if not paper_url:
    #     check_paper_url(r, base)
    return paper_url


def get_bibtex(id, session, headers):
    bibtex_xpath = '/html/body/div[@id="main"]/div[@id="bibtex-section"]/pre'
    bibtex_url_prefix = ['https://dblp.uni-trier.de/rec/', '.html?view=bibtex']

    bibtex_url = f'{bibtex_url_prefix[0]}{id}{bibtex_url_prefix[1]}'
    while True:
        try:
            bibtex_r = session.get(bibtex_url, headers=headers)
        except:
            continue
        break
    bibtex = bibtex_r.html.xpath(bibtex_xpath)
    if bibtex:
        bibtex = bibtex[0]
    # else:
    #     # print(bibtex_r.html.xpath('//*[@id="bibtex-section"]/*'))
    #     check_bibtex(bibtex_r)
    bibtex_r.close()
    try:
        return bibtex.full_text
    except Exception as e:
        print(repr(e))
        print(bibtex)


def get_ids(r, survey):
    id_xpath = '//@id'

    raw_ids = r.html.xpath(id_xpath)
    ids = []
    for id in raw_ids:
        id = id.split('/')
        if id[0] == 'conf':
            survey['/'.join(id)] = {'type': 'conference'}
            ids.append('/'.join(id))
        elif id[0] == 'journals':
            if id[1] == 'corr':
                survey['/'.join(id)] = {'type': 'arXiv'}
                ids.append('/'.join(id))
            else:
                survey['/'.join(id)] = {'type': 'journal'}
                ids.append('/'.join(id))
    return raw_ids, ids
