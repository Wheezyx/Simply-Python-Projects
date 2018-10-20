import logging

import pygal
from pygal.style import LightenStyle as LS

import config
from http_service import HttpService

logging.getLogger().setLevel(logging.INFO)


class GithubRepos:

    def organize_data(self):
        search_language = input('\nWhich language do i have to check?\n')
        response_dict = HttpService().repos_data(search_language)
        repo_dicts = response_dict['items']

        names, stars = [], []

        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])
            stars.append(repo_dict['stargazers_count'])
        logging.info('Data organized')
        self.create_chart(search_language, names, stars)

    def create_chart(self, search_language, names, stars):
        theme_version = input('\nDark or White theme? (type D/W)\n')

        logging.info('Creating chart...')
        my_style = LS('#333366', base_style=config.get_chart_style(theme_version))

        chart_config = config.get_pygal_config()
        chart = pygal.Bar(chart_config, style=my_style)
        chart.title = 'Most-Starred ' + search_language.capitalize() + ' Projects on GitHub'
        chart.x_labels = names

        chart.add('', stars)
        chart.render_to_file(search_language + '_' + theme_version + '_repos.svg')


GithubRepos().organize_data()
