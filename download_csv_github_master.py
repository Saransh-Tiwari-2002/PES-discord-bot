from github import Github
import pandas
import os

def get_json_from_github():
    try: os.remove(f'player_file.csv')
    except: pass
    g = Github('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')
    repository=g.get_user().get_repo('efootball_player_files')
    for x in ['1a', '1b', '1c', '1d','2a', '2b', '2c', '2d','3a', '3b', '3c', '3d','4a', '4b', '4c', '4d','5a', '5b', '5c', '5d','6a', '6b', '6c', '6d','7a', '7b', '7c','7d','8a', '8b']:
        data_csv = pandas.read_csv((repository.get_contents(f'{x}.csv').download_url))    
        data_csv.to_csv('player_file.csv', mode='a', header=False, index=False)
