# How to Run the Script "evaluate_model.py"

To execute the script "evaluate_model.py" and evaluate your model's performance, follow the steps below:

1. **Clone the Git Repository**: Clone the repository from the following link: [NITEX_AI_Challenge](https://github.com/fabinahian/NITEX_AI_Challenge.git)  
    ```
    git clone https://github.com/fabinahian/NITEX_AI_Challenge.git
    ```

2. **Change Directory**: Navigate to the location where you cloned the Git repository.

3. **Create and Activate Virtual Environment**: Using Anaconda Prompt, create a new virtual environment named "test_env" with Python version 3.10:
    ```
    conda create --name test_env python=3.10
    conda activate test_env
    ```

4. **Install Required Packages**: Install the necessary Python packages listed in "requirements.txt" using pip:
    ```
    pip install -r requirements.txt
    ```

5. **Run the Script**: Execute the script "evaluate_model.py" by providing the path to your CSV test data as an argument:
    ```
    python evaluate_model.py path_to_your_csv_test_data
    ```

Make sure to replace "path_to_your_csv_test_data" with the actual path to your CSV test data file.

## Objective

This script is designed to perform Exploratory Data Analysis (EDA) on the Fashion MNIST dataset and identify and classify sustainable apparel products.

## Data Analysis

Here are some insights derived from the data analysis:

- The train and test data both contain 785 columns, with the first column representing labels and the rest representing input features.
- While the number of columns remains consistent, the train data consists of 60,000 rows, while the test data consists of 10,000 rows.
- Both training and testing samples consist of integer values, including the labels.
- There are no cases of labeling outside of the expected range in either the training or testing data.
- There are no missing or null values in the samples, ensuring data integrity.
- Each label has an equal distribution of 6000 training data points and 1000 testing data points, preventing data imbalance.

## Thoughts Behind the Approach

The approach involved thorough understanding and exploration of the dataset, followed by necessary visualization and analysis. Data preprocessing steps were performed to normalize and segment the training data. Different models were experimented with before selecting a Convolutional Neural Network (CNN) architecture. Evaluation included training and validation curves, confusion matrix, precision, recall, and F1 score.

## Human in the Loop

An approach to involve humans in the loop could be to incorporate user feedback on model predictions, allowing for iterative improvements based on user validation.

## Final Thoughts

The Fashion MNIST dataset serves as an excellent benchmark for model development. While the current model shows promise, there is room for enhancement through various methods and creativity. With its quality and quantity of data, the dataset lays a strong foundation for building models in the fashion industry, paving the way for improved accuracy in future iterations.

---

This README provides clear instructions for running the script and offers insights into the dataset analysis and approach taken for model development, while maintaining a professional tone throughout.
