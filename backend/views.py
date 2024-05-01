from django.shortcuts import render
from .forms import robotsForm
import requests
import validators

def render_homepage(request):

    return render(request, 'home.html', {})

def display_robots(request):

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = robotsForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            website = form.cleaned_data['website']

            # URL validation
            if not validators.url(website):
                return render(request, 'home.html', {'robots': 'Invalid URL'})

            if not website.endswith('/robots.txt'):
                website = website + '/robots.txt'

            # Use a browser agent
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
            
            # Make sure we return an OK response otherwise rise error
            try:
                response = requests.get(website, headers=headers)
            except requests.exceptions.ConnectionError as ece:
                return render(request, 'home.html', {'robots': ece})
            except requests.exceptions.Timeout as et:
                return render(request, 'home.html', {'robots': et})
            except requests.exceptions.RequestException as err:
                return render(request, 'home.html', {'robots': err})

            if response.status_code == 200:
                
                # Parse robotx.txt file into a python structured object
                # I.e:
                # result_data_set = { <user-agent>: { <rule>: [pattern_list] }}
                robots = response.text
                result_data_set = {}

                for line in robots.split('\n'):

                    if line.startswith('#') or line == '' or line.startswith('Sitemap') or line.startswith('<'):
                        continue

                    if line.startswith('User'):
                        value_user = line.split(':')[1].strip()
                        result_data_set.update({value_user:{}})
                        continue

                    rule_line = line.split(':')
                    rule = rule_line[0].strip()
                    pattern = rule_line[-1].strip()

                    if rule in result_data_set[value_user]:
                        result_data_set[value_user][rule].append(pattern)
                    else:
                        result_data_set[value_user][rule] = [pattern]
            else:
                robots = 'Could not retrieve robtos file. Reponse status code ' + str(response.status_code)
                return render(request, 'home.html', {'robots': robots})
        else:
            robots = 'Input not valid'
            return render(request, 'home.html', {'robots': robots})
    else:
        return render(request, 'home.html', {})
    
    return render(request, 'robots.html', {'result_data_set': result_data_set})