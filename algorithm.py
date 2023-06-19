import operator

def get_best_substitute(teachers_list, subject):
    """
    Function to select the best substitute teacher based on experience, subject expertise, and proximity.
    Args:
        teachers_list (list): A list of dictionaries, each representing a teacher.
        subject (str): The subject for which a substitute teacher is required.
    Returns:
        dict: The best substitute teacher.
    """

    scores = {}

    for i, teacher in enumerate(teachers_list):
        # Initialize score to 0
        scores[i] = 0

        # Check subject expertise
        if subject in teacher['expertise']:
            scores[i] += 10

        # Years of experience (assuming that more years of experience is better)
        # Add one point for every year of experience
        scores[i] += teacher['experience_years']

        # Proximity to school (assuming that closer is better)
        # Subtract one point for every 10 kilometers away from the school
        scores[i] -= teacher['distance_km'] / 10

    # Find the teacher with the highest score
    best_teacher_index = max(scores.items(), key=operator.itemgetter(1))[0]

    return teachers_list[best_teacher_index]
