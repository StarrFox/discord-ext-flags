import re

from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("discord/ext/flags/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

setup(
    name="discord-flags",
    author="XuaTheGrate",
    version=version,
    url="https://github.com/XuaTheGrate/Flag-Parsing",
    packages=['discord.ext.flags'],
    license='MIT',
    description="A Discord.py extension allowing you to pass flags as arguments.",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=["discord.py>=1.2.5"],
    extras_require=None,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
