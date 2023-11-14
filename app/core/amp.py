head = '''
    <!doctype html>
    <html amp4email data-css-strict lang="en">
    <head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>
    <style amp4email-boilerplate></style>
    <style amp-custom>
    .wrapper {
      position: relative;
      max-width: 38.5em;
      margin: 0 auto;
      margin-top: 30px;
      text-align: center;
      align-content: center;
      font-family: arial, sans-serif;
      font-size: 1rem;
      background: #fff;
      color: #393939;
    }
    .marginer{
      margin-top: 10px;
      margin-bottom: 10px;
    }
    </style>
    </head>
    <body>
    <article class="wrapper" aria-label="placeholder aria label" lang="en">
    '''

footer = '''
    <button class="submit faux">SUBMIT YOUR REVIEW</button>
    </form>
    </article>
    </body>
    </html>
'''

enps = '''
    <div class="marginer">
    <label class="element title"><strong>{}</strong></label>
    <div class="score">
        <input class="input" type="radio" name="score" value="1" id="score-1">1</label>
        <input class="input" type="radio" name="score" value="2" id="score-2">2</label>
        <input class="input" type="radio" name="score" value="3" id="score-3">3</label>
        <input class="input" type="radio" name="score" value="4" id="score-4">4</label>
        <input class="input" type="radio" name="score" value="5" id="score-5">5</label>
        <input class="input" type="radio" name="score" value="6" id="score-6">6</label>
        <input class="input" type="radio" name="score" value="7" id="score-7">7</label>
        <input class="input" type="radio" name="score" value="8" id="score-8">8</label>
        <input class="input" type="radio" name="score" value="9" id="score-9">9</label>
        <input class="input" type="radio" name="score" value="10" id="score-10">10</label>
    </div>
    </div>
'''

department = '''
    <div class="marginer">
    <label class="element dep"><strong>{}</strong>
      <input type="text" name="dep">
    </label>
    <br>
    </div>
'''

written = '''
    <div class="marginer">
    <label class="element review"><strong>{}</strong>
     <input type="text" name="more">
    </label>
    <br>
    </div>
'''

def build_html(components, url:str):
    host = 'localhost:8000'
    form_url = '<form action-xhr="http://{}/api/file/{}" method="get" id="ic-form">'.format(host, url)
    build = []
    
    for comp in components:
        if comp['type'] == "enps-component":
            build.append(set_text_for_component(comp, enps))
        elif comp['type'] == "department-component":
            build.append(set_text_for_component(comp, department))
        elif comp['type'] == "written-component":
            build.append(set_text_for_component(comp, written))
    build = "".join(build)

    html = head + form_url + build + footer

    return html

def set_text_for_component(comp, text):
    if comp['custom_text'] != "":
        res = text.format(comp['custom_text'])
    else:
        res = text.format(comp['default_text'])
    return res
 