import helper


def get_config(organization, common_args):
    api_results = {}

    config = {
        'name': organization + '/nfs-server',
        'version': "latest",
        'version-develop': 'develop',
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION']
        },
        'tests': ['-h']
    }
    return config
