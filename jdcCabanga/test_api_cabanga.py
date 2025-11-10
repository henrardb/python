#!/usr/bin/env python3

import requests
import json
from datetime import date, timedelta

ACCESS_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIwdXZkTUROR215QktvTVFsel9WcXFCQmhBU1c3N0VVNkstYldJNWh0eWk4In0.eyJleHAiOjE3NjI3OTYzODYsImlhdCI6MTc2Mjc5NjA4NiwiYXV0aF90aW1lIjoxNzYyNzkwOTc3LCJqdGkiOiJvbnJ0cnQ6MjVmODdlNmYtODVhNi1jNTM3LWI3YTMtZmE1YjViOWJjMTZiIiwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5zY29sYXJlcy5iZS9hdXRoL3JlYWxtcy9ob3Jpem9uIiwiYXVkIjpbInJlZmVyZW5jZS1kYXRhLWFwaSIsInN0dWRlbnQtYXBpIiwiY2FiYW5nYS1hcGkiXSwic3ViIjoiMjMyZTYyMGYtMWUzNi00MTc5LWIxMWQtZWVmOGJkY2MxMjc0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2FiYW5nYS1mcm9udGVuZCIsInNpZCI6ImFkNjNjZjcxLTg5YjMtODU5ZS02Y2M1LTUwZTA0YTRhMjMxNiIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwczovL3d3dy5hcHAuY2FiYW5nYS5iZSIsImh0dHBzOi8vYXBwLmNhYmFuZ2EuYmUiLCJodHRwczovL2NhYmFuZ2Euc2NvbGFyZXMuYmUiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLWNhYmFuZ2EiXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWZlcmVuY2UtZGF0YS1hcGkiOnsicm9sZXMiOlsiVVNFUiJdfSwic3R1ZGVudC1hcGkiOnsicm9sZXMiOlsiVVNFUiJdfSwiY2FiYW5nYS1hcGkiOnsicm9sZXMiOlsiVVNFUiJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6ImJydW5vLmhlbnJhcmRAZ21haWwuY29tIiwiZW1haWwiOiJicnVuby5oZW5yYXJkQGdtYWlsLmNvbSJ9.O_qi7Oe-0UQ3LZyyG6wgjCvNIw1kiJRfjzgPlp4BcfHQe-SVQe58ZyEawgyhBk5XXPQZsUVuhfw2YAsaAb5Gg6fpj8BLHtBGQQQg6H3JDCrjzQAZg4uXG7Ev4yuK_aNgwK4DzMbHI3Kynp85Chnt4uhByiGRj5dQKoWLmhGY0rjojs8P4kn4sgOAstWWry_CnbeA_LkdVvSUdumFMe3uEoitIZyQYcKWK6mcOUzQxP7nPSqc5s_vBklt9wP9MNwjcQOqALrpAx0jzLWUsudyFRSZW-aD78fiSxMLYKXEFoVNBFxgxg1jXsORVX7obri99kxaZ7OXLX-dBkEytBjmPw"

STUDENT_ID = "20692610"
SCHOOL_CODE = "STBENHABAY"

TODAY = date(2025, 11, 10)
END_DATE = TODAY + timedelta(days=4)

DIARY_URL = (
    f"https://api.scolares.be/cabanga/api/schools/{SCHOOL_CODE}/students/{STUDENT_ID}/diary"
    f"?from={TODAY.isoformat()}&to={END_DATE.isoformat()}"
)


def get_diary_data(token: str, url: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }

    print(f"-> Connexion to API: {DIARY_URL}")

    try:
        response = requests.get(url, headers=headers, timeout=10)

        response.raise_for_status()

        print(f"Success: {response.status_code}")
        return response.json()

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error: {errh}")
        if response.status_code == 401 or response.status_code == 403:
            print("   Access token expired or invalid.")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
        return None


if __name__ == "__main__":
    data = get_diary_data(ACCESS_TOKEN, DIARY_URL)

    if data:
        print("--- Received JSON ---")
        print(json.dumps(data[:3], indent=4))
        print(f"Number of elements: {len(data)}")
