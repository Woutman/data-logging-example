# Data logging example
This repository shows an example of logging and analysing relevant data of chatbot conversations.

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
At the bottom of simulation.py, set the user_count and num_simulations variables. Then run ```python simulation.py``` to run the simulations.
A dataset based on 100 simulations is included in the repository.

### Data Analysis
Run ```python data_analysis.py```to generate plots for Total Cost per User, Average Cost per User, Average Number of Messages per User, Average Cost per Success and Failure, and Ratio of Successes to Failures per User.
