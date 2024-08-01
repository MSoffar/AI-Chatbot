# AI Chatbot for Maids.cc

![Logo](logo.png)

This project is an AI-powered chatbot designed for **Maids.cc**, a service helping clients to issue visas for their maids. The chatbot, named Sally, interacts with users to provide information and assistance related to maid visa services.

## Live Demo

You can access the live chatbot application here: [AI Chatbot for Maids.cc](https://chatbot-ai-maids.streamlit.app/)

## Features

- **Interactive Chatbot**: Engage with Sally, a friendly and welcoming chat agent.
- **Visa Assistance**: Get help with maid visa inquiries and learn how to apply.
- **Information Retrieval**: Sally can provide information about visa requirements, pricing, and more.
- **Secure Interaction**: The app uses OpenAI's API securely, with the API key managed through Streamlit secrets.

## Installation

To run this project locally, you'll need to have Python and pip installed. Follow the steps below:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/MSoffar/AI-Chatbot.git
    cd AI-Chatbot
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up OpenAI API Key**:
    - Create a `secrets.toml` file in the root directory of your project.
    - Add your OpenAI API key:
      ```toml
      OPENAI_API_KEY = "your-openai-api-key"
      ```

4. **Run the App**:
    ```bash
    streamlit run app.py
    ```

## Deployment

This application is deployed using Streamlit Community Cloud. To deploy your own version:

1. Push your code to a GitHub repository.
2. Log in to Streamlit Community Cloud and select your repository.
3. Configure secrets by adding your OpenAI API key in the Streamlit Secrets section.

## Project Structure

- `app.py`: Main Streamlit application file.
- `requirements.txt`: List of Python packages required for the project.
- `logo.png`: Logo image displayed in the app.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For inquiries or support, please visit [Maids.cc Support](https://maids.cc/support).

---

Enjoy interacting with Sally, your virtual assistant for all maid visa-related inquiries!
