from playwright.sync_api import sync_playwright
import time
from flask import Flask,jsonify,request



# Flask-App
APP = Flask(__name__)


PLAY = sync_playwright().start()
BROWSER = PLAY.firefox.launch_persistent_context(
    user_data_dir="tmp",
    headless=False,
)
PAGE = BROWSER.new_page()


# Functions

def get_message():
    """Get the latest message"""
    while is_loading_response():
        time.sleep(0.25)
    page_elements = PAGE.query_selector_all("div[class*='text-base']")
    if page_elements != []:
            last_element = page_elements.pop()
            return last_element.inner_text()
    else:
        return None

def get_input_box():
    #Get textarea
    return PAGE.query_selector("textarea")

def is_logged_in():
    # See if we have a textarea with data-id="root"
    return get_input_box() is not None

def is_loading_response() -> bool:
    return not PAGE.query_selector("textarea ~ button").is_enabled()

def send_message(message):
    textbox = get_input_box()
    textbox.click()
    textbox.fill(message)
    textbox.press("Enter")


def regenerate_response():
    """Clicks on the Try again button.
    Returns None if there is no button"""
    try_again_button = PAGE.query_selector("button:has-text('Try again')")
    if try_again_button is not None:
        try_again_button.click()
    return try_again_button


@APP.route("/chat", methods=["GET","POST"]) 
def chat():
    if request.method =="POST":
        message = request.args.get("q")
        send_message(message)
        response = get_message()
        return jsonify({'response':response})
    elif request.method =="GET":
        response = get_message()
        if response != None:
            return jsonify({'response':response})
        else:
            return jsonify({'response':'No Response'})
        

# create a route for regenerating the response
@APP.route("/regenerate", methods=["POST"])
def regenerate():
    if regenerate_response() is None:
        return "No Response"
    response = get_message()
    return jsonify({'response':response})

@APP.route("/reset", methods=["POST"])
def reset():
    global PAGE
    print("Resetting chat")
    PAGE.reload()
    return "Restarted Chat-Gpt"

@APP.route("/restart", methods=["POST"])
def restart():
    global PAGE,BROWSER,PLAY
    PAGE.close()
    BROWSER.close()
    PLAY.stop()
    time.sleep(1)
    PLAY = sync_playwright().start()
    BROWSER = PLAY.firefox.launch_persistent_context(
        user_data_dir="tmp",
        headless=False,
    )
    PAGE = BROWSER.new_page()
    PAGE.goto("https://chat.openai.com/")
    return "Restarted API"

def run_project():
    PAGE.goto("https://chat.openai.com/")
    if not is_logged_in():
        print("Please log in to OpenAI Chat")
        print("Press enter when you're done")
        input()
    else:
        print("Logged in")
        APP.run(port=8000, threaded=False)

if __name__ == "__main__":
    run_project()