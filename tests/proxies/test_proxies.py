from scrape_tools.proxies import Proxy, AuthProxy


def test_get_address():
    assert Proxy(host="any_host", port="any_port").get_address() == {
        "http": "any_host:any_port",
        "https": "any_host:any_port",
    }
    assert AuthProxy(
        host="any_host",
        port="any_port",
        name="any_name",
        password="any_password",
    ).get_address() == {
        "http": "http://any_name:any_password@any_host:any_port",
        "https": "http://any_name:any_password@any_host:any_port",
    }
