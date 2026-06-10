# Sample user preferences
users = {
    "Brindha": ["Python", "AI", "Machine Learning"],
    "Rahul": ["Python", "Web Development", "Flask"],
    "Priya": ["AI", "Data Science", "Machine Learning"]
}

def recommend(user_name):
    user_interests = users[user_name]

    recommendations = set()

    for other_user, interests in users.items():
        if other_user != user_name:
            common = set(user_interests) & set(interests)

            if common:
                recommendations.update(interests)

    recommendations -= set(user_interests)

    return list(recommendations)

# Test
print("Recommendations for Brindha:")
print(recommend("Brindha"))