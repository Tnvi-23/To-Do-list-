import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Task

def suggest_daily_tasks(user):
    tasks = Task.objects.filter(user=user)
    if not tasks.exists():
        return ["No history yet. Add tasks!"]

    df = pd.DataFrame(list(tasks.values("title")))
    vectorizer = CountVectorizer().fit_transform(df["title"])
    similarity = cosine_similarity(vectorizer)

    # Pick most common tasks
    common_tasks = df["title"].value_counts().head(3).index.tolist()
    return common_tasks
