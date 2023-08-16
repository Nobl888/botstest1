```python
import bot
import config

def main():
    bot.run_bot(config.DEXTOOLS_API_KEY, config.DEXSCREENER_API_KEY)

if __name__ == "__main__":
    main()
```