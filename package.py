name = 'fmt'

version = '8.0.1'

authors = [
    'FMT',
]

description = '''C++ formating'''

with scope('config') as c:
    # Determine location to release: internal (int) vs external (ext)
    # NOTE: Modify this variable to reflect the current package situation
    release_as = 'ext'

    # The 'c' variable here is actually rezconfig.py
    # 'release_packages_path' is a variable defined inside rezconfig.py

    import os
    if release_as == 'int':
        c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_INT']
    elif release_as == 'ext':
        c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
]

private_build_requires = [
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

# Pass cmake arguments (with debug symbols):
# rez-build -i -- -DCMAKE_POSITION_INDEPENDENT_CODE=1
# rez-release -- -DCMAKE_POSITION_INDEPENDENT_CODE=1


def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.REZ_FMT_ROOT = '{root}'


uuid = 'repository.fmt'
