import re

def extract_features(url):
    features = []

    # 1. URL length
    features.append(len(url))

    # 2. @ symbol
    features.append(1 if "@" in url else 0)

    # 3. Dot count
    features.append(url.count("."))

    # 4. Hyphen
    features.append(1 if "-" in url else 0)

    # 5. HTTPS
    features.append(1 if url.startswith("https") else 0)

    # 6. IP address
    ip_pattern = re.compile(
        r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
    )
    features.append(1 if ip_pattern.search(url) else 0)

    return features
