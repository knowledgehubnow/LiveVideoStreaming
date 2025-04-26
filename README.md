📡 Live Video Streaming Project
This project is a WebRTC-based live video streaming platform with real-time live chat and viewer reactions — built with Django Channels and pure WebRTC on the frontend.
It supports broadcasting, viewing, ICE handling, and auto-reconnect for better reliability.

✨ Features
📺 Live broadcast from browser (camera and mic)

👀 Real-time viewing with ultra-low latency

🧊 Automatic WebRTC ICE candidate gathering

🔄 Viewer auto-reconnect if connection is lost

🎥 Multiple viewers supported

💬 Future: Integrated live chat and reactions

🔥 Simple and lightweight frontend (no big frameworks)

README.md
🛠 Tech Stack
Backend: Django, Django Channels (WebSocket)

Frontend: HTML5, JavaScript (Vanilla), WebRTC API

WebSocket: Native browser WebSocket client

Streaming Protocol: Peer-to-peer WebRTC

🚀 How to Run Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/video-streaming-project.git
cd video-streaming-project
2. Install Backend Dependencies
bash
Copy
Edit
pip install -r requirements.txt
(Requirements include Django, Channels, daphne, etc.)

3. Start Django Server
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
📝 Note: Ensure WebSocket support (ASGI mode enabled via daphne or uvicorn for production).

4. Open in Browser
Broadcaster: Go to http://127.0.0.1:8000/broadcast/

Viewer: Go to http://127.0.0.1:8000/view/

⚙️ WebRTC Core Concepts Used
RTCPeerConnection

onicecandidate

ontrack

addTrack

SDP offer/answer exchange via WebSocket

Manual fallback for remoteVideo.play() if autoplay fails

📈 Future Improvements
Multi-stream broadcast (multiple rooms)

Live chat during broadcast

Viewer reactions (emoji overlays)

Recording and storing broadcasts

Viewer count and analytics

Mobile browser optimization

🧠 Important Notes
This project uses peer-to-peer streaming (no SFU/MCU server yet).

Works best on Chrome, Edge, Firefox (latest versions).

Browser permissions (camera, microphone) are required.

For production deployment, use secure WebSockets (wss://) and HTTPS.

📸 Screenshots
(You can add screenshots of the Broadcast page and Viewer page here.)

🤝 Contributions
Pull requests are welcome!
Feel free to open issues if you want new features or find bugs.

📜 License
This project is licensed under the MIT License.

🚀 Let's Stream Live!
Would you like me to also create a small version for just the README.txt format if you want something even simpler without GitHub markdown formatting?
(Example: if you're just distributing a ZIP file.) 📁
