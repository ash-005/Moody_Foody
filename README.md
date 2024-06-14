# Moody Foody
Mood-based food recommendation system, made using Google Gemini Pro where you can tell how you are feeling and get food recommendations.

## Project Structure
```
Moody_Foody/
├── app.py
├── requirements.txt
├── venv
├── .env
├── .gitignore
└── README.md
```

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.7+
- Streamlit
- google-generativeai
- python-dotenv

### Installation Steps

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/dish-recommendation-system.git
   ```
2. Navigate to the project directory
```bash
cd dish-recommendation-system
```
3. Create a virtual environment
```bash
python -m  venv venv
```
4. Activate the virtual environment
- On Windows
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux
  ```bash
  source venv/bin/activate
  ```
5. Install the required packages to use
```bash
pip install -r requirements.txt
```

## Usage
1. Obtain API keys from the Google Gemini Pro API.
2. Create a **.env** file in the project directory and add your API keys:
```bash
GOOGLE_API_KEY=your_api_key_here
```
3. Run the Streamlit application
```bash
streamlit run app.py
```
4. Open your browser and go to http://localhost:8501/ to see the application running.


## License
Distributed under the MIT License. See LICENSE for more information.
