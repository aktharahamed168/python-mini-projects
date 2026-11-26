import requests


def find_github_profile(username):

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            print("\n===== GitHub Profile Finder =====")

            print("Username:", data["login"])
            print("Name:", data["name"] or "Not available")
            print("Bio:", data["bio"] or "Not available")
            print("Location:", data["location"] or "Not available")
            print("Public Repositories:", data["public_repos"])
            print("Followers:", data["followers"])
            print("Following:", data["following"])
            print("Created At:", data["created_at"])
            print("Profile URL:", data["html_url"])

        elif response.status_code == 404:

            print("\nGitHub user not found.")

        elif response.status_code == 403:

            print("\nGitHub API rate limit exceeded.")

        else:

            print("\nSomething went wrong.")
            print("Status Code:", response.status_code)

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")

    except requests.exceptions.ConnectionError:
        print("\nPlease check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("\nError:", error)


print("===== GitHub Profile Finder =====")

username = input("Enter GitHub username: ").strip()

if username:
    find_github_profile(username)
else:
    print("Username cannot be empty.")
