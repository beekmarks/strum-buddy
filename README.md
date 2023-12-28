
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

To learn more about how secrets are managed within a Streamlit application please see the following docs: [Secrets management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management).

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

## Debugging

To provide a better developer experience the Strum Buddy app currently dumps the state information for the running app into a sidebar component that can be open/closed when running the app locally.  This sidebar is hidden when the app is deployed to the Main branch.

To reveal this sidebar simply comment out the following CSS related code block:

```
#CSS to hide developer options when deployed
#Comment out when developing locally to reveal debugging tools
st.markdown(
    """
    <style>
    header {display: none !important}
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    [data-testid="collapsedControl"] {
        display: none
    }
    .st-emotion-cache-z5fcl4 {padding-top: 0 !important}
    .viewerBadge_text__1JaDK {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

```

## Contributing

Feel free to clone and fork this repo as you see fit.  If you would like to propose updates or changes to the codebase please reach out to the maintainers of the project first so they are aware of your intentions and can work with you to ensure the continued functionality of the app.

Contact Email: <stephen.mccall@gmail.com>
