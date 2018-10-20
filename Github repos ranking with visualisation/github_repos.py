import pygal
import requests
from pygal.style import DarkGreenBlueStyle as DGBS, LightenStyle as LS
from http_service import HttpService


class GithubRepos:

    def organize_data(self):
        search_language = input('Which language do i have to check?\n')
        response_dict = HttpService().repos_data(search_language)
        repo_dicts = response_dict['items']

        names, stars = [], []

        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])
            stars.append(repo_dict['stargazers_count'])

        my_style = LS('#333366', base_style=DGBS)

        chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
        chart.title = 'Most-Starred ' + search_language + ' Projects on GitHub'
        chart.x_labels = names

        chart.add('', stars)
        chart.render_to_file(search_language + '_repos.svg')


GithubRepos().organize_data()
