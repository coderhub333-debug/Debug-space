import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})

        # Load local HTML file
        file_url = f"file://{os.getcwd()}/index.html"
        await page.goto(file_url)

        # Focus cart open button
        await page.focus("#cart-open")
        await page.wait_for_timeout(500) # Ensure focus styles apply
        await page.screenshot(path="/home/jules/verification/cart_open_focused.png")

        # Focus open drawer button
        await page.focus("#open-drawer-btn")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/menu_focused.png")

        await browser.close()
        print("Screenshots taken.")

asyncio.run(main())
