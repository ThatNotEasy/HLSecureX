# **HLSecureX: Secure Streaming Simplified**

**HLSecureX** is a platform for delivering encrypted video streams using **HLS (HTTP Live Streaming)**. It ensures robust AES-128 encryption and secure key delivery, making your media accessible and protected.

---

## **Features**
- **End-to-End Encryption**: Protects video segments with AES-128.
- **SKD-Like Key Management**: Simulates `skd://` for secure key delivery.
- **Cross-Platform Streaming**: Compatible with players like VLC and web-based HLS players.
- **Dynamic Key Generation**: Creates unique encryption keys and IVs for each session.
- **Secure Key Delivery**: Requires a `Bearer` token for key access.
- **Lightweight and Self-Hosted**: Runs locally or on the cloud.

---

## **Use Cases**
- **Media Streaming**: Secure live or on-demand streaming.
- **Corporate Training**: Protect sensitive training materials.
- **Film Distribution**: Prevent piracy of premium content.
- **Development**: Prototype secure streaming workflows.

---

## **How It Works**
1. Upload your video.
2. HLSecureX converts it into encrypted segments and playlists.
3. Secure key delivery ensures only authorized players can decrypt and stream.

---

## **Process Overview**

### **1. Creating Encrypted Segments**
- Segments (`segment-0.ts`, `segment-1.ts`, etc.) are encrypted and saved in `hls_files/`.

![3](https://github.com/user-attachments/assets/37e52904-1683-4fd9-a9c3-e1bd84ccc3a0)

### **2. Encoding with FFmpeg**
- FFmpeg encodes and encrypts video, generating `.ts` segments and a `.m3u8` playlist.

![image](https://github.com/user-attachments/assets/955101c6-5142-4ced-8dd3-52494447915d)


### **3. Flask Server and Playback**
Flask serves:
- Playlist: `http://localhost:5000/playlist/output.m3u8`.
- Encrypted segments and keys for authorized playback.
  
![image](https://github.com/user-attachments/assets/73060f9d-8d59-49db-b5e6-d4d04f28ba2c)

---
