# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:42:03 2024

@author: Admin
"""

# Pr : 05 ( Hospital Expert System )

def patient_triage():
    print("Welcome to the Hospital Triage System!")
    print("Please answer the following questions with 'Yes' or 'No'.")
    symptoms = {
        "Difficulty Breathing": 0,
        "Chest Pain": 0,
        "Unconsciousness": 0,
        "Severe Bleeding": 0,
        "High Fever": 0
    }
    # Ask questions about symptoms and assign severity based on user input
    for symptom in symptoms:
        answer = input(f"Do you have {symptom}? ").lower()
        if answer == "yes":
            symptoms[symptom] = 1

    # Evaluate the overall severity based on symptoms
    total_severity = sum(symptoms.values())
    print("Thank you for your responses.")

    # Provide triage recommendation based on the total severity
    if total_severity >= 4:
        print("Based on your symptoms, you should seek immediate medical attention.")
    elif total_severity >= 2:
        print("Based on your symptoms, you should see a doctor soon.")
    else:
        print("Based on your symptoms, you can wait for medical attention.")
    
    # Provide possible diseases based on reported symptoms
    print("Possible diseases based on reported symptoms:")
    if symptoms["Difficulty Breathing"] and symptoms["Chest Pain"]:
        print("- You may have a heart-related condition.")
    if symptoms["Unconsciousness"]:
        print("- You may have suffered a stroke or severe head injury.")
    if symptoms["Severe Bleeding"]:
        print("- You may have a serious injury or hemorrhage.")
    if symptoms["High Fever"]:
        print("- You may have an infection or flu.")
    if not any(symptoms.values()):
        print("- No specific disease can be identified based on the reported symptoms.")

# Call the function for patient triage
patient_triage() 


# output :
# Welcome to the Hospital Triage System!
# Please answer the following questions with 'Yes' or 'No'.
# Do you have Difficulty Breathing? yes
# Do you have Chest Pain? yes
# Do you have Unconsciousness? yes
# Do you have Severe Bleeding? yes
# Do you have High Fever? yes
# Thank you for your responses.
# Based on your symptoms, you should seek immediate medical attention.
# Possible diseases based on reported symptoms:
# - You may have a heart-related condition.
# - You may have suffered a stroke or severe head injury.
# - You may have a serious injury or hemorrhage.
# - You may have an infection or flu.