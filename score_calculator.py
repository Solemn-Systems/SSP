def calculate_scores(system):
    if not all(k in system for k in ['data_integrity', 'user_autonomy', 'transparency', 'environmental_impact', 'social_responsibility']):
        raise ValueError("Missing required input fields")

    scores = {
        "Data Integrity": system['data_integrity'],
        "User Autonomy": system['user_autonomy'],
        "Transparency": system['transparency'],
        "Environmental Impact": system['environmental_impact'],
        "Social Responsibility": system['social_responsibility']
    }

    return scores

# Example usage
if __name__ == "__main__":
    system_input = {
        "data_integrity": 4,
        "user_autonomy": 3,
        "transparency": 5,
        "environmental_impact": 2,
        "social_responsibility": 4
    }

    results = calculate_scores(system_input)
    for category, score in results.items():
        print(f"{category}: {score}/5")
