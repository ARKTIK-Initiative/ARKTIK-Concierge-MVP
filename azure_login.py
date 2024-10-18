
# ARKTIK Azure Authentication 🌌
# Elegant, secure, and seamless – because luxury starts with a smooth login experience. 🛡️

from azure.identity import InteractiveBrowserCredential
from msgraph.core import GraphClient
import sys

# Your Azure Application Client ID (replace with your actual client ID)
CLIENT_ID = "YOUR_CLIENT_ID"

def authenticate_user():
    """
    Authenticate the user through Azure Active Directory.
    Opens an interactive browser for login and fetches the user profile.
    """
    try:
        print("🌐 Opening your ARKTIK portal... Please wait.")
        
        # Set up interactive browser-based authentication
        credential = InteractiveBrowserCredential(client_id=CLIENT_ID)
        client = GraphClient(credential=credential)

        # Fetch and display authenticated user profile details
        user = client.get("/me").json()
        print(f"✨ Welcome, {user['displayName']}! Your ARKTIK experience begins now.")

    except Exception as e:
        # Graceful error handling with a touch of ARKTIK flair
        print("🚫 Authentication failed. Please try again.")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🔑 Starting ARKTIK Azure Authentication...")
    authenticate_user()
