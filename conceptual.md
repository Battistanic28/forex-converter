### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
      * Python is an object oriented language, JS is a scripting language.
      * Python runs on a server while JS runs in browser.
      * Python is a much less forgiving language than JS.
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
      * Try/Except
      * Check if the key exists within the dict, `"c" in dict #True`
- What is a unit test?
      * Unit tests test a single piece of functionality wihtin the code. A single function or method, for example.
- What is an integration test?
      * Integrations tests test how pieces of code intereact together.
- What is the role of web application framework, like Flask?
      * A web application framework compiles the tools reuired for web develoopment. They help us map requests, connect to a database, create customizable templates, and store state information.
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
      * URL parameters should be used to establish the broad structure of a website. Category = Color, for example.
      * Query parameters add extra detail about a specific page. Color = Blue, for example.
- How do you collect data from a URL placeholder parameter using Flask?
      * Add `<int:variable_name>` to `@app.route`
- How do you collect data from the query string using Flask?
      * `request.args`
- How do you collect data from the body of the request using Flask?
      * `request.form`
- What is a cookie and what kinds of things are they commonly used for?
      * Cookies add "state" to the HTTP protocol. They are composed of name/value pairs stored on the clients and are used to save bits of information on the browser. Cookies are used on the server side
- What is the session object in Flask?
      * Sessions add "state" to the HTTP protocol. They store bits of user information on the browser. Sessions only persist as long as the current browser window is open and are used on the client side.
- What does Flask's `jsonify()` do?
      * jsonify is a function used in Flask that converts response data into a JSON format.