from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
import requests

jobs = []

# Make a request to a webpage
def find_jobs(keyword):
    for start in range(0,25,25):
        print(start)
        url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keyword={keyword}&location=singapore&trk=public_jobs_jobs-search-bar_search-submit&position=3&pageNum=0&start={str(start)}'
        response = requests.get(url)


        # Parse the response text with Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title tag and print it
        lis = soup.find_all('li')
        print(len(lis))
        for li in lis:
            job_link = li.find('a')
            job_title = li.find('h3').text.strip()
            job_company = li.find('h4').text.strip()
            job_time = li.find('time').get('datetime')
            job_location = li.find('span', {'class': 'job-search-card__location'}).text.strip()

            if job_link:
                job = {
                    "job_link":job_link.get('href'),
                    "job_title":job_title,
                    "job_company":job_company,
                    "job_location":job_location,
                    "job_time":job_time,
                }
                jobs.append(job)

def get_details(url):
    response = requests.get(url)

    try:
        soup = BeautifulSoup(response.text,'html.parser')
        r = {}

        res = soup.find_all('section',{'class':"show-more-less-html"})
        # print('res len: ', len(res))

        if len(res) == 0:
            print(soup)
            return Exception()

        description = res[0].get_text(separator=' ',strip=True)
        # print(description)
        r['description'] = description

        details = soup.find_all('li',{'class':'description__job-criteria-item'})

        # print('details len: ', len(details))
        for detail in details:
            key = detail.find('h3').get_text(separator=' ',strip=True).lower().replace(" ",'_')
            value = detail.find('span').get_text(separator=' ',strip=True)
            r[key] = value

        return r

    except Exception as e:
        print("Error getting details ",url)
        print(e)
        return e

if __name__ == "__main__":
    keyword = 'software engineer'
    find_jobs(keyword=keyword)
    for job in jobs:
        retry = 5
        details = get_details(job['job_link'])
        while type(details) == Exception and retry > 0:
                details = get_details(job['job_link'])
                sleep(0.5)
                retry -= 1

        if type(details) != Exception:
            job.update(details)
        
    
    pprint(jobs)