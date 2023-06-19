import operator
from datetime import datetime, timedelta

def get_best_substitute(teachers_list, subject):
    """
    Function to select the best substitute teacher based on experience, subject expertise, 
    proximity, previous performance and preferences.
    Args:
        teachers_list (list): A list of dictionaries, each representing a teacher.
        subject (str): The subject for which a substitute teacher is required.
    Returns:
        dict: The best substitute teacher.
    """

    scores = {}
    now = datetime.now()

    for i, teacher in enumerate(teachers_list):
        # Initialize score to 0
        scores[i] = 0

        # Check subject expertise: high expertise adds 30, medium adds 20, low adds 10, none adds 0
        if subject in teacher['expertise']:
            if teacher['expertise'][subject] == 'high':
                scores[i] += 30
            elif teacher['expertise'][subject] == 'medium':
                scores[i] += 20
            elif teacher['expertise'][subject] == 'low':
                scores[i] += 10

        # Years of experience (assuming that more years of experience is better)
        # Add 0.5 point for every year of experience up to 10 years, then 0.25 points for each additional year
        if teacher['experience_years'] <= 10:
            scores[i] += 0.5 * teacher['experience_years']
        else:
            scores[i] += 5 + 0.25 * (teacher['experience_years'] - 10)

        # Proximity to school (assuming that closer is better)
        # Subtract one point for every 10 kilometers away from the school, with a maximum of 10 points subtracted
        distance_score = min(10, teacher['distance_km'] / 10)
        scores[i] -= distance_score

        # Previous performance (assuming that higher is better)
        # Add performance score, but decrease its value based on how long ago the performance was evaluated
        # Assume performance is a list of dictionaries with 'score' and 'date' keys
        for performance in teacher['performance']:
            days_ago = (now - performance['date']).days
            decay_factor = 1 / (1 + days_ago / 365)  # Decrease the value of older performances
            scores[i] += performance['score'] * decay_factor

        # Preferences
        # Add 5 points if the teacher has expressed a preference for the school or subject
        if 'preferences' in teacher:
            if 'schools' in teacher['preferences'] and school in teacher['preferences']['schools']:
                scores[i] += 5
            if 'subjects' in teacher['preferences'] and subject in teacher['preferences']['subjects']:
                scores[i] += 5

    # Find the teacher with the highest score
    best_teacher_index = max(scores.items(), key=operator.itemgetter(1))[0]

    return teachers_list[best_teacher_index]
