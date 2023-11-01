	HOW TO RUN THE SCRIPT CALLED "evaluate_model.py"

  - Clone the Git Repository: https://github.com/fabinahian/NITEX_AI_Challenge.git 
    [Command: git clone https://github.com/fabinahian/NITEX_AI_Challenge.git]
  - Change your directory to the location where you cloned the Git repo
  - Command: conda create --name test_env python = 3.10
  - Command: conda activate test_env
  - Command: pip install -r "requirements.txt"
  - Command: python evaluate_model.py path_to_your_csv_test_data

*Run the commands on your Anaconda Prompt

	OBJECTIVE

  - EDA of Fashion MNIST
  - Identification and classification of Sustainable Apparel Products

		DATA ANALYSIS

  - In both train data & test data, there are 785 columns, out of which, the 1st column is the label & the rest are the input features
  - The number of columns is the same for both train data & test data; however, the number of rows differs. For train data, there are 60000 rows & test data has 10000 rows. So, there are 60000 training data & 10000 testing data.
  - Both training samples & testing samples consist of integer values. So, the labels are also numerical values.
  -  There is no case of labelling outside of range within the training data. That's a good thing! ✅
  -  There is no case of labelling outside of range within the testing data. That's a good thing! ✅
  -  There is no missing value or null value in the training samples or the testing samples. That's a good thing! ✅
  -  Each label has 6000 training data. So, there's no imbalance in the training data. That's a good thing! ✅
  -  Each label has 1000 testing data. So, there's no imbalance in the testing data. That's a good thing! ✅

	THOUGHTS BEHIND THE APPROACH

  - I first read the entire Document that comes with the Data Set. So, I gained an idea about what to expect from the data.
  - I then explored the data & created some necessary visualization for  better understanding.
  - I analyzed the data to understand whether or not modifications (eg. cleanup) are required.
  - I then did some data pre-processing to normalize the acquired data, which helped divide the training data into 2 segments: training data and validation data.
  - I tried 4 different models for this problem in my experimental notebook. None of them worked that great. So, I decided to work with a CNN architecture since it's a very good neural network for image classification.
  - I tested for training & validation curve, and confusion matrix when evaluating the model.
  - I also printed out the precision, recall & F1 score of the model since that's a great way of observing a model's performance. 
  
		HUMAN IN THE LOOP

A possible method of keeping humans in the loop might be to give the users the option to vote whether or not the prediction made by the machine was correct. Based on that feedback, the model can be further improved. 

	FINAL THOUGHTS

MNIST is a benchmark dataset. Therefore, it's a great place to start working on models. The model that was built for this project can be improved over time by various methods & creativity. It has the potential of being the ideal dataset for building models for the fashion industry owing to the quality & quantity of data. One can build the foundation of a new model via this before moving on to a more relevant dataset for improved accuracy.  
