from setuptools import setup, find_packages

setup(
    name='reddit-reposter',
    version='2.2.4',
    url='https://github.com/avg333/reddit-reposter',
    author='Adrian Villar Gesto',
    author_email='adrian.villar.gesto@gmail.com',
    description='Upload to the Twitter platform a post of the chosen subreddit',
    packages=find_packages(),
    install_requires=[
        'certifi==2024.2.2',
        'charset-normalizer==3.3.2',
        'dnspython==2.6.1',
        'idna==3.7',
        'oauthlib==3.2.2',
        'pillow==10.2.0',
        'praw==7.7.1',
        'prawcore==2.4.0',
        'pymongo==4.6.2',
        'requests==2.31.0',
        'requests-oauthlib==1.4.0',
        'setuptools==69.2.0',
        'tweepy==4.14.0',
        'update-checker==0.18.0',
        'urllib3==2.2.1',
        'websocket-client==1.7.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
)
