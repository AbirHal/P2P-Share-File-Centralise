# 📂P2P-Share-File-Centralise
Python code for a peer-to-peer **file sharing** system.

---

# Features
- Uses **multithreading** to connect multiple clients to server.
- Uses **socket connection** to have peer-to-peer connection.
- Each peer has many options:
  - Register (to register a new file and make it available for other peers)
  - Search (to search for files available)
  - List all files (to list all files available at all peers)
  - Download (to download a particular file from given port at which it is available).

---
# 🚀 Installation
## Running locally

###### 1. Clone or Download the repository.

    git clone https://github.com/AbirHal/P2P-Share-File-Centralise.git
    cd P2P-Share-File-Centralise

###### 2. Start the server:

    python3 server.py

###### 3. Connect client in other terminal:

    python3 client.py

##### 4. Server runs at port 3456. Change port if port is busy in server.py and client.py file.

---

# 📷 Screenshots

![screen](https://user-images.githubusercontent.com/77001053/215157885-cbf909cc-6256-4744-a098-27cbe9e04a36.png)
