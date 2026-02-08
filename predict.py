import pickle
from feature_extraction import extract_features

print("Loading model...")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully")

url = input("Enter URL to check: ").strip()

if not url:
    print("❌ No URL entered")
    exit()

features = extract_features(url)

print("Extracted features:", features)
print("Feature count:", len(features))

prediction = model.predict([features])

print("Raw prediction:", prediction)

if prediction[0] == 1:
    print("⚠️ Phishing Website")
else:
    print("✅ Legitimate Website")

