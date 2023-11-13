head = '''
    <!-- {{={< >}=}} -->
    <!doctype html>
    <html amp4email data-css-strict lang="en">
    <head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>
    <style amp4email-boilerplate>body{visibility:hidden}</style>
    <style amp-custom>
    .wrapper {
      max-width: 38.5em;
      margin: 0 auto;
      font-family: arial, sans-serif;
      font-size: 1rem;
      background:#fff;
      color:#393939;
    }
    .header {
      padding: 3em 1.25em 0em;
      text-align:center;
    }
    .header amp-img {
      margin:0 auto;
      max-width: 220px;
    }
    .footer {
      text-align: center;
      padding: 3em 1em 3em;
      font-size:.8em;
    }
    .footer p {
      text-align: center;
      margin: 1.1em 1.33em;
    }
    .footer a {
      color:#393939;
    }
    .footer .link{
      font-weight:bold;
      color:#6DCCEE;
    }
    .footer .social{
      width:14em;
      margin:1.1em auto;
      display:flex;
      justify-content: space-between;
    }
    .footer .footer-nav{
      padding:1em 1em 2em;
    }
    .footer .footer-nav a{
      text-decoration:none;
    }
    .title input, .review textarea {
      width: 100%;
      box-sizing: border-box;
      padding: .5em;
      font: inherit;
      margin: .5em 0;
      color: #897f7f;
      border: 1px solid #76767676;
    }
    textarea {
      height: 150px;
    }
    .submit {
      font:inherit;
      display: inline-block;
      box-sizing: border-box;
      min-width: 10em;
      text-decoration: none;
      color: #fff;
      background-color: #097fb3;
      text-align: center;
      border-radius: 2em;
      padding: 1em 2em;
      margin: .2em 0;
      border:.2em solid #eee;
    }
    .submit:hover {
      cursor:pointer;
      background-color:#07658f;
    }
    .submit:active {
      border:.2em solid #b5b5b5;
      text-decoration: underline;
      text-decoration-color: #b5b5b5;
    }
    .amp-form-submit-success .faux {
      display: none;
    }
    h2 {
      padding: 0 2em;
      text-align: center;
    }
    h2 span {
      font-style: italic;
    }
    amp-img {
      max-width:350px;
      margin:0 auto;
    }
    .element {
      display: block;
    }
    .input {
      height: 1px;
      width: 1px;
      overflow: hidden;
      position: absolute;
      opacity:0;
    }
    .rating-default:not(:checked){
      display:none;
    }
    .ratings {
      display: inline-block;
    }
    .ratings label {
      font-size: 3.5em;
      color: #097fb3;
    }
    .rating-default:checked ~* label {
      color: #ccc;
    }
  	.rating-default:focus + .ratings label:first-of-type,
    .input:focus + label,
    .ratings:hover label {
      color: #6dccee;
    }				
    .ratings label:hover ~* {
      color: #ccc;
    }
    .ratings input:checked +* ~* {
      color: #ccc;
    }
    .sr-only:not(:focus):not(:active) {
      height: 1px;
      overflow: hidden;
      position: absolute;
      white-space: nowrap; 
      width: 1px;
    }
    </style>
    </head>
    <body>
    <article class="wrapper" aria-label="placeholder aria label" lang="en">
    <form action-xhr="https://webhook.site/b5348d30-ba02-4880-b7ca-4f094244799d" method="get" id="ic-form">
    '''

footer = '''
    <button class="submit faux" disabled>SUBMIT YOUR REVIEW</button>
    </form>
    </body>
    </html>
'''

enps = '''
    <label class="element title"><strong>{}</strong></label>
    <input type="radio" name="rating" class="rating-default input" value="" checked>
    <div class="ratings">
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="1" id="rating-1"><label for="rating-1">★<span class="sr-only">1 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="2" id="rating-2"><label for="rating-2">★<span class="sr-only">2 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="3" id="rating-3"><label for="rating-3">★<span class="sr-only">3 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="4" id="rating-4"><label for="rating-4">★<span class="sr-only">4 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="5" id="rating-5"><label for="rating-5">★<span class="sr-only">5 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="6" id="rating-6"><label for="rating-6">★<span class="sr-only">6 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="7" id="rating-7"><label for="rating-7">★<span class="sr-only">7 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="8" id="rating-8"><label for="rating-8">★<span class="sr-only">8 star of 10</span></label
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="9" id="rating-9"><label for="rating-9">★<span class="sr-only">9 star of 10</span></label>
        <input class="input" on="input-debounced:ic-form.submit" type="radio" name="rating" value="10" id="rating-10"><label for="rating-10">★<span class="sr-only">10 star of 10</span></label>
    </div>
'''

department = '''
    <label class="element title"><strong>{}</strong>
      <input type="text" name="title" on="input-debounced:ic-form.submit">
    </label>
'''

written = '''
    <label class="element review"><strong>{}</strong>
      <textarea name="review" on="input-debounced:ic-form.submit"></textarea>
    </label>
'''

def build_html(components):
    build = []
    for comp in components:
        if comp['type'] == "enps-component":
            build.append(set_text_for_component(comp, enps))
        elif comp['type'] == "department-component":
            build.append(set_text_for_component(comp, department))
        elif comp['type'] == "written-component":
            build.append(set_text_for_component(comp, written))
    build = "".join(build)
    html = head + build + footer
    return html

def set_text_for_component(comp, text):
    if comp['custom_text'] != "":
        res = text.format(comp['custom_text'])
    else:
        res = text.format(comp['default_text'])
    return res
 