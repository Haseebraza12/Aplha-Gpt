# Alpha GPT

A conversational AI web application built with Streamlit and powered by the OpenAI GPT-3.5 Turbo language model. Alpha GPT provides an interactive chat interface that enables users to engage in natural language conversations with an AI assistant.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Team](#team)
- [License](#license)

---

## Overview

Alpha GPT is a lightweight, browser-based chatbot application that leverages the OpenAI API to generate intelligent responses to user prompts. The application is designed with a custom visual theme, a sidebar navigation panel, and a multi-turn conversation loop that allows up to five consecutive interactions per session.

---

## Features

- Natural language conversation powered by GPT-3.5 Turbo
- Custom background image styling via base64-encoded CSS
- Multi-turn conversation support (up to five turns per session)
- Real-time response spinner for improved user experience
- Sidebar navigation with an About Us section
- Bold, centered title with text shadow for visual emphasis

---

## Tech Stack

| Technology     | Purpose                              |
|----------------|--------------------------------------|
| Python         | Core programming language            |
| Streamlit      | Web application framework            |
| OpenAI API     | Language model inference             |
| Base64         | Background image encoding            |
| Webbrowser     | External HTML file navigation        |

---

## Project Structure

```
Aplha-Gpt/
|-- app.py          # Main application entry point
|-- bg3.jpg         # Background image asset
|-- README.md       # Project documentation
```

---

## Prerequisites

Before running this application, ensure the following are installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- A valid OpenAI API key

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Haseebraza12/Aplha-Gpt.git
   cd Aplha-Gpt
   ```

2. Install the required dependencies:

   ```bash
   pip install streamlit openai
   ```

---

## Configuration

1. Open `app.py` in a text editor.
2. Replace the placeholder API key with your own OpenAI API key:

   ```python
   apikey = 'your-openai-api-key-here'
   openai.api_key = apikey
   ```

3. Update the background image path to match the location of `bg3.jpg` on your local machine:

   ```python
   image_path = 'path/to/your/bg3.jpg'
   ```

> **Security Notice:** Do not commit your API key directly into source code. Consider using environment variables or a `.env` file with the `python-dotenv` library to manage sensitive credentials securely.

---

## Usage

Run the application using the Streamlit CLI:

```bash
streamlit run app.py
```

The application will open in your default web browser. Enter a prompt in the text input field and receive a generated response from the AI assistant. You can continue the conversation for up to five turns per session.

---

## Team

| Name                     | Role                        |
|--------------------------|-----------------------------|
| Haseeb Raza              | Co-founder and CEO          |
| Ibrahim Nadeem           | Head of Operations          |
| Muhammad Bilal Afzal Awan| Chief Technology Officer    |

---

## License

This project is currently unlicensed. All rights reserved by the authors. For permissions or inquiries, please contact the repository owner.
