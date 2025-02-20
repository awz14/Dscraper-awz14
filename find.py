import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random
import os
import time

INVITE_FILE = "invites.txt"
BASE_URL = "https://discadia.com"
SORTED_URL = BASE_URL + "/?sort=member"  # Sorted by members

# Load previously saved invites
def load_existing_invites(filename=INVITE_FILE):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return set(f.read().splitlines())  # Return a set of invites
    return set()

# Save new invites
def save_invites(invites, filename=INVITE_FILE):
    with open(filename, 'a') as f:
        for invite in invites:
            f.write(f"{invite}\n")

# Scrape multiple pages of Discadia with error handling
def get_discadia_invites(min_members=10000, limit=100):
    print(f"Scraping {SORTED_URL}")

    invites = set()
    existing_invites = load_existing_invites()

    page = 1
    while len(invites) < limit:
        url = f"{SORTED_URL}&page={page}"
        print(f"Fetching page {page} -> {url}")

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            servers = soup.find_all('div', class_='server-card')  # Adjust class if needed
            print(f"Found {len(servers)} servers on page {page}.")

            if not servers:
                break  # No more servers to scrape

            for server in servers:
                # Extract invite link
                invite_tag = server.find('a', href=True)
                if not invite_tag:
                    continue
                invite_url = urljoin(BASE_URL, invite_tag["href"])

                # Extract member count
                member_tag = server.find('span', class_='self-center text-xs text-gray-400 ml-0.5')
                if not member_tag:
                    continue

                try:
                    member_count = int("".join(filter(str.isdigit, member_tag.text)))  # Extract numbers only
                except ValueError:
                    continue

                if member_count < min_members:
                    continue  # Skip servers with fewer than 10k members

                if invite_url in existing_invites or invite_url in invites:
                    continue  # Skip duplicates

                invites.add(invite_url)
                print(f"✅ Found: {invite_url} ({member_count} members)")

                if len(invites) >= limit:
                    break  # Stop when we reach the limit

            page += 1  # Go to the next page
            time.sleep(1)  # Add a short delay to prevent rate-limiting

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break

    # Save new invites
    save_invites(invites)

    # Ensure 100 servers by backfilling from previous ones
    all_invites = list(existing_invites.union(invites))  # Combine new & old
    random.shuffle(all_invites)
    
    invites = all_invites[:limit]  # Trim to exactly 100

    if not invites:
        print("❌ No servers found! Try again later.")
        return []

    return invites

# Run script
if __name__ == "__main__":
    invites = get_discadia_invites()
    if invites:
        print("\n✅ Found 100 unique Discord servers with 10k+ members:")
        for invite in invites:
            print(invite)
    else:
        print("\n❌ No new servers were found, and no previous servers exist!")
