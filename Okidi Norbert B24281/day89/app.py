import asyncio
import aiohttp

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def download_pages(urls):
    tasks = [fetch_page(url) for url in urls]
    pages = await asyncio.gather(*tasks)
    return pages

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]

    pages = await download_pages(urls)

    for url, page in zip(urls, pages):
        print(f"Content from {url}:\n{page[:100]}...\n")

if __name__ == "__main__":
    asyncio.run(main())