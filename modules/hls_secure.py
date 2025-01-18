import os
import subprocess

class HLSecureX:
    def __init__(self):
        # Configuration
        self.hls_dir = "hls_files"
        os.makedirs(self.hls_dir, exist_ok=True)  # Ensure directory exists

        # File paths
        self.content_key_file = os.path.join(self.hls_dir, "content.key")
        self.key_info_file = os.path.join(self.hls_dir, "key_info.txt")
        self.input_file = "11331.mp4"
        self.output_file = os.path.join(self.hls_dir, "output.m3u8")

        # Dynamic Key ID
        self.key_id = os.urandom(8).hex()

    def generate_content_key(self):
        """
        Generate a 16-byte content key and save it to the content.key file.
        """
        try:
            key = os.urandom(16)
            with open(self.content_key_file, "wb") as f:
                f.write(key)
            print(f"Generated content key: {key.hex()}")
        except Exception as e:
            raise RuntimeError(f"Failed to generate content key: {e}")

    def create_key_info_file(self, key_uri, iv):
        """
        Create the key_info.txt file for FFmpeg encryption.
        """
        try:
            with open(self.key_info_file, "w") as f:
                f.write(f"{key_uri}/{self.key_id}\n{self.content_key_file}\n{iv}\n")
            print("Generated key_info.txt with encryption details.")
        except Exception as e:
            raise RuntimeError(f"Failed to create key_info.txt: {e}")

    def generate_hls(self, segment_duration=6):
        """
        Generate HLS playlist and segments using FFmpeg.
        """
        command = [
            "ffmpeg",
            "-i", self.input_file,
            "-hls_time", str(segment_duration),
            "-hls_key_info_file", self.key_info_file,
            "-hls_playlist_type", "vod",
            "-hls_segment_filename", os.path.join(self.hls_dir, "segment-%d.ts"),
            self.output_file
        ]
        try:
            print(f"Running command: {' '.join(command)}")
            subprocess.run(command, check=True)
            print("HLS generation complete.")
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error during HLS generation: {e}")

    def setup_workflow(self, key_uri="http://localhost:5000/key", iv=None):
        if not iv:
            iv = os.urandom(16).hex()

        self.generate_content_key()
        self.create_key_info_file(key_uri=key_uri, iv=iv)
        self.generate_hls()