from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

texte1 = "Je suis tellement heureux aujourd'hui !"
texte2 = "C'était une journée horrible."

score1 = analyser.polarity_scores(texte1)
score2 = analyser.polarity_scores(texte2)

print(f"Texte : {texte1} | Score : {score1}")
print(f"Texte : {texte2} | Score : {score2}")
