# Prints an Introductory statement for each domain choice of the quiz
def intro_statement(choice):

    print(f"Welcome to the {choice} Quiz !!!")
    print("You'll be given 5 multiple-choice questions, each worth 20 marks")
    print(f"Depending on your final score, your proficiency level in {choice} will be identified.")
    print("""
Evaluation Criteria -
0-40: Beginner
41-60: Intermediate
61-80: Advanced
81-100: Expert
""")
    print('For each incorrect answer, a penalty of 10 marks will be deducted from your score.')


# Main Global Score
score = 0
# Evaluate each answer and accordingly calculates the score
def evaluate(q,choice,score):

    if q.upper() == choice:
        print("Congratulations! That's the correct answer!")
        score += 20
    else:
        print("Oops! That's not the correct answer.")
        print("Correct choice is : ",choice)
        score -= 10

    return score

# Decides the category of users expertise based on the final score
def final_evaluation(score):

    print(f'Your Final Score is {score} ')
    if score <= 40:
        print("Your proficiency level: Beginner")
        print("Comment : Getting Started - Keep Learning!")
    elif score <= 60:
        print("Your proficiency level: Intermediate")
        print("Comment : Making Progress - Keep Going!")
    elif score <= 80:
        print("Your proficiency level: Advanced")
        print("Comment : Almost There - Refine Skills!")
    else:
        print("Your proficiency level: Expert")
        print("Comment : Job Ready - Well Done!")


# Program starts from here
print("*" * 32)
print("\tWELCOME TO THE QPREP !!!     ")
print("*" * 32)

while(1):
    # Taking domain input from the user and acting accordingly
    inp = int(input('''
Select a Topic for the Quiz - 
0. Exit 
1. Django
2. Machine Learning 
3. Data Analysis 

Enter your choice : '''))


    if inp == 0:

        print("Thank for Playing ! Visit Again !")
        break
    elif inp == 1 :
        print('\n')
        intro_statement('Django')


        q1 = input('''
Question: What command creates a Django superuser?
Options:
A) django createsuperuser
B) python manage.py createsuperuser
C) create superuser
D) django-admin createsuperuser        

Enter your choice : ''')

        score = evaluate(q1,'B',score)

        print('Feedback : A Django superuser has elevated access, controlling administrative tasks and accessing all parts of a project.')

        q2 = input('''
Question: What is the purpose of Django's middleware?
Options:
A) To define URL patterns
B) To manage database migrations
C) To handle user authentication
D) To process request-response cycles globally        

Enter your choice : ''')

        score = evaluate(q2,'D',score)

        print("Feedback : Django's middleware manages global request-response cycles, allowing for processing before reaching views.")

        q3 = input('''
Question: In Django, what does the @classmethod decorator do in a model?
Options:
A) Defines a class method accessible by instances
B) Enables direct SQL query execution
C) Marks a method as a static method
D) Provides access to instance attributes        

Enter your choice : ''')

        score = evaluate(q3,'A',score)

        print("Feedback : The @classmethod decorator in Django models allows the creation of methods accessible by the class itself, not just instances.")


        q4 = input('''
Question: What does Django's select_related() method do in a queryset?
Options:
A) Filters results based on a condition
B) Fetches related objects with a single query
C) Aggregates query results
D) Performs case-insensitive searches        
    ''')

        score = evaluate(q4,'B',score)

        print("Feedback : select_related() fetches related objects in a single query to reduce database hits when accessing related objects.")


        q5 = input('''
Question: Explain the role of Django's signals in the framework.
Options:
A) Handling asynchronous tasks
B) Controlling URL routing
C) Implementing web sockets
D) Executing certain actions based on sender signals        
        
        ''')

        score = evaluate(q5,'D',score)

        print("Feedback : Django's signals allow decoupled applications to get notified when certain actions occur elsewhere in the codebase, often used for triggering actions on model events.")

        # Giving the Final Evaluation for Django
        final_evaluation(score)



    elif inp == 2:

        print('\n')
        intro_statement('Machine Learning')


        q1 = input('''
Question: What is an ensemble method in machine learning?
Options:
A) A single model that combines multiple algorithms
B) A method to preprocess data before modeling
C) An evaluation metric for model performance
D) A technique to visualize high-dimensional data

Enter your choice : ''')

        score = evaluate(q1, 'A', score)

        print(
            'Feedback : Ensemble methods combine multiple models to improve prediction accuracy and robustness.')

        q2 = input('''
Question: What is the purpose of regularization in machine learning?
Options:
A) To reduce overfitting in models
B) To increase model complexity
C) To speed up model training
D) To handle missing data in datasets

Enter your choice : ''')

        score = evaluate(q2, 'A', score)

        print(
            "Feedback : Regularization techniques help prevent overfitting by penalizing overly complex models.")

        q3 = input('''
Question: What is the difference between supervised and unsupervised learning?
Options:
A) Supervised learning uses labeled data; unsupervised learning uses unlabeled data
B) Supervised learning uses regression; unsupervised learning uses clustering
C) Supervised learning predicts categories; unsupervised learning predicts quantities
D) There is no difference between supervised and unsupervised learning
     
Enter your choice : ''')

        score = evaluate(q3, 'A', score)

        print(
            "Feedback : Supervised learning relies on labeled data with known outcomes, while unsupervised learning deals with unlabeled data to discover patterns.")

        q4 = input('''
Question: What is the purpose of the activation function in a neural network?
Options:
A) To initialize weights in the network
B) To calculate the loss function
C) To introduce non-linearity in the network
D) To adjust learning rates during training

Enter your choice : ''')

        score = evaluate(q4, 'C', score)

        print(
            "Feedback : Activation functions introduce non-linear transformations, enabling neural networks to model complex relationships between inputs and outputs.")

        q5 = input('''
Question: Explain the concept of bias-variance tradeoff in machine learning.
Options:
A) Balancing computational resources with model accuracy
B) Managing tradeoffs between model complexity and generalization
C) Balancing precision and recall in classification tasks
D) Adjusting hyperparameters to minimize model errors
        
Enter your choice : ''')

        score = evaluate(q5, 'B', score)

        print(
            "Feedback : The bias-variance tradeoff deals with the tradeoff between model simplicity (bias) and ability to capture patterns (variance) for optimal generalization to new data.")

        # Giving the Final Evaluation for Machine Learning
        final_evaluation(score)


    elif inp == 3:
        print('\n')
        intro_statement('Data Analysis')

        q1 = input('''
        Question: What is the purpose of exploratory data analysis (EDA) in data analysis?
        Options:
        A) To clean and preprocess raw data
        B) To visually analyze and summarize data characteristics
        C) To build machine learning models
        D) To perform statistical hypothesis testing

        Enter your choice : ''')

        score = evaluate(q1, 'B', score)

        print(
            'Feedback: Exploratory data analysis aims to visually analyze and summarize data characteristics to gain insights before modeling.')

        q2 = input('''
        Question: What does the term "Outlier" refer to in data analysis?
        Options:
        A) Data points that do not fit the expected pattern or distribution
        B) The center point in a dataset
        C) Values that fall within the interquartile range
        D) Extreme values that always indicate errors

        Enter your choice : ''')

        score = evaluate(q2, 'A', score)

        print(
            "Feedback: Outliers are data points that deviate significantly from other observations in a dataset, often indicating anomalies or errors.")

        q3 = input('''
        Question: What is the purpose of correlation analysis in data analysis?
        Options:
        A) To determine causation between variables
        B) To identify relationships and strength of associations between variables
        C) To perform clustering of similar data points
        D) To detect anomalies in the dataset

        Enter your choice : ''')

        score = evaluate(q3, 'B', score)

        print(
            "Feedback: Correlation analysis measures the strength and direction of relationships between variables in a dataset.")

        q4 = input('''
        Question: What does the term "P-value" represent in statistical analysis?
        Options:
        A) The probability that the null hypothesis is true
        B) The significance level of the test
        C) The range of confidence intervals
        D) The number of variables in a regression model

        Enter your choice : ''')

        score = evaluate(q4, 'A', score)

        print(
            "Feedback: The P-value represents the probability of observing the data given that the null hypothesis is true in statistical hypothesis testing.")

        q5 = input('''
        Question: What is the purpose of a Boxplot in data analysis?
        Options:
        A) To visualize distributions of a single variable
        B) To compare distributions of multiple variables
        C) To detect outliers in the dataset
        D) All of the above

        Enter your choice : ''')

        score = evaluate(q5, 'D', score)

        print(
            "Feedback: Boxplots visualize distributions of variables, compare distributions between groups, and identify outliers.")

        # Giving the Final Evaluation for Data Analysis
        final_evaluation(score)


else:

        print("Invalid Choice !!")





