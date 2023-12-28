
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([URL_TO_YOUR_APP](https://strum-buddy-n5sjbnsddt7kk8vbejctvo.streamlit.app/))


# Welcome to Strum Buddy 👋

**Strum Buddy is a Streamlit community project that leverages the OpenAI Assistants API to create a conversational experience focused on discovering and displaying instructional materials to be used to learn to play popular songs on the guitar.**

If you are unfamiliar with Streamlit please refer to the information below before getting started with the Strum Buddy source code.

## Resources

- Streamlit [docs](https://docs.streamlit.io), [community forum](https://discuss.streamlit.io) and [blog](https://blog.streamlit.io).

Streamlit lets you turn data scripts into shareable web apps in minutes, not weeks. It’s all Python, open-source, and free! And once you’ve created an app you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app.

## Installation

Open a terminal and run:

```bash
$ pip install streamlit
$ pip install openai
```
## Quickstart

### Run the app locally

To run the app locally, execute the following command:
```
$ streamlit run strum_buddy.py
```
## Configuration

To better understand the configuration options available for Streamlit apps please refer to the following docs: [Configuration](https://docs.streamlit.io/library/advanced-features/configuration)

## Secrets

Since Strum Buddy makes use of the [OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview) it is required that both the API key and Assistant ID to be used with the app be stored in an appropriate secrets file.  This file should never be checked into this repo and has been added to the .gitignore file to prevent this from occurring.  The secrets file should be added locally at the following location:

```
strum-buddy/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml # Make sure to gitignore this!
├── strum_buddy.py
└── requirements.txt
```
The secrets file should contain at least the following two valid entries.  These values should be sourced directly from your OpenAI account:
```
OPENAI_API_KEY = "your api key here"
OPENAI_ASSISTANT_ID = "your assistant id here"
```
The maintainers of this project have configured the deployed version of the application to make use of an API Key and Assistants ID associated with their own OpenAI account.

## Deploying 

Any updates introduced to the Main branch of this repo will be instantaneously reflected in the running version of the deployed Streamlit Community app!

This is both a feature and a risk so please only introduce changes to the Main branch that have been tested and verified locally first.  There are currently no other procedures or policies in place to restrict abuse and misuse of this setup.  It's entirely up to the contributors of the project to keep the example app up and running in Production.
