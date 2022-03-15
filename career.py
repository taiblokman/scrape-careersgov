from requests_html import HTMLSession
import pandas as pd

all_jobs = []

def output():
    df = pd.DataFrame(all_jobs)
    df.to_csv('alljobs_final_v3.csv', index=False)
    # df.to_json('alljobs_final_v3.json')
    print('saved to file')

url= 'https://www.careers.hrp.gov.sg/sap/bc/ui5_ui5/sap/ZGERCFA004/index.html'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
s = HTMLSession()
r = s.get(url, headers=headers)

r.html.render(sleep=1, keep_page=True, scrolldown=1000, timeout=20)

# jobs = r.html.find('#__link1-__clone0')
jobs = r.html.xpath("//div[@class='sapMFlexBox sapMVBox sapMFlexBoxJustifyStart sapMFlexBoxAlignItemsStretch sapMFlexBoxWrapNoWrap sapMFlexBoxAlignContentStretch sapMFlexBoxBGTransparent sapUiSmallMarginTop sapMFlexItem']")
# print(jobs)

# //div[@class='sapMFlexBox sapMVBox sapMFlexBoxJustifyStart sapMFlexBoxAlignItemsStretch sapMFlexBoxWrapNoWrap sapMFlexBoxAlignContentStretch sapMFlexBoxBGTransparent sapUiSmallMarginTop sapMFlexItem']/div/div[2]

for item in jobs:
    # print("working...")
    title = item.xpath(".//div[1]/a", first = True).full_text
    # org = item.xpath(".//div[2]/span/text()")[:1]
    org = item.xpath(".//div[2]/span", first = True).full_text
    level = item.xpath(".//div[3]/div[2]/span", first = True).full_text
    term = item.xpath(".//div/div[4]/span", first = True).full_text
    closing_date = item.xpath(".//div/div[6]/span", first = True).full_text
    posted_date = item.xpath(".//div/div[7]/span", first = True).full_text
    job = {
        'title': title,
        'org': org,
        'level': level,
        'term': term,
        'closing_date': closing_date,
        'posted_date': posted_date,
    }
    # print(job)
    all_jobs.append(job)
    
print ("Number of jobs = ", len(all_jobs))
output()

