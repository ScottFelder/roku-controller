import requests


class Device:
    def __init__(self, ip_address, port):
        self.base_url = f"http://{ip_address}:{port}"

    def _send_command(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error sending command to {url}: {e}")
            return None

    def press_key(self, key):
        return self._send_command(f"/keypress/{key}")

    def launch_app(self, app_id):
        return self._send_command(f"/launch/{app_id}")

    def get_active_app(self):
        response = self._send_command("/query/active-app")
        if response:
            return response.strip()
        return None
