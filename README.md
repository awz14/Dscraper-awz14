# Discord Server Scraper

**Wassup!**  
I know you needed this—though it may seem random, it surely has its use! I hope it works well for you, and let's hope it doesn't get patched! If you have any questions, feel free to add me on Discord: **`awz14`**.

---

## 🚀 **How to Set Up**

### 1. **Install Requirements**

In the project directory, run the following command to install all required dependencies:

```bash
pip install -r requirements.txt

### 2. Run the Script

Execute **`find.py`** to start scraping the Discord servers. The script will:

- Save the server invites in **`invites.txt`**.
- Ensure **no duplicates** are included.
- Only include servers with **10k+ members**.

The script will stop once it finds **100 unique servers**.

---

## ⚙️ **Requirements**

Make sure you have these Python libraries installed:

- **`requests`**: For handling HTTP requests.
- **`beautifulsoup4`**: For parsing and scraping HTML content.

You can install them by running:

```bash
pip install -r requirements.txt

---

## 📥 **How the Script Works**

The script is designed to scrape Discord server invites from Discadia, filtering only those with **10k+ members**. Here's how it works:

1. **Scrapes servers**: It scrapes pages sorted by member count to ensure the largest communities are found.
2. **Avoids duplicates**: Any server that’s already been scraped will not be included again in the list.
3. **Stores results**: Server invites are stored in **`invites.txt`**.

### **Important Notes:**
- The script will run until it finds **100 unique servers**.
- You must have an internet connection for the script to access Discadia's website.

---

## 💬 **Questions?**

If you have any questions or if something isn’t working as expected, feel free to reach out to me on Discord:  
**`awz14`**
