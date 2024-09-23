from serpapi import GoogleSearch
import json
import pandas as pd

# Must perform  pip install google-search-results to get GoogleSearch library

params = {
    "api_key": "a1ac8e27db5406f5e8f793ce30f9803d40953234717e290114d3afd1dd08a0e9",
    "engine": "google_scholar",
    "q": "Bone Bioreactor",
    "hl": "en",
    "num": 100,
}

# # search = GoogleSearch(params)
# results = search.get_dict()
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(results, f, ensure_ascii=False, indent=4)
# print(results)

with open("data.json", encoding="utf-8") as f:
    results = json.load(f)
    citations = [
        results["organic_results"][i]["inline_links"]["cited_by"]["total"]
        for i in range(len(results["organic_results"]))
    ]
    sorted_citations = [
        b[:] for b in sorted(enumerate(citations), key=lambda i: i[1], reverse=True)
    ]

    # sorted_indices = [b[1] for b in sorted(enumerate(citations), key=lambda i: i[1])]
    print(sorted_citations)

    titles = [
        results["organic_results"][sorted_citations[i][0]]["title"]
        for i in range(len(sorted_citations))
    ]

    data = {
        "Title": titles,
        "Citations": [sorted_citations[i][1] for i in range(len(sorted_citations))],
    }

    df = pd.DataFrame(data)
    print(df)
