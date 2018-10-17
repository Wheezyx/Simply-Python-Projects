import requests

from http_service import HttpService


class GithubRepos:

    def organize_data(self):
        search_language = input('Which language do i have to check?\n')
        response_dict = HttpService().repos_data(search_language)
        print(response_dict.keys())


GithubRepos().organize_data()
