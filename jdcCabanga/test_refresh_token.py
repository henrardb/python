#!/usr/bin/env python3

import requests
import json
REFRESH_TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2Nzc2MTM0MC00YmQxLTRkZWQtYWY4Mi00ZTg4NzU5NjNmZDIifQ.eyJleHAiOjE3NjMzOTg1MzQsImlhdCI6MTc2Mjc5MzczNCwianRpIjoiZTZkMWI4NzAtYjY0Ni1jZTQ3LTM3ZmYtYzA0M2Q2YjM0MTQ4IiwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5zY29sYXJlcy5iZS9hdXRoL3JlYWxtcy9ob3Jpem9uIiwiYXVkIjoiaHR0cHM6Ly9sb2dpbi5zY29sYXJlcy5iZS9hdXRoL3JlYWxtcy9ob3Jpem9uIiwic3ViIjoiMjMyZTYyMGYtMWUzNi00MTc5LWIxMWQtZWVmOGJkY2MxMjc0IiwidHlwIjoiUmVmcmVzaCIsImF6cCI6ImNhYmFuZ2EtZnJvbnRlbmQiLCJzaWQiOiJhZDYzY2Y3MS04OWIzLTg1OWUtNmNjNS01MGUwNGE0YTIzMTYiLCJzY29wZSI6Im9wZW5pZCB3ZWItb3JpZ2lucyBlbWFpbCByb2xlcyBwcm9maWxlIGJhc2ljIn0.zuAl2mKC5o-kSigkVzh7zBwPss3W6FNhj87ZyxnR2BbFEKm-Xn2bqDePOacJxgSlrCelXi1wlBi-14cJZSQe3Q"
TOKEN_URL = "https://login.scolares.be/auth/realms/horizon/protocol/openid-connect/token"
CLIENT_ID = "cabanga-frontend" 


def refresh_access_token(current_refresh_token: str):
    print("-> Try token refresh...")
    
    payload = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "refresh_token": current_refresh_token,
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(TOKEN_URL, data=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        token_data = response.json()
        
        if "access_token" in token_data and "refresh_token" in token_data:
            print("Refresh token success.")
            return {
                "access_token": token_data["access_token"],
                "refresh_token": token_data["refresh_token"],
                "expires_in": token_data.get("expires_in")
            }
        print("Wrong response token.")
        
        return None

    except requests.exceptions.HTTPError as e:
        if response.status_code == 400:
             print("Refresh token revoked or expired.")
        else:
             print(f"HTTP error during refresh: {e}")
        return None


if __name__ == "__main__":
    print(f"Start token: {REFRESH_TOKEN[:20]}...")

    new_token = refresh_access_token(REFRESH_TOKEN)

    if new_token:
        print(f"New access token: {new_token['access_token']}")
        print(f"New refresh token: {new_token['refresh_token'][:50]}")
        print(f"Expires in: {new_token['expires_in']} seconds")
    else:
        print("\nRefresh failed.")
