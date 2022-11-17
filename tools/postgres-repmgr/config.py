import helper


def get_config(organization, common_args):
    api_results = {
        # 'REPMGR_GITHUB_RELEASE_VERSION': helper.get_latest_github_release('EnterpriseDB/repmgr', 'repmgr'),
    }

    config = {
        'name': organization + '/postgres-repmgr',
        'version': '13',
        'version-develop': '13-develop',
        'buildargs': {
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
            # 'REPMGR_GITHUB_RELEASE_VERSION': api_results['REPMGR_GITHUB_RELEASE_VERSION'],
            # 'REPMGR_GITHUB_RELEASE_PACKAGE': "https://github.com/EnterpriseDB/repmgr/archive/refs/tags/v5.3.3.tar.gz"
        },
        'tests': ['-h']
    }
    return config
