import http.client


def get_my_ip() -> str:
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = conn.getresponse().read().decode("utf-8")
    return ip


if __name__ == "__main__":
    print(get_my_ip())
