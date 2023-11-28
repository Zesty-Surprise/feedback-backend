global head_amp
global head_fall
global footer_amp
global footer_fall
global logo
global enps
global department
global question 

head_amp = '''
    <!DOCTYPE html>
<html amp4email data-css-strict lang="en">
  <head>
    <meta charset="utf-8" />
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <script
      async
      custom-element="amp-form"
      src="https://cdn.ampproject.org/v0/amp-form-0.1.js"
    ></script>
    <style amp4email-boilerplate></style>
    <style amp-custom>
      p {
        font-weight: bold;
      }
      body {
        background: #f5e5d3;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
        color: #595959;
      }
      .container {
        max-width: 420px;
        margin: 50px auto;
        background-color: #fcf8f4;
        padding: 20px 50px 50px 50px;
        border-radius: 10px;
        box-shadow: 10px 10px 2px 2px #e6d5c3;
      }
      .feedback-input {
        font-weight: 500;
        font-size: 18px;
        line-height: 22px;
        margin-bottom: 15px;
        padding: 13px;
        width: 100%;
        box-sizing: border-box;
      }
      textarea {
        height: 150px;
        line-height: 150%;
        border-radius: 10px;
        border-width: 2px;
        border-color: #de896e;
        background-color: #fcf8f4;
        resize: none;
      }
      .radio-label {
        display: inline-block;
        vertical-align: top;
        margin-top: 0.5%;
        margin-right: 1.5%;
      }

      .feedback-input {
        appearance: none;
        border: 2px solid #de896e;
        background-color: #fcf8f4;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
      }
      .radio-input {
        display: inline-block;
        appearance: none;
        border-radius: 50%;
        width: 22px;
        height: 22px;
        border: 2px solid #de896e;
        background-color: #fcf8f4;
        margin-right: 3.3%;
      }
      .radio-label {
        display: inline-block;
        appearance: none;
        border-radius: 50%;
        width: 22px;
        height: 22px;
        margin-left: 9px;
      }
      .radio-input:checked {
        border: 6px solid #96533f;
      }
      .enps {
        border-radius: 10px;
        border-width: 10px;
        margin: auto;
      }
      .submit {
        margin-top: 3%;
        width: 100%;
        font-size: 20px;
        font-weight: 700;
        color: #fcf8f4;
        border-radius: 10px;
        border: 0;
        background-color: #595959;
        padding: 10px;
      }
      img{
        margin-bottom: 5%;
      }
      h1{
       font-size: 65px;
      }
    </style>
  </head>

  <body>
    <div class="container">      
      '''

# logo = '''
# <amp-img
#   alt="A view of the sea"
#   src="https://assets.yoursurprise.com/images/template/logo-yoursurprise-2023.svg"
#   width="700"
#   height="250"
#   layout="responsive"
# >
# </amp-img>
# '''


logo = '''
<h1>YourSurprise</h1>
'''


head_fall = '''
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <style>
      p {
        font-weight: bold;
      }
      body {
        background: #f5e5d3;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
        color: #595959;
      }
      .container {
        max-width: 420px;
        margin: 50px auto;
        background-color: #fcf8f4;
        padding: 20px 50px 50px 50px;
        border-radius: 10px;
        box-shadow: 10px 10px 2px 2px #e6d5c3;
      }
      .feedback-input {
        font-weight: 500;
        font-size: 18px;
        line-height: 22px;
        margin-bottom: 15px;
        padding: 13px;
        width: 100%;
        box-sizing: border-box;
      }
      textarea {
        height: 150px;
        line-height: 150%;
        border-radius: 10px;
        border-width: 2px;
        border-color: #de896e;
        background-color: #fcf8f4;
        resize: none;
      }
      .radio-label {
        display: inline-block;
        vertical-align: top;
        margin-top: 0.5%;
        margin-right: 1.5%;
      }

      .feedback-input {
        appearance: none;
        border: 2px solid #de896e;
        background-color: #fcf8f4;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
      }
      .radio-input {
        display: inline-block;
        appearance: none;
        border-radius: 50%;
        width: 22px;
        height: 22px;
        border: 2px solid #de896e;
        background-color: #fcf8f4;
        margin-right: 3.3%;
      }
      .radio-label {
        display: inline-block;
        appearance: none;
        border-radius: 50%;
        width: 22px;
        height: 22px;
        margin-left: 9px;
      }
      .radio-input:checked {
        border: 6px solid #96533f;
      }
      .enps {
        border-radius: 10px;
        border-width: 10px;
        margin: auto;
      }
      .button{
        margin-top: 3%;
        width: 100%;
        font-size: 20px;
        font-weight: 700;
        color: #fcf8f4;
        border-radius: 10px;
        border: 0;
        background-color: #595959;
        padding: 10px;
      }
      a:link{
        text-decoration: none;
        text-align: center;
        font-size: 20px;
        font-weight: 700;
      }
      a{
        text-decoration: none;
        text-align: center;
        font-size: 20px;
        font-weight: 700;
      }
      img{
        margin-bottom: 5%;
      }
      h1{
       font-size: 65px;
      }
    </style>
  </head>

  <body>
    <div class="container">      
    '''

footer_amp = '''
            <input type="submit" value="SUBMIT" class="submit" />
      </form>
    </div>
  </body>
</html>
'''

footer_fall = '''
    </div>
  </body>
</html>
'''

enps = '''
     <p class="text">{}</p>
        <div class="enps">
          <input class="radio-input" type="radio" name="score" value="1" />
          <input class="radio-input" type="radio" name="score" value="2" />
          <input class="radio-input" type="radio" name="score" value="3" />
          <input class="radio-input" type="radio" name="score" value="4" />
          <input class="radio-input" type="radio" name="score" value="5" />
          <input class="radio-input" type="radio" name="score" value="6" />
          <input class="radio-input" type="radio" name="score" value="7" />
          <input class="radio-input" type="radio" name="score" value="8" />
          <input class="radio-input" type="radio" name="score" value="9" />
          <input class="radio-input" type="radio" name="score" value="10" />
        </div>
        <div class="enps">
        <label for="input" class="radio-label">1</label>
        <label for="input" class="radio-label">2</label>
        <label for="input" class="radio-label">3</label>
        <label for="input" class="radio-label">4</label>
        <label for="input" class="radio-label">5</label>
        <label for="input" class="radio-label">6</label>
        <label for="input" class="radio-label">7</label>
        <label for="input" class="radio-label">8</label>
        <label for="input" class="radio-label">9</label>
        <label for="input" class="radio-label">10</label>
      </div>
'''

department = '''
    <p class="text">{}</p>
        <select id="roles" name="dep" class="feedback-input">
          <option value="Customer Service">
            <label>Customer Service</label>
          </option>
          <option value="E-commerce"><label>E-commerce</label></option>
          <option value="Finance"><label>Finance</label></option>
          <option value="Gifts"><label>Gifts</label></option>
          <option value="Innovation"><label>Innovation</label></option>
          <option value="IT"><label>IT</label></option>
          <option value="People"><label>People</label></option>
          <option value="Production"><label>Production</label></option>
          <option value="Purchase"><label>Purchase</label></option>
        </select>
'''

question = '''
    <p class="text">{}</p>
    <textarea name="custom{}" class="feedback-input"></textarea>
'''
