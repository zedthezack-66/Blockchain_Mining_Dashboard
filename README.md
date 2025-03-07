Monero CPU Mining Dashboard 🚀
This is a Monero mining dashboard that uses CPU power to mine XMR (Monero). It is designed for easy scalability, allowing  its users to expand to Bitcoin (BTC), Ethereum (ETH), or other cryptocurrencies using GPUs.

The project includes a real-time mining statistics dashboard built with HTML, CSS (Bootstrap), and JavaScript. It can display key mining info such as hash rate and blocks mined, with an optional backend for live data fetching.

🌟 Features
✅ Monero (XMR) CPU Mining Support
✅ Live Statistics – Displays real-time hash rate & blocks mined
✅ Dark-Themed UI – Modern, sleek, and responsive
✅ Auto-Updating Dashboard – Fetches mining info every 3 seconds
✅ Animations & Interactive UI – Hover effects & moving text
✅ Scalable to BTC, ETH & GPU Mining – Can be modified for other cryptocurrencies

🚀 Installation & Setup
1️⃣ Clone the Repository

2️⃣ Install Monero Mining Software
To start mining Monero (XMR), install XMRig (a CPU miner).
📌 Install XMRig (for Monero CPU Mining)
bash
Copy
Edit
sudo apt update && sudo apt install xmrig
For Windows: Download from XMRig's official site

3️⃣ Configure XMRig for Mining

4️⃣ Start Mining
./xmrig
This will start mining Monero using your CPU.

🖥️ Running the Dashboard
1️⃣ Open the Dashboard
Open index.html in a web browser to view the mining stats.
2️⃣ (Optional) Set Up a Backend for Live Data
For real-time data, run a Flask API that simulates mining stats.

📌 Install Python & Flask
pip install flask

📌 Run the Flask Server
Run the script (python server.py) to serve real stats.

💪 Scaling to GPU Mining (BTC, ETH, etc.)
To scale this miner to Bitcoin (BTC) or Ethereum (ETH) using GPUs, switch from XMRig to mining software like NBMiner, T-Rex, or PhoenixMiner.
Modify config.json to connect to BTC/ETH mining pools like SlushPool or Ethermine.

 📌Feel free to fork, modify, and contribute to this mining dashboard! Ideas Include :
       -Add GPU mining support (for BTC, ETH, etc.)
       -Improve UI with more real-time stats
       -Adding coin support (auto-switch mining)🚀
