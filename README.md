# Data logging example
This repository shows an example of logging relevant data of a chatbot conversation.

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/woutman/data-logging-example.git
   cd data-logging-example
   ```

2. **Create a Virtual Environment and Activate It**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `api_key.env` file in the root directory and add the necessary environment variables:

   ```env
   OPENAI_API_KEY='your_openai_api_key'
   ```

## Usage

### Conversation Simulation
At the bottom of app.py, set the user_count and num_simulations variables. Then run ```sh python app.py``` to run the simulations.

### Data Analysis
Run ```sh python data_analysis.py```to generate plots for Total Cost per User, Average Cost per User, Average Number of Messages per User, Average Cost per Success and Failure, and Ratio of Successes to Failures per User.
