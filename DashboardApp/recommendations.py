import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from DashboardApp.models import Event, Lesson
from AuthenticationApp.models import CustomUser

def get_recommendations(user):
    """Generate event and lesson recommendations for a user."""
    
    # Fetch user interests
    user_interests = user.interest  # Assuming 'interest' is a text field in CustomUser
    if not user_interests:
        return [], []  # Return empty lists if no interests are defined

    # Fetch all events and lessons
    events = list(Event.objects.all().values('id', 'name', 'description'))  # 'name' instead of 'title'
    lessons = list(Lesson.objects.all().values('id', 'title', 'content'))  # Assuming 'title' for lessons

    # Combine data into a dataframe
    data = pd.DataFrame(events + lessons)
    data['content'] = data['description'].fillna('') + ' ' + data.get('content', '').fillna('')

    # Include user interests in the dataset using pd.concat() instead of append
    user_data = pd.DataFrame([{'id': 'user', 'content': user_interests}])
    data = pd.concat([data, user_data], ignore_index=True)

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(data['content'])

    # Compute similarity between user interests and events/lessons
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Get top recommendations
    recommendations = np.argsort(cosine_sim[0])[::-1]  # Sort by similarity score
    top_recommendations = [data.iloc[i]['id'] for i in recommendations[:5]]  # Get top 5

    # Fetch recommended events and lessons
    recommended_events = Event.objects.filter(id__in=top_recommendations)
    recommended_lessons = Lesson.objects.filter(id__in=top_recommendations)
    
    # Return both separately for rendering in template
    return recommended_events, recommended_lessons
