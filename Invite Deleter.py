import requests, os

token = input(" [>] Token : ")
invite = input(" [>] Invite : ")
if "https://discord.gg/" in invite:
    invite = invite.replace("https://discord.gg/", "")
elif "https://discord.com/invite/" in invite:
    invite = invite.replace("https://discord.com/invite", "")
req = requests.delete(f"https://discord.com/api/v9/invites/{invite}", headers={"content-type": "application/json", "authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9002 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",})
if req.status_code == 200:
    print(f" [<] Invite successfully deleted [{req.status_code}]")
else:
    print(f" [<] There was an error deleting the invite [{req.status_code}]\n [<] Error : {req.text}")
os.system("pause >nul")
