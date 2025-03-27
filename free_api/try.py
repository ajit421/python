import requests
from PIL import Image
from io import BytesIO
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def api_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data['success']:
        api_username = data["data"]["login"]["username"]
        api_pass = data["data"]["login"]["password"]
        api_country = data["data"]["location"]["country"]
        api_picture = data["data"]["picture"]["large"]
        return api_username, api_pass, api_country, api_picture
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        api_username, api_pass, api_country, api_picture = api_user()

        # Fetch the image from the URL
        img_response = requests.get(api_picture)
        img = Image.open(BytesIO(img_response.content))

        # Print user details
        console.print(Panel(f"[bold]Username:[/bold] {api_username}\n"
                            f"[bold]Password:[/bold] {api_pass}\n"
                            f"[bold]Country:[/bold] {api_country}",
                            title="User Info", expand=False))

        # Show the image in the VS Code terminal
        console.print(f"![User Image]({api_picture})")

    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

if __name__ == '__main__':
    main()
