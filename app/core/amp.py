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
    <script custom-template="amp-mustache"
      src="https://cdn.ampproject.org/v0/amp-mustache-0.2.js" async
    ></script>
    <style amp4email-boilerplate></style>
    <style amp-custom>
      .window {
        background: #f5e5d3;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
        color: #595959;
        display: flex;
        justify-content: center;
        margin:0;
      }
      .window-container {
        margin-top:2%;
        background-color: #fcf8f4;
        padding: 20px 50px 50px 50px;
        border-radius: 10px;
        width:40%;
      }
      .feedback-department {
        appearance: none;
        border: 2px solid #de896e;
        border-radius: 10px;
        background-color: #fcf8f4;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
        font-weight: 500;
        font-size: 18px;
        line-height: 22px;
        margin-bottom: 15px;
        padding: 13px;
        width: 100%;
        box-sizing: border-box;
      }
      .numbers,
		.slider {
  			display: flex;
  			justify-content: space-between;
	  }

      .numbers span,
		.slider span {
          width: 0;
          flex-grow: 1;
          text-align: center;
	  }

	  .slider span {
  			flex-grow: 1;
	  }

      .slider input {
        flex-grow: 24;
        margin-left: -2px; 
        margin-right: -2px;
      }
      textarea {
        appearance: none;
        border: 2px solid #de896e;
        background-color: #fcf8f4;
        font-family: "Montserrat", Arial, Helvetica, sans-serif;
        height: 80px;
        width:98%;
        border-radius: 10px;
        background-color: #fcf8f4;
        resize: none;
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
      .submit:hover {
        background-color: #de896e;
        cursor: pointer;
      }
      .error{
        color: red;
        padding-top: 15px;
		text-align: center;
      }
      .success{
        color: green;
        padding-top: 15px;
		text-align: center;
      }
    </style>
  </head>

  <body class="window">
    <div class="window-container">        
      '''

logo = '''
    <amp-img alt="yoursuprise" src="https://s3-eu-west-1.amazonaws.com/tpd/logos/496768280000640005040244/0x0.png" width="50" height="10" layout="responsive">
    </amp-img>   
'''

logo_fall = '''
    <img alt="yoursuprise" src="https://s3-eu-west-1.amazonaws.com/tpd/logos/496768280000640005040244/0x0.png" width="450em">
    </img>   
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
      .button:hover{
        background-color: #de896e;
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
        <div submit-success class="success">
          <template type="amp-mustache">
            Survey submitted!
          </template>
        </div>
        <div submit-error class="error">
          <template type="amp-mustache">
            The submission failed.. Did you already send it?
          </template>
        </div>
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
     <p>{}</p>
     <div class="enps">
        <div class="numbers">
          <span>0</span><span>1</span><span>2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span>
        </div>
        <div class="slider">
          <span>
          </span>
          <input type="range" min="0" max="10" name="score" value="5"/>
          <span>
          </span>
        </div>
    </div>

'''

department = '''
    <p class="text">{}</p>
        <select id="roles" name="dep" class="feedback-department">
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
    <textarea name="custom{}"></textarea>
'''
