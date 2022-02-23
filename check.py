def check_title(r, base):
    print(r.html.xpath(f'{base}/cite/*'))
    print(r.html.xpath(f'{base}/cite/br/*'))
    print(r.html.xpath(f'{base}/link/*'))
    print(r.html.xpath(f'{base}/link/cite/*'))
    print(r.html.xpath(f'{base}/link/cite/br/*'))


def check_paper_url(r, base):
    print(r.html.xpath(f'{base}/link/*'))
    print(r.html.xpath(f'{base}/link/nav/*'))
    print(r.html.xpath(f'{base}/link/nav/ul/*'))
    print(r.html.xpath(f'{base}/link/nav/ul/li[1]/*'))
    print(r.html.xpath(f'{base}/link/nav/ul/li[1]/div[@class="body"]/*'))
    print(r.html.xpath(f'{base}/link/nav/ul/li[1]/div[@class="body"]/ul/*'))
    print(
        r.html.xpath(
            f'{base}/link/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/*'
        )
    )
    print(
        r.html.xpath(
            f'{base}/link/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/a/*'
        )
    )
    print(r.html.xpath(f'{base}/*'))
    print(r.html.xpath(f'{base}/nav/*'))
    print(r.html.xpath(f'{base}/nav/ul/*'))
    print(r.html.xpath(f'{base}/nav/ul/li[1]/*'))
    print(r.html.xpath(f'{base}/nav/ul/li[1]/div[@class="body"]/*'))
    print(r.html.xpath(f'{base}/nav/ul/li[1]/div[@class="body"]/ul/*'))
    print(r.html.xpath(f'{base}/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/*'))
    print(
        r.html.xpath(f'{base}/nav/ul/li[1]/div[@class="body"]/ul/li[@class="ee"]/a/*')
    )


def check_bibtex(r):
    print(r.html.xpath('/html/*'))
    print(r.html.xpath('/html/body/*'))
    print(r.html.xpath('/html/body/div[@id="main"]/*'))
    print(r.html.xpath('/html/body/div[@id="main"]/div[@id="bibtex-section"]/*'))
