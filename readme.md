<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100" alt="readme-logo" />
</p>
<p align="center">
    <h1 align="center">REDDIT-REPOSTER</h1>
</p>
<p align="center">
    <em>Repost Reddit to X (aka Twitter): Automate viral content sharing</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/avg333/reddit-reposter?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/avg333/reddit-reposter?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/avg333/reddit-reposter?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/avg333/reddit-reposter?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
</p>
<hr>

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [🚀 Getting Started](#-getting-started)
> - [🏀 Running reddit-reposter](#-running-reddit-reposter)
> - [🧪 Tests](#-tests)
> - [🤖 Automate with GitHub Actions](#-automate-with-github-actions)
> - [🤝 Contributing](#-contributing)
> - [📄 License](#-license)

---

## 📍 Overview

The reddit-reposter project is a production-ready codebase that specializes in reposting posts from Reddit to the
X platform. Its core functionality revolves around fetching posts from a chosen subreddit, filtering them based on
various criteria, and reposting them on X. The project provides easy configuration through command-line arguments,
allowing users to specify the subreddit to repost from and set limits for different types of posts (hot, top,
controversial, new). With robust exception handling, media file management, and save history functionalities,
reddit-reposter offers a valuable solution for automating the reposting process and amplifying content on both Reddit
and X.

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.13`
* **MongoDB**: `version 8.0`

The MongoDB database can be hosted locally or on a [cloud platform](https://www.mongodb.com/atlas/database).

You will also need to obtain [Reddit](https://www.reddit.com/wiki/api/)
and [X](https://docs.x.com/x-api/getting-started/getting-access) API
keys to obtain the necessary credentials for the environment.

### ⚙️ Installation

1. Clone the reddit-reposter repository:

```sh
git clone https://github.com/avg333/reddit-reposter
```

2. Change to the project directory:

```sh
cd reddit-reposter
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Set up the environment variables:

```sh
export DB_URL=<mongodb-url>
export REDDIT_CLIENT_ID=<reddit-client-id>
export REDDIT_CLIENT_SECRET=<reddit-client-secret>
export REDDIT_USER_AGENT=<reddit-user-agent>
export TWITTER_API_KEY=<X-api-key>
export TWITTER_API_KEY_SECRET=<X-api-key-secret>
export TWITTER_ACCESS_TOKEN=<X-access-token>
export TWITTER_ACCESS_TOKEN_SECRET=<X-access-token-secret>
```

You can choose the database, collection and key field with the following environment variables:

```sh
export DB_NAME=<database-name> # default is 'reddit_reposter'
export DB_TABLE_NAME=<collection-name> # default is 'uploaded_posts'
export ENV_DB_KEY_FIELD_KEY=<key-field> # default is 'id'
```

### 🏀 Running `reddit-reposter`

Use the following command to run reddit-reposter:

```sh
python main.py --subreddit <subreddit>
```

The `--subreddit` argument is required and specifies the subreddit to repost from. You can also use the following
optional arguments:

```sh
--hot <number> # Number of hot posts to repost. Default is 10.
--top <number> # Number of top posts to repost. Default is 10.
--controversial <number> # Number of controversial posts to repost. Default is 10.
--new <number> # Number of new posts to repost. Default is 10.
```

### 🧪 Tests

Use the following command to run tests:

```sh
pytest
```

### 🤖 Automate with GitHub Actions

This project uses [GitHub Actions](https://github.com/features/actions) to automate the execution of the Reddit Repost
Bot. The bot is scheduled to run every hour, reposting content from a specified subreddit to X.

The workflow involves several steps:

1. **Checkout Repository**: The latest code is fetched from the repository.
2. **Setup Python Environment**: A Python environment is set up with the specified version.
3. **Install Python Dependencies**: The necessary Python dependencies are installed from the `requirements.txt` file.
4. **Execute Repost Bot**: The bot is executed with the necessary environment variables.

The environment variables are securely stored in GitHub Secrets and include database connection details, Reddit and
X API keys, and the subreddit to repost from.

This automation ensures that the bot runs regularly without manual intervention, making it easy to maintain and operate.

The default setting is a one-hour period for the bot's execution, but this can be modified in
the `.github/workflows/reddit-reposter.yml` file. The period is set using a [cron expression](https://crontab.guru/).

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/avg333/reddit-reposter/blob/main/CONTRIBUTING.md)**: Review open PRs, and
  submit your own PRs.
- **[Join the Discussions](https://github.com/avg333/reddit-reposter/discussions)**: Share your insights, provide
  feedback, or ask questions.
- **[Report Issues](https://github.com/avg333/reddit-reposter/issues)**: Submit bugs found or log feature requests for
  the project.

---

## 📄 License

This project is protected under the [GNU GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html).

---

[**Return**](#-quick-links)

---
