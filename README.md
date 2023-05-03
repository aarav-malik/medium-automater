# Medium Automater

Medium Automater is a tool that automates the process of generating articles using the OpenAI API and publishing them on Medium. 

## Installation

1. Clone the repository from GitHub:
```git clone https://github.com/aarav-malik/medium-automater.git```


2. Install the dependencies:
```python generate_article.py --prompt "Your prompt goes here"```


3. Set up your OpenAI API key:
- Sign up for an OpenAI API key [here](https://beta.openai.com/signup/).
- Copy your API key and set it as an environment variable named `OPENAI_API_KEY`.

4. Set up your Medium account:
- Sign up for a Medium account if you don't have one already.
- Create a new integration [here](https://medium.com/me/settings) by clicking on "Integration tokens" in the left sidebar.
- Copy your integration token and set it as an environment variable named `API_KEY`.
- Set your client id as the variable `CLIENT_ID`.

## Usage

1. To generate an articles, replace "Hello" in the topics array to the topic of your choice
2. Tags can be changed by adding strings to the Tags array
3. Status of article can be changed by modifying `publishStatus` -> set to "public" to publish upon running code or "draft" to send it to medium as a draft
4. Run the code


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

