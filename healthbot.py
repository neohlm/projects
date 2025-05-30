#Neo Hlumbene
#This is a simple diagnostic chatbot using a knowledge base from FOL facts and rules

#knowledge base                 #Converting FOL to sentences
knowledge_base = {
    'flu': [
        'HasSymptom(X, fever)', #A person has a fever symptom
        'HasSymptom(X, cough)', #A person has a cough symptom
        'HasSymptom(X, sore_throat)'#A person has a sore throat symptom 
    ],
    'common_cold': [
        'HasSymptom(X, sneezing)',#A person has a sneezing symptom
        'HasSymptom(X, runny_nose)',#A person has a runny nose symptom
        'HasSymptom(X, mild_fever)'#A person has a mild fever symptom
    ],
    'malaria': [
        'HasSymptom(X, fever)', 
        'HasSymptom(X, chills)',#A person has a chills symptom
        'HasSymptom(X, sweating)',#A person has a sweating symptom
        'HasSymptom(X, headache)'#A person has a headache symptom
    ],
    'covid19': [
        'HasSymptom(X, fever)',
        'HasSymptom(X, cough)',
        'HasSymptom(X, shortness_of_breath)',#A person has a shortness of breadth symptom
        'HasSymptom(X, loss_of_taste)'#A person has a loss of taste symptom
    ],
    'strep_throat': [
        'HasSymptom(X, sore_throat)',
        'HasSymptom(X, swollen_lymph_nodes)',#A person has a swollen lymph nodes symptom
        'HasSymptom(X, fever)'
    ]
}

#advice
advice_base = {
    'flu': [
        "1. Drink plenty of fluids",
        "2. rest",
        "3. and consult a doctor if symptoms worsen"
    ],
    'common_cold': [
        "1. Try using nasal saline if there's congestion",
        "2. Use a humidifier to ease breathing",
        "3. and consult a doctor if symptoms worsen"
    ],
    'malaria': [
        "1. Seek medical attention immediately!",
        "2. Always use the drugs you were prescribed for antimalarial",
        "3. Monitor your body temperature regularly"
    ],
    'covid19': [
        "1. Go into quarantine immediately and take a covid19 test",
        "2. Monitor your oxygen levels",
        "3. Consult a doctor about antiviral treatments"
    ],
    'strep_throat': [
        "1. Use warm salt water to gargle your throat",
        "2. rest",
        "3. Monitor your body temperature regularly"
    ]
}

#diagnosis
def diagnose(symptoms): #checking if user input has any matches with symptoms in the database
    matches = []
    for disease, reqs in knowledge_base.items():
        if all(req in symptoms for req in reqs):
            matches.append(disease)
    return matches



#chatbot
def chat():
    print("\n" + "*"*30) #interacting with the user
    print("🩺 Welcome to HealthBot!")
    print("*"*30 + "\n")
            
    print("Please enter your symptoms (comma-seperated): (e.g. fever'). Type 'done' when finished.\n")#asking for user input
    
    #Validating user input
    symptoms = []
    while True:
        symptom = input("Symptom: ").strip().lower()
        if symptom == 'done':
            break
        if symptom:  
            symptoms.append("HasSymptom(X, {symptom.replace(' ', '_')})")
    
    print("\n" + "-"*40)
    print("🔍  Analyzing symptoms...")
    diagnoses = diagnose(symptoms)
    
    if diagnoses:
        print("\nPossible conditions detected:") #display diagnosis if it is found
        for idx, disease in enumerate(diagnoses, 1):
            print(" {idx}. {disease.upper()}")
        
        print("\nRecommended Actions:")
        for disease in diagnoses:
            print("\nFor {disease}:")
            for advice in advice_base.get(disease, []):
                print(" {advice}")
    else:
        print("\nBased on your symptoms you might have:") #no diagnosis
        print("- strep throat")
        print("Advice: Use warm salt water to gargle your throat, rest. Monitor your body temperature regularly")
        #print("Consider going to a pharmacist for symptom relief medication")
    
    print("\n" + "*"*30)
    print("✅  Consultation complete. Remember, an apple a day keeps a doctor away!\n") #program closing



#main function
if __name__ == "__main__":
    chat()
