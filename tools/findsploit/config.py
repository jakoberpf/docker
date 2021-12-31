import helper

def get_config(organization, common_args):
    api_results = {
        'FINDSPLOIT_GITHUB_INFO':  helper.get_latest_github_release_no_browser_download('1N3/Findsploit'),
    }

    config = {
        'name': organization+'/findsploit',
        'version': api_results['FINDSPLOIT_GITHUB_INFO']['version'][1:], # Remove the leading 'v'
        'buildargs': {
            'LAST_UBUNTU_VERSION': common_args['LAST_UBUNTU_VERSION'],
            'FINDSPLOIT_DOWNLOAD_URL': api_results['FINDSPLOIT_GITHUB_INFO']['url']
        }
    }
    return config