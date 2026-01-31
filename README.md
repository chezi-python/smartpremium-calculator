■■ Swiggy Restaurant Finder
Content-Based Restaurant Recommendation System using Streamlit
Project Overview
A content-based restaurant recommendation web application built using Python, Scikit-learn, and
Streamlit. The system recommends restaurants based on city, cuisine preference, rating, and cost
with an intelligent fallback mechanism.


Key Features
- City-based restaurant filtering
- Cuisine preference matching
- Rating-aware recommendations
- Cost sensitivity handling
- Weighted cosine similarity engine
- Smart nearest-city fallback logic
- Optimized performance with Streamlit caching


Recommendation Logic
The recommendation engine uses content-based filtering. Restaurant attributes are one-hot
encoded and compared with a dynamically built user preference vector using weighted cosine
similarity. Cuisine, rating, and cost are assigned different importance levels to improve
recommendation relevance.

Tech Stack
Python, Streamlit, Pandas, NumPy, Scikit-learn


How to Run
1. Install dependencies using requirements.txt
2. Run the app using: streamlit run app.py
4. Open browser at http://localhost:8501


Author
Elancheziyan R – Data Science & Machine Learning Enthusiast

