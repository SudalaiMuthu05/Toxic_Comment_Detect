# Toxic_Comment_Detect

Project Description

The Toxic Comment Detection and Moderation Module is an intelligent system designed to automatically identify, block, and log harmful or abusive comments on web and social media platforms. The primary objective of this project is to create a safer online environment by preventing toxic content from being published in real time. The system integrates Natural Language Processing (NLP) and Machine Learning techniques to analyze user-generated text before it appears on the platform.

When a user submits a comment, it is sent to a Flask-based backend through a REST API, where the text undergoes preprocessing and feature extraction using TF-IDF vectorization. The processed text is then evaluated by a trained Scikit-learn classification model to determine whether it is toxic or non-toxic. Safe comments are published normally, while toxic comments are instantly blocked and stored securely in a SQLite database along with user details, IP address, toxicity count, and timestamp information.

The system also includes an IP-based monitoring mechanism that tracks repeated violations and can automatically restrict users after multiple toxic attempts. Designed as a modular solution, this system can be seamlessly integrated into platforms such as Instagram clones or other web applications, combining full-stack development, machine learning, and security principles to enable real-time content moderation and secure logging.
