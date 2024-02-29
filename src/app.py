from flask import Flask, render_template, request, jsonify
from classes.language import FormalLanguage
  
app = Flask(__name__) 
  
@app.route("/") 
def home(): 
    return render_template(
         "index.html"
    )

@app.route('/', methods=['POST'])
def create_language():
    data = request.form
    global language

    if 'alphabet' in data:

        alphabet = request.form.get('alphabet')
        
        language = FormalLanguage(alphabet)

        result = f"Formal Language's Alphabet: {alphabet}"

        # Send the result back to the front-end
        return jsonify({'result': result})

    elif 'length' in data:

        length = int(request.form.get('length'))

        strings = language.generate_strings(length)

        result = f"Strings: {strings}"

        # Send the result back to the front-end
        return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)