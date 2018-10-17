import sys

import requests
import logging


class HttpService:

    def repos_data(self, search_language):
        url = 'https://api.github.com/search/repositories?q=language:' + search_language + '&sort=stars'
        logging.info('Doing http get operation')
        response = requests.get(url)
        logging.info('Http get done, status: ' + str(response.status_code))
        response_dict = response.json()
        if response.ok:
            return response_dict
        else:
            if response_dict['errors']:
                error_msg = response_dict['errors'][0]['message']
                logging.error(error_msg)
            sys.exit()
