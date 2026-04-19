import requests
import re
import time
from Crypto.Cipher import AES
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich import box
from rich.align import Align
from rich.text import Text

console = Console()


models = [
    "DeepSeek-V1",
    "DeepSeek-V2",
    "DeepSeek-V2.5",
    "DeepSeek-V3",
    "DeepSeek-V3-0324",
    "DeepSeek-V3.1",
    "DeepSeek-V3.2",
    "DeepSeek-R1",
    "DeepSeek-R1-0528",
    "DeepSeek-R1-Distill",
    "DeepSeek-Prover-V1",
    "DeepSeek-Prover-V1.5",
    "DeepSeek-Prover-V2",
    "DeepSeek-VL",
    "DeepSeek-Coder",
    "DeepSeek-Coder-V2",
    "DeepSeek-Coder-6.7B-base",
    "DeepSeek-Coder-6.7B-instruct",
]

header = """
╔═══════════════════════════════════════════╗
║                                           ║
║    🤖 DEEPSEEK AI CHAT INTERFACE 🤖      ║
║                                           ║
║        Developer: Shakal Bhau             ║
║                                           ║
╚═══════════════════════════════════════════╝
"""

print("\n")
print(
    Panel.fit(
        Align.center(Text(header, style="bold bright_cyan")),
        border_style="bright_green",
        title="[bold yellow]🌟 WELCOME 🌟[/bold yellow]",
        subtitle="[bold magenta]💎 Premium Edition 💎[/bold magenta]",
    )
)


print("\n[bold yellow]═══════════════════════════════════════[/bold yellow]")
print("[bold bright_white]       📋 CHOOSE YOUR AI MODEL        [/bold bright_white]")
print("[bold yellow]═══════════════════════════════════════[/bold yellow]\n")

table = Table(
    show_header=True,
    box=box.DOUBLE_EDGE,
    border_style="bright_blue",
    header_style="bold bright_yellow",
)
table.add_column("№", style="bold cyan", justify="center", width=5)
table.add_column("🤖 Model Name", style="bright_white", width=35)
table.add_column("Status", style="green", justify="center", width=10)

for i, m in enumerate(models, 1):
    status = "✅ Ready"
    table.add_row(f"{i}", m, status)

console.print(table)

while True:
    try:
        choice = Prompt.ask(
            "\n[bold bright_green]👉 Enter Model Number[/bold bright_green]",
            default="1",
        )
        choice_num = int(choice)
        if 1 <= choice_num <= len(models):
            model = models[choice_num - 1]
            break
        else:
            print("[bold red]❌ Invalid number! Choose between 1-18[/bold red]")
    except:
        print("[bold red]❌ Please enter a valid number![/bold red]")

print(
    f"\n[bold green]✅ Selected Model:[/bold green] [black on bright_cyan] {model} [/black on bright_cyan]\n"
)


print(
    Panel.fit(
        "[bold yellow]⚙️  Initializing AI Session...[/bold yellow]",
        border_style="yellow",
    )
)

with console.status("[bold bright_yellow]🔄 Loading AI Engine...", spinner="dots"):
    try:
        s = requests.Session()
        s.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Android 12; Mobile; rv:97.0) Gecko/97.0 Firefox/97.0"
            }
        )

        r = s.get("https://asmodeus.free.nf/")
        nums = re.findall(r'toNumbers\("([a-f0-9]+)"\)', r.text)
        key, iv, data = [bytes.fromhex(n) for n in nums[:3]]

        s.cookies.set(
            "__test",
            AES.new(key, AES.MODE_CBC, iv).decrypt(data).hex(),
            domain="asmodeus.free.nf",
        )
        s.get("https://asmodeus.free.nf/index.php?i=1")
        time.sleep(0.8)

        print(
            "\n[bold bright_green]✅ AI Session Successfully Initialized![/bold bright_green]\n"
        )
    except Exception as e:
        print(f"\n[bold red]❌ Error: {e}[/bold red]")
        exit()

print(
    Panel.fit(
        "[bold bright_white]💬 Chat Interface Active | Type 'exit' to quit[/bold bright_white]",
        border_style="bright_green",
        title="[bold yellow]🔥 READY TO CHAT 🔥[/bold yellow]",
    )
)

message_count = 0

while True:
    msg = Prompt.ask("\n[bold bright_cyan]📝 You[/bold bright_cyan]").strip()

    if msg.lower() in ["exit", "quit", "bye"]:
        print(
            Panel.fit(
                "[bold bright_yellow]👋 Thanks for using DeepSeek AI!\n🔔 Follow on GitHub: github.com/ShakalBhau0001 | If you enjoyed this project, don’t forget to star the repo ⭐[/bold bright_yellow]",
                border_style="bright_magenta",
                title="[bold red]GOODBYE[/bold red]",
            )
        )
        break

    if not msg:
        print("[bold red]⚠️ Please enter a message![/bold red]")
        continue

    message_count += 1

    with console.status(
        f"[bold bright_yellow]🧠 AI is thinking... (Query #{message_count})",
        spinner="bouncingBall",
    ):
        try:
            r = s.post(
                "https://asmodeus.free.nf/deepseek.php",
                params={"i": "1"},
                data={"model": model, "question": msg},
            )

            reply = re.search(
                r'<div class="response-content">(.*?)</div>', r.text, re.DOTALL
            )
            response_text = (
                reply.group(1).strip() if reply else "⚠️ No response received"
            )

        except Exception as e:
            response_text = f"❌ Error: {str(e)}"

    print(f"\n[bold bright_magenta]🤖 {model} Response:[/bold bright_magenta]")
    print(
        Panel(
            response_text,
            border_style="bright_magenta",
            title=f"[bold green]💡 Answer #{message_count}[/bold green]",
            subtitle="[bold cyan]Powered by DeepSeek AI[/bold cyan]",
        )
    )
