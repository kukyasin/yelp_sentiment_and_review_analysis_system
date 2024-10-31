import random

# Yelp ile ilgili yerler
# Yelp ile ilgili yerler
places = [
    "restaurant", "cafe", "diner", "bar", "bistro", "food truck", 
    "pizzeria", "brewery", "steakhouse", "bakery", "ice cream shop", 
    "sushi bar", "breakfast spot", "fast food place", "coffee shop", 
    "salad bar", "taco stand", "fine dining restaurant", "brunch place", 
    "caterer", "wine bar", "juice bar", "tea shop", "pub", 
    "rooftop bar", "deli", "sandwich shop", "buffet", "market"
]

# Olumlu sıfatlar
adjectives_positive = [
    "amazing", "great", "fantastic", "wonderful", "excellent", 
    "superb", "delicious", "tasty", "incredible", "outstanding", 
    "fresh", "authentic", "charming", "cozy", "friendly", 
    "helpful", "inviting", "satisfying", "spectacular", "yummy", 
    "mouthwatering", "top-notch", "vibrant", "quaint", 
    "remarkable", "generous", "perfect", "exceptional", "wholesome"
]

# Olumsuz sıfatlar
adjectives_negative = [
    "terrible", "bad", "awful", "poor", "horrible", 
    "disappointing", "mediocre", "bland", "overcooked", 
    "undercooked", "rude", "slow", "dirty", "unpleasant", 
    "expensive", "small", "crowded", "noisy", "chaotic", 
    "lackluster", "dismal", "uninviting", "subpar", 
    "greasy", "stale", "forgettable", "shoddy", "awkward", 
    "unprofessional", "dry", "inconvenient", "disorganized"
]

# Nötr sıfatlar
adjectives_neutral = [
    "okay", "average", "fine", "decent", "satisfactory", 
    "unremarkable", "acceptable", "moderate", "standard", 
    "typical", "ordinary", "run-of-the-mill", "so-so", 
    "nothing special", "plain", "simple"
]


def generate_random_review():
    place = random.choice(places)
    sentiment = random.choice(["positive", "negative", "neutral"])
    
    if sentiment == "positive":
        adjective = random.choice(adjectives_positive)
        review_template = random.choice([
            f"I absolutely loved my experience at this {place}! The atmosphere was {adjective}.",
            f"What a {adjective} {place}! I can't wait to come back.",
            f"The {place} exceeded my expectations with its {adjective} service and ambiance.",
            f"I'm thrilled with my visit to this {place}; it was {adjective}!",
            f"This {place} is simply {adjective}. I highly recommend it!"
        ])
    elif sentiment == "negative":
        adjective = random.choice(adjectives_negative)
        review_template = random.choice([
            f"I was really disappointed by my visit to this {place}; it was {adjective}.",
            f"This {place} didn't meet my expectations. It was {adjective}.",
            f"I can't say I enjoyed my time at this {place}. It was {adjective}.",
            f"My experience at this {place} was quite {adjective}, to say the least.",
            f"I regret choosing this {place}. The service was {adjective}."
        ])
    else:
        adjective = random.choice(adjectives_neutral)
        review_template = random.choice([
            f"My time at this {place} was just {adjective}. It’s okay.",
            f"This {place} was fairly {adjective}. Nothing stood out.",
            f"I had an {adjective} experience at this {place}. It was alright.",
            f"This {place} is pretty {adjective}. I wouldn’t go out of my way for it.",
            f"My visit to this {place} was {adjective}. Just average."
        ])
    
    return review_template

# 100 örnek oluştur
reviews = [{"text": generate_random_review(), 
            "label": "positive" if "fantastic" in generate_random_review() 
                      else "negative" if "terrible" in generate_random_review() 
                      else "neutral"} for _ in range(300)]

# Yorumları yazdır
for review in reviews:
    print(review)
