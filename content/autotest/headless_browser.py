import sys
from playwright.sync_api import sync_playwright, Route, Response, Request


def PageRouteInterception(route):
    if isinstance(route, Route):
        if route.request.resource_type in ["image", "media", "font", "stylesheet", "manifest", "websocket", "eventsource"]:
            if '.gif' not in route.request.url:
                route.abort()
            else:
                route.continue_()
        else:
            # route.continue_(headers=headers)
            route.continue_()


def PageInterceptionRequest(request):
    pass


def PageInterceptionRequestFailure(request):
    pass


def PageInterceptionResponse(response):
    if isinstance(response, Response):
        # print(response.headers)
        # print(response)
        if "application" not in response.headers.get("content-type", "") and "javascript" not in response.headers.get(
                "content-type", ""):
            pass


def get_obj_size(obj):
    if obj:
        size_mb = sys.getsizeof(obj)
    else:
        size_mb = 0
    return size_mb


def fetch_html(url: str, chorme_path: str = 'browsers/chromium-907428/chrome-win/chrome.exe') -> tuple:
    """

    :param url:
    :param chorme_path:
    :return: (html, success)
    """

    with sync_playwright() as p:
        # webkit = p.chromium.launch(executable_path=chorme_path)
        webkit = p.chromium.launch()

        if url.lower().startswith("http://http://"):
            url = url.replace("http://", "", 1)
        print(f"fetch page: {url}")
        try:
            pageWebkit = webkit.new_page(viewport={"width": 1920, "height": 1080})
            pageWebkit.route('**/*', PageRouteInterception)
            pageWebkit.on("request", PageInterceptionRequest)
            pageWebkit.on("requestfailed", PageInterceptionRequestFailure)
            pageWebkit.on("response", PageInterceptionResponse)
            pageWebkit.goto(url, timeout=50000, wait_until="networkidle")
            pageWebkit.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
            html = pageWebkit.content()
            obj_size = get_obj_size(html)
            success = True
        except Exception as e:
            html = ""
            success = False
        finally:
            pageWebkit.close()

        webkit.close()
    return html, success


__all__ = ["fetch_html"]

if __name__ == '__main__':
    test_url = """https://ec.europa.eu/commission/presscorner/detail/en/ip_20_1006"""
    html_str, is_success = fetch_html(test_url, chorme_path=r"C:\E\proj\spider\browsers\chromium-907428\chrome-win\chrome.exe")
    print(f"is_success: {is_success}")
    print(f"html_length: {len(html_str)}")
