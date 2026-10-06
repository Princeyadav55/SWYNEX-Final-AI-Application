# 🤖 SWYNEX Final AI Application — Smart SMS Risk Analyzer

## 📌 Project Overview

Smart SMS Risk Analyzer is a beginner-friendly AI application developed as the final project of the SWYNEX Technologies internship.

The application uses Machine Learning and intelligent rule-based analysis to identify potentially suspicious SMS messages.

It predicts whether an SMS is:

- 🚨 Spam
- ✅ Not Spam

It also provides:

- Model confidence
- Spam probability
- Risk level
- Suspicious indicators
- Safety recommendation

---

## 🎯 Problem Statement

SMS messages are commonly used for communication, but users may receive unwanted or suspicious messages containing:

- Fake rewards
- Urgent requests
- Financial scams
- Suspicious links
- Promotional spam

It can be difficult for users to quickly identify these messages.

This project aims to provide a simple AI-assisted tool that helps users understand the potential risk of an SMS message.

---

## 🎯 Objective

The main objectives of this project are:

1. Classify SMS messages as Spam or Not Spam.
2. Display the model's confidence.
3. Estimate the probability that a message is spam.
4. Detect suspicious indicators in the message.
5. Assign a risk level.
6. Provide a simple safety recommendation.
7. Present the results through a beginner-friendly interface.

---

## 🧠 How the Application Works

The application follows this workflow:

SMS Message

↓

Text Processing

↓

TF-IDF Vectorization

↓

Multinomial Naive Bayes Model

↓

Spam / Not Spam Prediction

↓

Probability & Confidence

↓

Intelligent Indicator Analysis

↓

Risk Assessment

↓

Safety Recommendation

---

## 🤖 Machine Learning Method

The application uses a trained Machine Learning pipeline.

### TF-IDF Vectorization

TF-IDF converts text into numerical features that can be processed by the Machine Learning model.

### Multinomial Naive Bayes

The Multinomial Naive Bayes classifier is used for SMS text classification.

The model predicts whether the input message is likely to be Spam or Not Spam.

---

## 🔎 Intelligent Risk Analysis

In addition to the Machine Learning prediction, the application performs rule-based analysis to identify suspicious patterns.

Examples include:

- 🎁 Prize or reward-related words
- ⚡ Urgency-related language
- 💰 Financial requests
- 🔗 Suspicious links
- 📢 Promotional language

These indicators are combined with the model prediction to provide a simple risk assessment.

---

## ⚠️ Risk Levels

The application provides three risk levels:

### 🔴 HIGH

The message has a high probability of being suspicious.

### 🟠 MEDIUM

The message contains some suspicious characteristics and should be verified.

### 🟢 LOW

No major suspicious risk was detected by the application.

---

## ✨ Main Features

- SMS Spam Classification
- Machine Learning based prediction
- TF-IDF text representation
- Multinomial Naive Bayes classifier
- Model confidence
- Spam probability
- Intelligent suspicious-indicator detection
- Risk-level assessment
- Safety recommendation
- Example spam and normal messages
- Input validation
- Error handling
- Beginner-friendly Streamlit interface

---

## 🖥️ Application Interface

The application allows users to enter an SMS message and analyze it.

The result includes:

- Prediction
- Model confidence
- Spam probability
- Risk level
- Detected indicators
- Safety recommendation

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Princeyadav55/SWYNEX-Final-AI-Application.git